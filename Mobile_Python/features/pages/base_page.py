from datetime import time
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def procura_elemento(self, locator_type, locator):
        element = None
        try:
            if locator_type.lower() == "id":
                element = self.driver.find_element(AppiumBy.ID, locator)
            elif locator_type.lower() == "xpath":
                element = self.driver.find_element(AppiumBy.XPATH, locator)
            elif locator_type.lower() == "text":
                element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   f'new UiSelector().text("{locator}")')
        except Exception as e:
            raise e
        return element

    def espera(self, locator_type, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            if locator_type.lower() == "xpath":
                return wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
            elif locator_type.lower() == "id":
                return wait.until(EC.presence_of_element_located((AppiumBy.ID, locator)))
        except Exception as e:
            print(f"Elemento não encontrado: {locator}")
            raise e

    def clicar(self, locator_type, locator):
        self.procura_elemento(locator_type, locator).click()

    def digitar(self, locator_type, locator, texto):
        self.procura_elemento(locator_type, locator).send_keys(texto)

    def digitando_devagar(self, locator_type, locator, text, delay: float = 0.2):
        element = self.procura_elemento(locator_type, locator)
        typed_text = ""
        for char in text:
            typed_text += char
            element.clear()
            element.send_keys(typed_text)
            time.sleep(delay)

