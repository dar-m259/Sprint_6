import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self) -> str:
        return self.driver.current_url
    
    @allure.step("Ожидание элемента {locator}")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self, timeout=TIMEOUT):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)
        return True
    
    @allure.step("Ожидание загрузки страницы с {page_url} в url")
    def wait_for_page_to_load(self, page_url, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(page_url))
    
    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Скролл до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввести текст {keys} в поле {locator}")
    def send_keys_to_element(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента {locator}")
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Элемент {locator} отображается")
    def element_is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

        
