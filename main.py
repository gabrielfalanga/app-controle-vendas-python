from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class HomePage(Screen):
    pass


class AjustesPage(Screen):
    pass


GUI = Builder.load_file('main.kv')
class MainApp(App):

    def build(self):
        return GUI

    def mudar_tela(self, id_tela_destino):
        # self.root é o 'main.kv'  |  ids é um dicionário com as telas seus ids
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela_destino


MainApp().run()
