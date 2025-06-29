from behave import fixture, use_fixture
from appium import webdriver
from appium.options.android import UiAutomator2Options
# from utils.logger import setup_logger
import os

# logger = setup_logger(__name__)


@fixture
def appium_driver(context):
    # Configurações do driver
    capabilities = dict(
        platformName='Android',
        automationName='UiAutomator2',
        appPackage='com.android.settings',
        appActivity='.Settings',
    )

    # Cria o driver e atribui ao contexto
    context.driver = webdriver.Remote(
        'http://127.0.0.1:4723',
        options=UiAutomator2Options().load_capabilities(capabilities)
    )

    # logger.info("Driver do Appium inicializado")

    yield context  # Passa o contexto com o driver

    # Finalização (executa após o cenário)
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        # logger.info("Driver do Appium finalizado")


def before_scenario(context, scenario):
    # Garante que o diretório de reports existe
    # os.makedirs('reports', exist_ok=True)
    # os.makedirs('logs', exist_ok=True)

    # Configura o driver para cada cenário
    use_fixture(appium_driver, context)


def after_scenario(context, scenario):
    # Nada a fazer aqui, o quit é feito no yield da fixture
    pass

# def before_all(context):
#    context.driver = Driver.iniciar_driver()
# def after_all(context):
#    Driver.finalizar_driver()