import unittest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
#
# capabilities = dict(
#     platformName='Android',
#     automationName='UiAutomator2',
#     appPackage='com.android.settings',
#     appActivity='.Settings',
# )
#
# appium_server_url = 'http://127.0.0.1:4723'
#
# driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
# element1 = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/deny_radio_button").click
# # element1.click()
# driver.quit()
import unittest

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
#
#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()
#
#     def test_find_battery(self) -> None:
#         el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
#         el.click()
#
# if __name__ == '__main__':
#     unittest.main()