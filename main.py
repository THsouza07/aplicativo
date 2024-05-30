from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.banner.banner import MDFlatButton
class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class TelaPrincipal(MDScreen):
    pass

class Denuncia(MDScreen):
    pass

class Perfil(MDScreen):
    pass

class App(MDApp, App):
    dialog = None
    def build(self):
        Window.size = (300, 600)
        Builder.load_file(('main.kv'))
        sm = MDScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(TelaPrincipal())
        sm.add_widget(Denuncia())
        sm.add_widget(Perfil())
        return sm

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Sua denúncia foi feita com sucesso!",
                
                buttons=[
                    MDFlatButton(
                        text = "Ok",
                        theme_text_color = "Custom",
                        text_color = '#0081F8',
                        on_release = lambda *args: self.denuncia_and_dismiss()
                    ),
                ],
            )
        self.dialog.open()
    
    def denuncia_and_dismiss(self):
        self.dialog.dismiss() 
        self.denuncia() 

    def denuncia(self):
        self.root.current = 'tela_principal'

App().run()