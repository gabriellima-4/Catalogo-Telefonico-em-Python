# Esse catálogo telefônico foi feito utilizando a estrutura de dicionário, que foi pedido à mim por meio de um exercício da universidade.

# O código ainda não está do jeitinho que eu quero, irei mudar algumas coisas.


class CatalogoTelefonico:

    def __init__(self):
        self.catalogo = {}

    def incluir_contato(self, nome, telefone):
        self.catalogo[nome] = telefone
        print("Contato adicionado ao catálogo.")
    
    def pesquisar_contato(self, nome):
        if nome in self.catalogo:
            print(f"O contato que você procura existe no catálogo. O telefone referente à ele é {self.catalogo.get(nome)}")
        else:
            raise KeyError("O contato que você procura não existe no catálogo. Portanto, não há um telefone referente à ele.")
        
    def excluir_contato(self, nome):
        del self.catalogo[nome]
        print("O contato foi excluído com sucesso.")
    
    def imprimir_catalogo(self):
        return print(self.catalogo)


ct = CatalogoTelefonico()

contato1 = ct.incluir_contato("Pedro", "98432-0103")
contato2 = ct.incluir_contato("Livian", "91103-7327")
contato3 = ct.incluir_contato("Ana", "90230-4439")
contato4 = ct.incluir_contato("Madalena", "92851-7725")

pesquisa = ct.pesquisar_contato("Ana")

exc = ct.excluir_contato("Livian")

imp = ct.imprimir_catalogo()
