from pages.base_page import BasePage
from generators import *
from locators import *
import allure


class PasswdRecoveryPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def navigate_to_recovery_passwd_page(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.BUTTON_RECOVER_PASSWORD_MAIN)
        self.click_on_element(PasswordRecoveryLocators.BUTTON_RECOVER_PASSWORD_MAIN)

    @allure.step('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.EMAIL_INPUT)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.EMAIL_INPUT)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.EMAIL_INPUT, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.BUTTON_RECOVER)
        self.click_on_element(PasswordRecoveryLocators.BUTTON_RECOVER)

    @allure.step('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)

    @allure.step('Ввести password')
    def send_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)
        passwd = create_random_password()
        self.send_keys_to_input(PasswordRecoveryLocators.PASSWORD_INPUT, passwd)

    @allure.step('Кликнуть на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.ICON_TO_VIEW_PASSWORD)
        self.click_on_element(PasswordRecoveryLocators.ICON_TO_VIEW_PASSWORD)

    @allure.step('Проверить, что значение поля password отображается')
    def check_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_FIELD_VISIBLE)

    @allure.step('Проверить, что значение поля password не отображается')
    def check_not_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_FIELD_INVISIBLE)
