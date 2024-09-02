from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from bannervenda import BannerVenda


GUI = Builder.load_file('main.kv')


class MainApp(App):

    id_usuario = 1

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

        # preenchendo lista de vendas
        try:
            vendas = requisicao['vendas'][1:]
            print(vendas)

            for venda in vendas:
                print(venda['cliente'], venda['foto_cliente'])
                banner = BannerVenda(cliente=venda['cliente'], foto_cliente=venda['foto_cliente'],
                                     produto=venda['produto'], foto_produto=venda['foto_produto'],
                                     data=venda['data'], preco=venda['preco'],
                                     unidade=venda['unidade'], quantidade=venda['quantidade'])

                pag_homepage = self.root.ids['homepage']
                lista_vendas = pag_homepage.ids['lista_vendas']
                lista_vendas.add_widget(banner)
        except:
            pass

    def mudar_tela(self, id_tela_destino):
        # self.root é o 'main.kv'  |  ids é um dicionário com as telas e seus ids
        gerenciador_telas = self.root.ids['screen_manager']
        gerenciador_telas.current = id_tela_destino


MainApp().run()
