
__author__="Deivid k.l"
import os
import sys
import glob
tipo=glob.glob('*.c')
def listando():
    for lista in tipo:
        print(lista)
def clang():
    print('###############')
    print("assistente do compilador clang")
    print("""
comandos:
compilar
renomear
executar
""")
    opc=sys.argv[1]
    if opc=='compilar':
        try:
            os.system('clang -v '+arq)
        except UnboundLocalError:
            print('compilar qual arquivo?')
            listando()
            arq=input('arquivo:')
            os.system('clang -v '+arq)
    if opc=='renomear':
        try:
            os.system('mv '+arq,nome)
        except UnboundLocalError:
            print('renomear qual arquivo?')
            os.system('ls')
            arq=input('arquivo:')
            nome=input('novo nome:')
            os.system('mv '+arq,nome)
    if opc=='executar':
        try:
            os.system('./'+arq)
        except UnboundLocalError:
            print("executar qual arquivo?")
            os.system('ls')
            arq=input('arquivo:')
            os.system('./'+arq)
if __name__=='__main__':
    clang()
