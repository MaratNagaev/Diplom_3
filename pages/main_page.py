from pages.base_page import BasePage
import allure
from locators import *


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_PERSONAL_ACC)
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACC)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_header_feed_button(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_ORDER_LIST)
        self.click_on_element(MainPageLocators.BUTTON_ORDER_LIST)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_MAIN)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_visibility_of_element(MainPageLocators.CONFIRMATION_ORDER_TITLE)
        return self.check_displaying_of_element(MainPageLocators.CONFIRMATION_ORDER_TITLE)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_1)
        self.click_on_element(MainPageLocators.INGREDIENT_1)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_INGREDIENT_DETAILS)
        return self.check_displaying_of_element(MainPageLocators.HEADER_INGREDIENT_DETAILS)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainPageLocators.HEADER_INGREDIENT_DETAILS)
        if not self.check_displaying_of_element(MainPageLocators.HEADER_INGREDIENT_DETAILS):
            return True

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_CLOSE_DETAILS)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_DETAILS)

    @allure.step('Добавить интгридиенты')
    def drag_and_drop_ingredient_to_order(self):
        source_element = self.find_element_with_wait(MainPageLocators.IMAGE_INGREDIENT)
        target_element = self.find_element_with_wait(MainPageLocators.PLACE_FOR_INGREDIENTS)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNT)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        return self.check_displaying_of_element(MainPageLocators.CONFIRMATION_ORDER_TITLE)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainPageLocators.NUMBER_OF_ORDER, '9999')
        return self.get_text_on_element(MainPageLocators.NUMBER_OF_ORDER)

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_modal(self):
        self.check_element_is_clickable(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
