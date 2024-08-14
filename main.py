from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *


GUI = Builder.load_file('main.kv')


class MainApp(App):

    # retorna o GUI (interface visual definida em `main.kv`)
    def build(self):
        return GUI

    def mudar_tela(self, id_tela_destino):
        # self.root é o 'main.kv'  |  ids é um dicionário com as telas seus ids
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela_destino


MainApp().run()
