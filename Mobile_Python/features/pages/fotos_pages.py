import time
from features.pages.base_page import BasePage


class Fotos(BasePage):
    BOTAO_CONFIGURACAO = "//android.widget.TextView[@content-desc='Configurar']"
    CAMPO_PESQUISA = "//android.widget.AutoCompleteTextView[@text='Pesquisar']"
    LUPA_PESQUISA = "com.android.settings:id/search_action_bar_title"
    FOTOS = "(//android.widget.TextView[@text='Fotos'])[2]"
    PERMISSOES_FOTOS = "//android.widget.TextView[@text='Permissões']"
    LOCALIZACAO_FOTOS = "//android.widget.TextView[@text='Localização']"
    PERMITIR_SEMPRE_FOTOS = "com.android.permissioncontroller:id/allow_foreground_only_radio_button"
    PERMITIR_NUNCA_FOTOS = "com.android.permissioncontroller:id/deny_radio_button"

    def __init__(self, driver):
        super().__init__(driver)

    def localizar_fotos(self):
        self.espera("ID", self.LUPA_PESQUISA)
        self.clicar("ID", self.LUPA_PESQUISA)
        self.digitando_devagar("XPATH", self.CAMPO_PESQUISA, "Fotos")
        time.sleep(2)

    def clicar_retorno_busca_fotos(self):
        # time.sleep(6)
        self.espera("xpath", self.FOTOS)
        self.clicar("xpath", self.FOTOS)

    def acessar_permissoes_fotos(self):
        self.espera("xpath", self.PERMISSOES_FOTOS)
        self.clicar("xpath", self.PERMISSOES_FOTOS)

    def acessar_localizacao_fotos(self):
        self.espera("xpath", self.LOCALIZACAO_FOTOS)
        self.clicar("xpath", self.LOCALIZACAO_FOTOS)

    def permitir_sempre_fotos(self):
        self.espera("ID", self.PERMITIR_SEMPRE_FOTOS)
        self.clicar("ID", self.PERMITIR_SEMPRE_FOTOS)

    def validar_check_permitir_sempre_fotos(self):
        self.espera("ID", self.PERMITIR_SEMPRE_FOTOS)
        self.clicar("ID", self.PERMITIR_SEMPRE_FOTOS)
        radio_permitir_sempre = self.procura_elemento("ID", self.PERMITIR_SEMPRE_FOTOS)
        assert radio_permitir_sempre.get_attribute("checked") == 'true', ("O radio button 'Permitir durante o uso do app' não está "
                                                                          "selecionado")

    def permitir_nunca_fotos(self):
        self.espera("ID", self.PERMITIR_NUNCA_FOTOS)
        self.clicar("ID", self.PERMITIR_NUNCA_FOTOS)

    def validar_check_permitir_nunca_fotos(self):
        self.espera("ID", self.PERMITIR_NUNCA_FOTOS)
        self.clicar("ID", self.PERMITIR_NUNCA_FOTOS)
        radio_permitir_nunca = self.procura_elemento("ID", self.PERMITIR_NUNCA_FOTOS)
        assert radio_permitir_nunca.get_attribute("checked") == 'true', ("O radio button 'Permitir nunca' não está "
                                                                         "selecionado")