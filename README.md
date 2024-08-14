# Visão geral do aplicativo

## Primeira tela - Login / Criar Conta
- Fundo com cor ou imagem
- Logo da empresa
- Título com várias cores
- Formulário de Login
- Texto com mensagem para o usuário
- Criar Conta (botões estilizados)
  - Autentica e cria um usuário no BD
  - Firebase do Google
- Login
  - Valida o Login do usuário
  - Carrega as informações do usuário
  - Mantém o usuário com Login feito

## Tela inicial
- Foto de perfil do usuário
- Total de vendas em banner atualizado
- Lista Scrollable com vendas
  - Foto do cliente
  - Foto do produto
  - Data da venda
  - Preço
  - Unidades
- Botão de adicionar nova venda
- Botão para ver outros vendedores
- Botão ajustes

## Tela adicionar venda
- Foto de perfil do usuário
- Lista Scrollable para o lado com Clientes
- Lista Scrollable para o lado com Produtos
- Data preenchida automaticamente
- Unidade de venda
  - Obs.: Qualquer seleção destaca o item selecionado
- Preço total (campo a ser preenchido)
- Quantidade total (campo a ser preenchido)
- Botão de Cancelar venda
- Botão de Adicionar venda
  - Valida se a venda está toda preenchida
  - Adiciona a venda ao banco de dados
  - Atualiza o aplicativo

## Tela vendedores
- Foto de perfil do usuário
- Lista Scrollable com os vendedores
  - Foto do vendedor
  - ID do vendedor
  - Total de vendas
  - Quando um item é clicado, abre as vendas do vendedor (próxima tela)
- Botão de voltar

## Tela vendedor selecionado
- Foto de perfil do usuário alterada para o vendedor atual
- Resto da tela como a página inicial (vendas do vendedor selecionado)

## Tela ajustes
- Foto de perfil do usuário
- ID do usuário em banner
- Imagem/Botão de mudar foto de perfil
- Imagem/Botão de acompanhar vendedor
- Imagem/Botão de ver todas as vendas da empresa
- Botão de voltar

## Tela mudar foto de perfil
- Foto de perfil do usuário
- Texto para selecionar uma foto de perfil
- Fotos em Lista Scrollable, com 3 por linha
  - Quando clicar na foto, altera a foto de perfil (no app e no banco de dados)
- Botão de voltar

## Tela acompanhar/adicionar vendedor
- Foto de perfil do usuário
- Texto estilizado para inserir o ID de outro vendedor
- Formulário para inserir o ID de outro vendedor
- Botão adicionar vendedor
  - Valida se o ID existe
  - Verifica se já está na lista
  - Adiciona o vendedor
- Texto de mensagem para o usuário abaixo do formulário
- Botão de voltar

## Tela todas vendas da empresa
- Igual a página de vendas de um vendedor, mas
  - com todas as vendas da empresa
  - valor total atualizado