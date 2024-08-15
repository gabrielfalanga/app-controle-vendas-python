from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests


GUI = Builder.load_file('main.kv')


class MainApp(App):

    id_usuario = 2

    # retorna o GUI (interface visual definida em `main.kv`)
    def build(self):
        return GUI

    def on_start(self):
        # link do firebase com id do usuário atual
        link = f'https://app-controle-vendas-812bb-default-rtdb.firebaseio.com/{self.id_usuario}.json'
        # resposta da requisição como dicionário
        requisicao = requests.get(link).json()
        # campo 'avatar' do usuário atual no banco de dados
        avatar = requisicao['avatar']
        # pegando o id da foto de perfil do main.kv
        foto_perfil = self.root.ids['foto_perfil']
        # alterando a foto pelo id
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

    def mudar_tela(self, id_tela_destino):
        # self.root é o 'main.kv'  |  ids é um dicionário com as telas seus ids
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela_destino


MainApp().run()
