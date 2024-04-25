from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
import requests

class WindowManager(ScreenManager):
    pass

class LoginScreen(Screen):
    pass

class LoginUI(MDFloatLayout):
    def CalculeIMC(self):
        peso = self.ids.Peso.text
        altura = self.ids.Altura.text
        imc = self.ids.IMC.text
        classificacao = self.ids.classificacao.text
        
        req = requests.get(f"https://imc-fastapi.onrender.com/imc/?peso={peso}&altura={altura}")
        imc = round((req.json()['IMC']), 2)
        self.ids.IMC.text =  "IMC: "+ str(imc)
        self.ids.classificacao.text = req.json()['Classificacao']

class IMCApp(MDApp):
    def build(self):
        self.theme_cls.primary_pallete = "Blue"
        self.theme_cls.theme_style = "Dark"
        self.root.current = "login"
        return 

if __name__ == "__main__":
    IMCApp().run()
        