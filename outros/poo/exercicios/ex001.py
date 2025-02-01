class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

romeu_julieta = Livro('Romeu e Julieta', 'William Shakespeare', 'Não sei')
print(f'Título: {romeu_julieta.titulo}')
print(f'Autor: {romeu_julieta.autor}')
print(f'Ano de publicação: {romeu_julieta.ano_publicacao}')