from datetime import time
import time

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator):
        element = None
        try:
            if locator_type.lower() == "id":
                element = self.driver.find_element(AppiumBy.ID, locator)
            elif locator_type.lower() == "xpath":
                element = self.driver.find_element(AppiumBy.XPATH, locator)
            elif locator_type.lower() == "text":
                element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   f'new UiSelector().text("{locator}")')
            # logger.info(f"Elemento encontrado - Tipo: {locator_type}, Locator: {locator}")
        except Exception as e:
            # logger.error(f"Erro ao encontrar elemento - Tipo: {locator_type}, Locator: {locator}")
            raise e
        print("passou no find element")
        return element

    def espera(self, locator_type, locator, timeout=10):
        print("entrou no met espera")
        try:
            wait = WebDriverWait(self.driver, timeout)
            if locator_type.lower() == "xpath":
                return wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
            # adicione outros tipos de localizadores conforme necessário
        except Exception as e:
            print(f"Elemento não encontrado: {locator}")
            raise e

    def click(self, locator_type, locator):
        # logger.info(f"Clicando no elemento - Tipo: {locator_type}, Locator: {locator}")
        self.find_element(locator_type, locator).click()

    def send_keys(self, locator_type, locator, texto):
        self.find_element(locator_type, locator).send_keys(texto)

    def send_keys_slowly(self, locator_type, locator, text, delay=0.2):
        element = self.find_element(locator_type, locator)
        # element.clear()

        for character in text:
            self.find_element(locator_type, locator).send_keys(character)
            time.sleep(delay)

    def get_text(self, locator_type, locator):
        text = self.find_element(locator_type, locator).text
        # logger.info(f"Texto obtido: {text} - Tipo: {locator_type}, Locator: {locator}")
        return text

    def is_selected(self, locator_type, locator):
        selected = self.find_element(locator_type, locator).is_selected()
        # logger.info(f"Elemento selecionado: {selected} - Tipo: {locator_type}, Locator: {locator}")
        return selected
