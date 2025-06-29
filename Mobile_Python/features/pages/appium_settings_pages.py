import time

from Mobile_Python.features.pages.base_page import BasePage


# INICIO =
# //android.view.View[@content-desc="Início"]

class AppiumSettings(BasePage):
    BOTAO_CONFIGURACAO = "//android.widget.TextView[@content-desc='Configurar']"
    CAMPO_PESQUISA = "//android.widget.AutoCompleteTextView[@text='Pesquisar']"
    LUPA_PESQUISA = "com.android.settings:id/search_action_bar_title"
    APPIUM_SETTINGS = "//android.widget.TextView[@text='Appium Settings']"
    # APPs = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
    #         ".widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout"
    #         "/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView"
    #         "/android.widget.LinearLayout[6]/android.widget.RelativeLayout"
    # VER_TODOS_APPS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
    #                   "/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android"
    #                   ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx"
    #                   ".recyclerview.widget.RecyclerView/android.widget.LinearLayout["
    #                   "4]/android.widget.LinearLayout/android.widget.ImageView"
    # APPIUM_SETTINGS = "//android.widget.TextView[@content-desc='Appium Settings']"
    PERMISSOES_APPIUM = "//android.widget.TextView[@text='Permissões']"
    # LOCALIZACAO_APPIUM = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
    #                       ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView"
    #                       "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout["
    #                       "2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
    #                       "/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout["
    #                       "11]/android.widget.RelativeLayout/android.widget.TextView"
    PERMITIR_SEMPRE_APPIUM = "com.android.permissioncontroller:id/allow_always_radio_button"
    PERMITIR_NUNCA_APPIUM = "com.android.permissioncontroller:id/deny_radio_button"

    def __init__(self, driver):
        super().__init__(driver)

    def abrir_configuracao(self):
        # self.espera("XPATH", self.BOTAO_CONFIGURACAO)
        # self.click("XPATH", self.BOTAO_CONFIGURACAO)
        print("entrou medodo de abrir config")
        # self.click("ID", self.LUPA_PESQUISA)
        # self.send_keys("ID", self.CAMPO_PESQUISA, "Appium Settings")

    def encontrar_apps(self):
        self.click("ID", self.LUPA_PESQUISA)
        # self.click("xpath", self.CAMPO_PESQUISA)
        self.send_keys("XPATH", self.CAMPO_PESQUISA, "appium sett")
        time.sleep(6)

    # def selecionar_ver_todos(self):
    #     self.click("xpath", self.BOTAO_CONFIGURACAO)

    def clicar_retorno_busca_appium_settings(self):
        # time.sleep(6)
        self.espera("xpath", self.APPIUM_SETTINGS)
        self.click("xpath", self.APPIUM_SETTINGS)
        self.click("xpath", self.APPIUM_SETTINGS)

    def acessar_permissoes(self):
        self.espera("xpath", self.PERMISSOES_APPIUM)
        self.click("xpath", self.PERMISSOES_APPIUM)

    # def marcar_opcao_desabilitar(self, texto):
    #     if texto == "Don't allow":
    #         locator = (AppiumBy.XPATH,
    #                    '//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/deny_radio_button"]')
    #     else:
    #         locator = (
    #             AppiumBy.XPATH,
    #             f'//*[contains(@text, "{texto}")]'
    #         )
    #     self._marcar_opcao_desabilitar(locator)
    #     time.sleep(2)
    #
    # def marcar_opcao_habilitar(self, texto):
    #     if texto == "Allow all the time":
    #         locator = (AppiumBy.XPATH,
    #                    '//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/deny_radio_button"]')
    #     else:
    #         locator = (
    #             AppiumBy.XPATH,
    #             f'//*[contains(@text, "{texto}")]'
    #         )
    #     self._marcar_opcao_habilitar(locator)
