from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]') # Раздел "Профиль"
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]') # Раздел "История заказов"
    LOGOUT_BUTTON = (By.XPATH, '//button[@class = "Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') # Кнопка "Выйти", логаут
    REGISTER_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]') # Кнопка "Зарегистрироваться"
    DESCRIPTION_OF_SECTION = (By.XPATH, '//p[contains(@class, "Account_text")]') # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"


class MainPageLocators:
    BUTTON_LOGIN_MAIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]') # Кнопка "Войти в аккаунт" на главной
    BUTTON_PERSONAL_ACC = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')# Кнопка "Личный кабинет"
    BUTTON_MAKE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')# Кнопка "Оформить заказ"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')# Кнопка "Конструктор" в шапке сайта
    SELECTED_BUTTON = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))# Селектор, помечающий выбранный раздел конструктора как активный
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1') # Заголовок раздела "Конструктор"
    BUNS_TITLE = (By.XPATH, '//span[text() = "Булки"]') # Заголовок раздела "Булки" в меню конструктора
    SAUCES_TITLE = (By.XPATH, '//span[text() = "Соусы"]') # Заголовок раздела "Соусы" в меню конструктора
    FILLINGS_TITLE = (By.XPATH, '//span[text() = "Начинки"]') # Заголовок раздела "Начинки" в меню конструктора
    BUTTON_ORDER_LIST = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li') # Кнопка "Лента заказов"
    INGREDIENT_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]') # Ингредиент
    HEADER_INGREDIENT_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]') # Заголовок окна "Детали ингредиента"
    BUTTON_CLOSE_DETAILS = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]') # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    IMAGE_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') # Картинка ингредиента в общем списке
    PLACE_FOR_INGREDIENTS = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')   # Куда перетаскиваются игнредиенты
    CONTENT_OF_ORDER = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')   # Состав заказа в условной "Корзине"
    INGREDIENT_COUNT = (By.XPATH, '(.//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"])[1]') # Количество экземпляров ингредиента в заказе (счетчик)
    CONFIRMATION_ORDER_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')     # Окно подтверждения создания заказа
    NUMBER_OF_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2') # Номер созданного заказа в окне подтверждения
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'
                                           ']//button[contains(@class, "close")]') # Кнопка с крестиком, закрывающая окно подтвержденного заказа


class OrderHistoryPageLocators:

    ORDER_CARD_IN_HISTORY = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')    # Карточка заказа в истории заказов
    NAME_ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2') # Заголовок карточки заказа с названием бургера
    ID_CARD_OF_ORDER = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]') # Номер заказа в карточке заказа

class OrderListLocators:
    ORDER_FEED_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]') # Раздел заказов
    ORDER_FEED_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')# Заголовок ленты заказов
    ORDER_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')# Карточка заказа в ленте
    MODAL_OF_ORDER_DETAILS = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')  # Всплывающее окно с деталями заказа
    MODAL_OF_ORDER_DETAILS_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2') # Заголовок всплывающего окна с деталями заказа
    COUNTER_OF_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p') # Счетчик заказов "Выполнено за все время"
    COUNTER_OF_ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p') # Счетчик заказов "Выполнено за сегодня"
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li') # Заказ в разделе "В работе"
    ID_OF_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]') # Номер заказа в разделе "В работе"
    ID_ORDER_CARD_IN_FEED = (By.XPATH, './/*[text()="{order_id}"]') # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа


class PasswordRecoveryLocators:
    BUTTON_RECOVER_PASSWORD_MAIN = (By.XPATH, '//a[text() = "Восстановить пароль"]') # Кнопка "Восстановить пароль" на экране входа
    EMAIL_INPUT = (By.CLASS_NAME, 'input__textfield') # Поле ввода email
    BUTTON_RECOVER = (By.CLASS_NAME, 'button_button__33qZ0') # Кнопка "Восстановить" на странице ввода email
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.input_type_password .input__textfield') # Поле ввода пароля
    ICON_TO_VIEW_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') # Иконка, скрывающая (боль) пароль
    PASSWORD_FIELD_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]') # Пароль со статусом видимости
    PASSWORD_FIELD_INVISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]') # Пароль скрыт