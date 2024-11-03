import pytest
from generators import *
import requests
from urls import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser_name = request.param
    driver = None
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        ValueError("Can't create instance for this browser param")

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def generate_user_credentials():
    email = create_random_email()
    password = create_random_password()
    name = create_random_name()
    return email, password, name


@pytest.fixture
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(USER_DELETE, headers={'Authorization': access_token})


@pytest.fixture
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [
        '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
        '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79'
    ]}
    response_body = requests.post(ORDER_CREATE, data=payload, headers=headers)

    yield access_token, response_body
    requests.delete(USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
def set_user_tokens(driver, create_new_user_and_delete):
    driver.get(BASE_URL)
    user_data = create_new_user_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')
