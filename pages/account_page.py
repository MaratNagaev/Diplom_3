from pages.base_page import BasePage
from locators import *
import allure


class ProfilePage(BasePage):
    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY)

    @allure.step('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Подождать прогрузки текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(ProfilePageLocators.DESCRIPTION_OF_SECTION)

    @allure.step('Проверить отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(ProfilePageLocators.DESCRIPTION_OF_SECTION)

    @allure.step('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        self.wait_visibility_of_element(ProfilePageLocators.REGISTER_BUTTON)

    @allure.step('Проверить отображение кнопки "Зарегистрироваться"')
    def check_displaying_of_button_register(self):
        return self.check_displaying_of_element(ProfilePageLocators.REGISTER_BUTTON)
