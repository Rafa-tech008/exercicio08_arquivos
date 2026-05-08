#OP.ARQ_LT01.37
#Declaração de variáveis

import os

def func_escrever (dir01, arq01, buffer_conteudo):
    enc: str = ''
    tipo: str = ''
    arquivo = dir01 + arq01
    if os.path.exists (dir01) and os.path.isdir (dir01):
        tipo = 'w'
        enc = 'utf-8'
        with open (arquivo, tipo, encoding= enc) as file:
            file.write (buffer_conteudo)


def func_fibon (cont):
    a= 0
    b= 1
    buffer: str = ''
    for i in range (1, cont + 1):
        buffer += (str (a) + '\n')
        termos = a + b
        a= b
        b= termos
    return buffer


def main ():
    dir00: str = ''
    arq00: str = ''
    contador: int = 0

    dir00 = '/media/sf_VS_Code/Atividades_python/atividade_08/Arquivos.txt/'
    arq00 = 'exercicio37.txt'
    contador = int (input("Digite um número: "))
    buffer= func_fibon (contador)
    
    func_escrever (dir00, arq00, buffer)

if (__name__ == "__main__"):
    main ()

#Fim