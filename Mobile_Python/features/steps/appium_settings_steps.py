from behave import given, when, then

from Mobile_Python.features.pages.appium_settings_pages import AppiumSettings
from Mobile_Python.features.pages.base_page import BasePage


@given(u'que estou no menu de Configuracoes do dispositivo')
def step_impl(context):
    context.configuracoes = AppiumSettings(context.driver)
    print("primeiro = passou pelo step de abrir config")
    context.configuracoes.abrir_configuracao()
    print("passou pelo ultimo step de abrir config")


@when(u'eu navego para as permissoes de localizacao do Appium Settings')
def step_impl(context):
    context.configuracoes.encontrar_apps()
    print("passou pelo step de abrir config")
    context.configuracoes.clicar_retorno_busca_appium_settings()
    context.configuracoes.acessar_permissoes()


@when(u'seleciono "Permitir o tempo todo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When seleciono "Permitir o tempo todo"')
    pass


@then(u'a permissao de localizacao deve estar marcada como "Permitir o tempo todo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a permissao de localizacao deve estar marcada como "Permitir o tempo todo"')


@when(u'seleciono "Não permitir"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When seleciono "Não permitir"')


@then(u'a permissao de localizacao deve estar marcada como "Não permitir"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a permissao de localizacao deve estar marcada como "Não permitir"')
