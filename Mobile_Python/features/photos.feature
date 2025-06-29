#language: pt
Funcionalidade: Permissao de localizacao do Fotos

  Cenário: Permitir acesso a localizacao em Fotos
    Dado que estou no menu de Configuracoes do dispositivo
    Quando eu navego para as permissões de localização do aplicativo Fotos
    E seleciono "Permitir durante o uso do app"
    Então a permissao de localizacao deve estar marcada como "Permitir o tempo todo"

  Cenário: Negar acesso a localizacao em fotos
    Dado que estou no menu de Configuracoes do dispositivo
    Quando eu navego para as permissões de localização do aplicativo Fotos
    E seleciono "Não permitir"
    Então a permissao de localizacao deve estar marcada como "Não permitir"

#	• Apps -> See all apps -> Photos -> Permissions -> Photos and videos -> Allow
#
#	De <https://github.com/users/cleidi-rocha-24/projects/10/views/2?pane=issue&itemId=114135112>
#
#		Id       com.android.permissioncontroller:id/allow_radio_button
#
#		/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RadioButton
#
#		Class android.widget.RadioButton
#
#		Element id 00000000-0000-1a42-ffff-ffff00001f04
#
#	• Apps -> See all apps -> Photos -> Permissions -> Photos and videos -> Dont allow
#		○ ID com.android.permissioncontroller:id/deny_radio_button
#		○ /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RadioButton
#		○ Class android.widget.RadioButton
#Element id 00000000-0000-1a42-ffff-ffff00001f0d


