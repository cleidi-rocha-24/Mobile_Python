from behave import given, when, then

from Mobile_Python.features.pages.fotos_pages import Fotos


@given(u'que eu navego para as permissoes de localizacao de Fotos')
def step_impl(context):
    context.foto = Fotos(context.driver)
    context.foto.localizar_fotos()
    context.foto.clicar_retorno_busca_fotos()
    context.foto.acessar_permissoes_fotos()
    context.foto.acessar_localizacao_fotos()

@when(u'clico em "Permitir durante o uso do app"')
def step_impl(context):
    context.foto.permitir_sempre_fotos()


@then(u'a permissao de localizacao deve estar marcada como "Permitir durante o uso do app"')
def step_impl(context):
    context.foto.validar_check_permitir_sempre_fotos()

@when(u'clico em "Não permitir"')
def step_impl(context):
    context.foto.permitir_nunca_fotos()

@then(u'a permissao de localizacao de fotos deve estar marcada como "Não permitir"')
def step_impl(context):
    context.foto.validar_check_permitir_nunca_fotos()
