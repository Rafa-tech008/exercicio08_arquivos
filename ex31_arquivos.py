#OP.ARQ_LT01.31
#Declaração de Variáveis

import os

def func_escreve (dir01, arq01, buffer_conteudo):
    tipo: str = ''
    enc: str = ''
    arquivo01: str = ''
    if os.path.exists (dir01) and os.path.isdir (dir01):
        tipo = 'w'
        enc = 'utf-8'
        arquivo01 = dir01 + arq01
        if os.path.exists (arquivo01):
            with open (arquivo01,tipo, encoding=enc) as file:
                file.write (buffer_conteudo)

def func_calc (numero):
    buffer: str = ''
    for i in range (10, 151):
        numero = i ** 2
        buffer += (str(numero) + '\n')
    return buffer


def main():
    num: int = 0
    arq00: str = ''
    dir00: str = ''

    dir00 = '/media/sf_VS_Code/Atividades_python/atividade_05/Arquivos.txt/'
    arq00 = 'exercicio31.txt'

    buffer = func_calc (num)

    func_escreve (dir00, arq00, buffer)

if (__name__ == "__main__"):
    main ()

#Fim