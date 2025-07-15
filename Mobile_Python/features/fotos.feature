#language: pt
Funcionalidade: Permissao de localizacao do Fotos

  Cenário: Permitir acesso a localizacao de Fotos
    Dado que eu navego para as permissoes de localizacao de Fotos
    Quando clico em "Permitir durante o uso do app"
    Então a permissao de localizacao deve estar marcada como "Permitir durante o uso do app"
#
  Cenário: Negar acesso a localizacao de Fotos
    Dado que eu navego para as permissoes de localizacao de Fotos
    Quando clico em "Não permitir"
    Então a permissao de localizacao de fotos deve estar marcada como "Não permitir"

#	•