class Aluno:
    def __init__(self):
        self.__nota = None
    
    def definir_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
            print(f'Nota {nota} definida com sucesso.')
        else:
            print('ERRO! Nota inválida.')
    
    def mostrar_nota(self):
        if self.__nota != None:
            return f'Nota: {self.__nota}'
        else:
            return 'Nota não encontrada.'

aluno = Aluno()

aluno.definir_nota(9.5)
print(aluno.mostrar_nota())