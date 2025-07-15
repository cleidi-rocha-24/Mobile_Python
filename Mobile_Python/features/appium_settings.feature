#language: pt
Funcionalidade: Permissao de localizacao do Appium Settings

  Cenário: Permitir acesso a localizacao do Appium Settings
    Dado que eu navego para as permissoes de localizacao do Appium Settings
    Quando seleciono "Permitir o tempo todo"
    Então a permissao de localizacao deve estar marcada como "Permitir o tempo todo"

  Cenário: Negar acesso a localizacao no Appium Settings
    Dado que eu navego para as permissoes de localizacao do Appium Settings
    Quando seleciono "Não permitir"
    Então a permissao de localizacao deve estar marcada como "Não permitir"





