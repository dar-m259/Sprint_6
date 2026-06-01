from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, ".//*[contains(text(), 'Сокольники')]")
    METRO_STATION_1 = (By.XPATH, ".//*[contains(text(), 'Коломенская')]")
    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")
    WHEN_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    WHEN_DATE = (By.XPATH, ".//div[text() = '15']")
    WHEN_DATE_1 = (By.XPATH, ".//div[text() = '23']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD = (By.XPATH, ".//*[contains(text(), 'сутки')]")
    RENTAL_PERIOD_1 = (By.XPATH, ".//*[contains(text(), 'семеро суток')]")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, ".//button[text() = 'Да']")

    ORDER_SUCCESS = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")