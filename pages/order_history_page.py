from pages.base_page import BasePage
import allure
from locators import *


class OrderHistoryPage(BasePage):

    @allure.step('Подождать прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_CARD_IN_HISTORY)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.NAME_ORDER_CARD)

    @allure.step('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ID_CARD_OF_ORDER)
