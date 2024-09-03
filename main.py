from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from bannervenda import BannerVenda
import os
from functools import partial

GUI = Builder.load_file('main.kv')


class MainApp(App):

    id_usuario = 1

    # retorna o GUI (interface visual definida em `main.kv`)
    def build(self):
        return GUI

    def on_start(self):
        # carregar as fotos de perfil
        arquivos = os.listdir('icones/fotos_perfil')
        pag_fotoperfil = self.root.ids['fotoperfilpage']
        lista_fotos = pag_fotoperfil.ids['lista_fotos_perfil']
        for foto in arquivos:
            imagem = ImageButton(source=f'icones/fotos_perfil/{foto}', on_release=partial(self.mudar_foto_perfil, foto))
            lista_fotos.add_widget(imagem)

        # carrega as informações do usuário
        self.carregar_info_usuario()

    def carregar_info_usuario(self):
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

        # preencher lista de vendas
        try:
            vendas = requisicao['vendas'][1:]
            pag_homepage = self.root.ids['homepage']
            lista_vendas = pag_homepage.ids['lista_vendas']

            for venda in vendas:
                banner = BannerVenda(cliente=venda['cliente'], foto_cliente=venda['foto_cliente'],
                                     produto=venda['produto'], foto_produto=venda['foto_produto'],
                                     data=venda['data'], preco=venda['preco'],
                                     unidade=venda['unidade'], quantidade=venda['quantidade'])

                lista_vendas.add_widget(banner)
        except:
            pass

    def mudar_tela(self, id_tela_destino):
        # self.root é o 'main.kv'  |  ids é um dicionário com as telas e seus ids
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela_destino

    def mudar_foto_perfil(self, foto, *args):
        # pegando o id da foto de perfil do main.kv
        foto_perfil = self.root.ids['foto_perfil']
        # alterando a foto pelo id
        foto_perfil.source = f"icones/fotos_perfil/{foto}"

        # firebase aceita só um dicionário em forma de string com as chaves e os valores entre aspas duplas
        info = f'{{"avatar": "{foto}"}}'
        # enviando a alteração com patch
        requests.patch(f'https://app-controle-vendas-812bb-default-rtdb.firebaseio.com/{self.id_usuario}.json',
                                    data=info)


MainApp().run()
