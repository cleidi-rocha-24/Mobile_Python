from appium import webdriver
from behave import use_fixture


def before_all(context):
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }

    context.driver = webdriver.Remote("http://localhost:4723", desired_caps)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(before_all, context)
