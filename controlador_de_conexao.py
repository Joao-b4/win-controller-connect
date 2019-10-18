#!/bin/python3
# encoding: utf-8
import os
import time
import getpass
import sys

try:
    while True:
        print("o que você deseja fazer ? \n ")#(net stop netprofm) se for win 7
        x = int(input("[1] - desativar conexão \n[2] - ativar conexão \n"))
        if(x == 1):
            time.sleep(3)
            a =  getpass.getpass("insira sua senha: ")
            if(a == "admin"):
                os.system("ipconfig /release")
                time.sleep(3)
                print("conexao desativada\n")
                break
            else:
                print("\nsenha incorreta, tente novamente...\n")
        elif(x == 2):
            time.sleep(3)
            z =  getpass.getpass("insira sua senha: ")
            if(z == "admin"):
                os.system("ipconfig /renew")#(net start netprofm)se for win 7
                time.sleep(2)
                print("conexao ativada\n")
                break
            else:
                print("\nsenha incorreta, tente novamente...\n")
        else:
            print("por favor insira um valor valido...\n #################\n")
except KeyboardInterrupt:
    print("\nfim do programa...")
    time.sleep(3)
    sys.exit()
except Exception as erro:
    print("Erro ocorrido: ",erro)
    time.sleep(3)
