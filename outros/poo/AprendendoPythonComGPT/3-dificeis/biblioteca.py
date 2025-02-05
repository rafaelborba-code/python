def linha():
    print('-'*50)


# Criar um sistema de gerenciamento de biblioteca

# cadastrar livros
class Livro:
    def __init__(self, titulo, autor, quantidade_total, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_total = quantidade_total
        self.quantidade_disponivel = quantidade_disponivel

    

# registrar o empréstimo e devolução dos livros pelos membros
class Membro:
    def __init__(self, nome_membro):
        self.nome_membro = nome_membro
        self.livros_emprestados = []

    # quais membros estão com livros emprestados
    def emprestar_livro(self, livro):
        if livro.quantidade_disponivel > 0:
            livro.quantidade_disponivel -= 1
            self.livros_emprestados.append(livro)
            print(f'Livro {livro.titulo} emprestado com sucesso para {self.nome_membro}')
        else:
            print('Livro indisponível.')

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.quantidade_disponivel += 1
            self.livros_emprestados.remove(livro)
            print(f'Livro {livro.titulo} devolvido com sucesso.')
        else:
            print(f'Erro! {self.nome_membro} não pegou o livro {livro.titulo} emprestado.')

# quais livros estão disponíveis
class Biblioteca:
    def __init__(self, nome_biblioteca):
        self.nome_biblioteca = nome_biblioteca
        self.lista_livros_disponiveis = []
        self.lista_membros = []

    def cadastrar_livro(self, livro):
        self.lista_livros_disponiveis.append(livro)
        print(f'Livro \"{livro.titulo}\" cadastrado com sucesso.')

    def cadastrar_membro(self, membro):
        self.lista_membros.append(membro)
        print(f'Membro \"{membro.nome_membro}\" cadastrado com sucesso.')
    
    def listar_livros_disponiveis(self):
        print(f'Livros disponíveis na biblioteca \"{self.nome_biblioteca}\":')
        for livro in self.lista_livros_disponiveis:
            print(f'{livro.titulo} - Autor: {livro.autor} ({livro.quantidade_disponivel} disponíveis)')

beethoven = Biblioteca('Beethoven')
dom_casmurro = Livro('Dom Casmurro', 'Machado de Assis', 1, 1)
romeu_julieta = Livro('Romeu e Julieta', 'Shakespeare', 2, 2)
diario_banana = Livro('Diário de um Banana', 'Jeff Kinney', 4, 4)

beethoven.cadastrar_livro(dom_casmurro)
beethoven.cadastrar_livro(romeu_julieta)
beethoven.cadastrar_livro(diario_banana)
linha()
rafael_borba = Membro('Rafael Borba')
miguel_brito = Membro('Miguel Brito')
pedro_tavares = Membro('Pedro Tavares')

beethoven.cadastrar_membro(rafael_borba)
beethoven.cadastrar_membro(miguel_brito)
beethoven.cadastrar_membro(pedro_tavares)
linha()
beethoven.listar_livros_disponiveis()
linha()
rafael_borba.emprestar_livro(dom_casmurro)
miguel_brito.emprestar_livro(diario_banana)
miguel_brito.emprestar_livro(romeu_julieta)
pedro_tavares.emprestar_livro(diario_banana)
linha()
beethoven.listar_livros_disponiveis()
linha()
rafael_borba.devolver_livro(dom_casmurro)
miguel_brito.devolver_livro(diario_banana)
miguel_brito.devolver_livro(romeu_julieta)
pedro_tavares.devolver_livro(diario_banana)
linha()
beethoven.listar_livros_disponiveis()