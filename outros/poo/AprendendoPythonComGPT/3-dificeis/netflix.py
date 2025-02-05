# 1 - Criar uma classe para filmes/séries
#   Cada filme terá título e categoria(ação, comédia, romance, etc)
class Conteudo:
    def __init__(self, titulo, categoria):
        self.titulo = titulo
        self.categoria = categoria

# 2 - Criar uma classe para usuários
#   2.1 - Cadastrar usuários na plataforma.
#       Cada usuário terá um nome e uma lista de conteúdos já assistidos
class Usuario:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.lista_assistidos = []
        self.categorias = []
#   2.2 - Permitir que os usuários assistam conteúdos.
#       Criar um método que adiciona o filme assistido na lista de conteudos ja assistidos
    def assistir(self, conteudo):
        self.lista_assistidos.append(conteudo)
        self.categorias.append(conteudo.categoria)

#   2.3 - Exibir recomendações com base nos conteúdos assistidos
#       Criar um método que verifica as categorias já assistidas pelo usuário e recomenda outros filmes da mesma categoria.
    def recomendar(self, plataforma):
        categorias_assistidas = set()
        for conteudo in self.lista_assistidos:
            categorias_assistidas.update(conteudo.categoria)

        recomendacoes = []
        for conteudo in plataforma.lista_conteudos:
            if conteudo not in self.lista_assistidos and any(cat in categorias_assistidas for cat in conteudo.categoria):
                recomendacoes.append(conteudo.titulo)

        if recomendacoes:
            print(f'Recomendações para {self.nome_usuario}: {", ".join(recomendacoes)}')
        else:
            print(f'Nenhuma recomendação disponível para {self.nome_usuario}.')


# 3 - Criar uma classe para a plataforma
#   3.1 - Atributos:
#       Nome da plataforma
#       lista de filmes disponíveis
#       lista de usuários
class Plataforma:
    def __init__(self, nome_plataforma):
        self.nome_plataforma = nome_plataforma
        self.lista_conteudos = []
        self.lista_usuarios = []
#   3.2 - Método para cadastrar filmes/séries
#       pegará uma variável com a classe de filmes/séries e adicionará à lista de filmes disponíveis
    def cadastrar_conteudo(self, conteudo):
        self.lista_conteudos.append(conteudo)
#   3.3 - Método para cadastrar usuários
#       pegará uma variável com a classe de usuários e adicionará à lista de usuários
    def cadastrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)
#   3.4 - Método para mostrar filmes disponíveis
#       mostrará os itens da lista de filmes disponíveis(o nome e a categoria)
    def listar_conteudos(self):
        for conteudo in self.lista_conteudos:
            print(f'{conteudo.titulo} - {', '.join(conteudo.categoria)}')

streamhub = Plataforma('StreamHub')
joao_silva = Usuario('João Silva')
maria_oliveira = Usuario('Maria Oliveira')

streamhub.cadastrar_usuario(joao_silva)
streamhub.cadastrar_usuario(maria_oliveira)

vingadores = Conteudo('Vingadores: Ultimato', ['Ação', 'Aventura', 'Ficção'])
culpa_das_estrelas = Conteudo('A Culpa é das Estrelas', ['Romance', 'Drama'])
toy_story = Conteudo('Toy Story 4', ['Animação', 'Aventura', 'Comédia'])
jogo_da_imitacao = Conteudo('O Jogo da Imitação', ['Drama', 'Biografia', 'História'
])

streamhub.cadastrar_conteudo(vingadores)
streamhub.cadastrar_conteudo(culpa_das_estrelas)
streamhub.cadastrar_conteudo(toy_story)
streamhub.cadastrar_conteudo(jogo_da_imitacao)

streamhub.listar_conteudos()

joao_silva.assistir(vingadores)

joao_silva.recomendar(streamhub)