def escreva(texto):
    print('~'*(len(texto)+8))
    print(f'{texto:^{len(texto)+8}}')
    print('~'*(len(texto)+8))


escreva('Curso em Vídeo Python')
escreva('CeV')
escreva('Rafael Borba')