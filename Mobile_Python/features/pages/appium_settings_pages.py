import time

from Mobile_Python.features.pages.base_page import BasePage


# INICIO =
# //android.view.View[@content-desc="Início"]

class AppiumSettings(BasePage):
    BOTAO_CONFIGURACAO = "//android.widget.TextView[@content-desc='Configurar']"
    CAMPO_PESQUISA = "//android.widget.AutoCompleteTextView[@text='Pesquisar']"
    LUPA_PESQUISA = "com.android.settings:id/search_action_bar_title"
    APPIUM_SETTINGS = "//android.widget.TextView[@text='Appium Settings']"
    PERMISSOES_APPIUM = "//android.widget.TextView[@text='Permissões']"
    LOCALIZACAO_APPIUM = "//android.widget.TextView[@text='Localização']"
    PERMITIR_SEMPRE_APPIUM = "com.android.permissioncontroller:id/allow_always_radio_button"
    PERMITIR_NUNCA_APPIUM = "com.android.permissioncontroller:id/deny_radio_button"

    def __init__(self, driver):
        super().__init__(driver)

    def localizar_appium_settings(self):
        self.espera("ID", self.LUPA_PESQUISA)
        self.clicar("ID", self.LUPA_PESQUISA)
        self.digitando_devagar("XPATH", self.CAMPO_PESQUISA, "sett")
        time.sleep(8)

    def clicar_retorno_busca_appium_settings(self):
        # time.sleep(6)
        self.espera("xpath", self.APPIUM_SETTINGS)
        self.clicar("xpath", self.APPIUM_SETTINGS)

    def acessar_permissoes(self):
        self.espera("xpath", self.PERMISSOES_APPIUM)
        self.clicar("xpath", self.PERMISSOES_APPIUM)

    def acessar_localizacao(self):
        self.espera("xpath", self.LOCALIZACAO_APPIUM)
        self.clicar("xpath", self.LOCALIZACAO_APPIUM)

    def permitir_sempre(self):
        self.espera("ID", self.PERMITIR_SEMPRE_APPIUM)
        self.clicar("ID", self.PERMITIR_SEMPRE_APPIUM)

    def validar_check_permitir_sempre(self):
        self.espera("ID", self.PERMITIR_SEMPRE_APPIUM)
        self.clicar("ID", self.PERMITIR_SEMPRE_APPIUM)
        radio_permitir_sempre = self.procura_elemento("ID", self.PERMITIR_SEMPRE_APPIUM)
        assert radio_permitir_sempre.get_attribute("checked") == 'true', ("O radio button 'Permitir sempre' não está "
                                                                          "selecionado")

    def permitir_nunca(self):
        self.espera("ID", self.PERMITIR_NUNCA_APPIUM)
        self.clicar("ID", self.PERMITIR_NUNCA_APPIUM)

    def validar_check_permitir_nunca(self):
        self.espera("ID", self.PERMITIR_NUNCA_APPIUM)
        self.clicar("ID", self.PERMITIR_NUNCA_APPIUM)
        radio_permitir_nunca = self.procura_elemento("ID", self.PERMITIR_NUNCA_APPIUM)
        assert radio_permitir_nunca.get_attribute("checked") == 'true', ("O radio button 'Permitir nunca' não está "
                                                                         "selecionado")
