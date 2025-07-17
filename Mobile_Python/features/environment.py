from behave import fixture, use_fixture
from appium import webdriver
from appium.options.android import UiAutomator2Options

@fixture
def appium_driver(context):
    if not hasattr(context, 'driver') or not context.driver:
        capabilities = dict(
            platformName='Android',
            automationName='UiAutomator2',
            appPackage='com.android.settings',
            appActivity='.Settings',
        )

        context.driver = webdriver.Remote(
            'http://127.0.0.1:4723',
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

def before_scenario(context, scenario):
    use_fixture(appium_driver, context)

def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
