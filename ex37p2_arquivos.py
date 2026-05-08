#OP.ARQ_LT01.37
#Declaração de variáveis

import os

def ler_conteudo (dir01, arq01):
    valor: int= 0
    arquivo: str = ''
    arquivo = dir01 + arq01
    if (os.path.exists (dir01) and os.path.isdir (dir01)):
        with open (arquivo) as file:
            for linha in file:
                valor= int(linha)
                resultado= verif_cont (valor)
                if (resultado != -1 ):
                    print (f"O valor de {resultado} é impar")


def verif_cont (value):
    if (value % 2 != 0):
        return value
    else:
        return -1

def main ():
    dir00: str = ''
    arq00: str = ''

    dir00 = '/media/sf_VS_Code/Atividades_python/atividade_08/Arquivos.txt/'
    arq00 = 'exercicio37.txt'

    ler_conteudo (dir00, arq00)

if (__name__ == "__main__"):
    main ()

#Fim