from behave import given, when, then
from Mobile_Python.features.pages.appium_settings_pages import AppiumSettings


@given(u'que eu navego para as permissoes de localizacao do Appium Settings')
def step_impl(context):
    context.configuracoes = AppiumSettings(context.driver)
    context.configuracoes.localizar_appium_settings()
    context.configuracoes.clicar_retorno_busca_appium_settings()
    context.configuracoes.acessar_permissoes()
    context.configuracoes.acessar_localizacao()

@when(u'seleciono "Permitir o tempo todo"')
def step_impl(context):
    context.configuracoes.permitir_sempre()


@then(u'a permissao de localizacao deve estar marcada como "Permitir o tempo todo"')
def step_impl(context):
    context.configuracoes.validar_check_permitir_sempre()

@when(u'seleciono "Não permitir"')
def step_impl(context):
    context.configuracoes.permitir_nunca()

@then(u'a permissao de localizacao deve estar marcada como "Não permitir"')
def step_impl(context):
    context.configuracoes.validar_check_permitir_nunca()
