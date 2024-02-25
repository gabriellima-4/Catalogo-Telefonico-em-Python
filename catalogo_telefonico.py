# Esse catálogo telefônico foi feito utilizando a estrutura de dicionário, que foi pedido à mim por meio de um exercício da universidade.

import os
import time

class CatalogoTelefonico:

    def __init__(self):
        self.catalogo = {}

    def incluir_contato(self):
        self.nome = input("Escreva o nome do contato que deseja adicionar: ")
        self.telefone = input("Digite o telefone do novo contato: ")
        self.catalogo[self.nome] = self.telefone

        print("Contato adicionado ao catálogo.")
    
    def pesquisar_contato(self):
        self.nome = input("Digite o contato que você procura: ")
        
        if self.nome in self.catalogo:
            print(f"O contato que você procura existe no catálogo. O telefone referente à ele é {self.catalogo.get(self.nome)}")
        else:
            raise KeyError("O contato que você procura não existe no catálogo. Portanto, não há um telefone referente à ele.")
        
    def excluir_contato(self):
        self.nome = input("Digite o nome do contato para excluí-lo: ")
        
        if self.nome in self.catalogo:
            del self.catalogo[self.nome]
            print("O contato foi excluído com sucesso.")
        else:
            raise KeyError("Não há como excluir esse contato pois ele não existe.")     

    status_catalogo = lambda self: len(self.catalogo)
    # Mostrar numericamente quantos contatos existem nesse catálogo.

    def imprimir_catalogo(self):
        for nome, telefone in self.catalogo.items():
            print("{} -- {}".format(nome, telefone))


ct = CatalogoTelefonico()

while True:
    print(f"""
    _____________________________
         Catálogo Telefônico
    -----------------------------
    1 - Adicionar contato
    2 - Pesquisar contato
    3 - Excluir contato
    4 - Mostrar todos os contatos
    -----------------------------
    0 - Sair
    -----------------------------

    No momento, esse catálogo possui {ct.status_catalogo()} contatos.

""")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        ct.incluir_contato()
        time.sleep(3)
        os.system("cls")

    if opcao == 2:
        ct.pesquisar_contato()
        time.sleep(5)
        os.system("cls")

    if opcao == 3:
        ct.excluir_contato()
        time.sleep(3)
        os.system("cls")

    if opcao == 4:
        ct.imprimir_catalogo()
        time.sleep(6)
        os.system("cls")

    if opcao == 0:
        break

