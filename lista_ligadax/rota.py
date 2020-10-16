from listas_ligadas import ListaLigada


class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self.nome, self.endereco)


def main():
    loja1 = Loja("Mercadinho", "Rua das Laranjeira, 12")
    loja2 = Loja("Hortifruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")
    loja4 = Loja("Supermercado", "Alameda Santos, 400")
    loja5 = Loja("Mini mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")


    lista = ListaLigada()

    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)

    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover_do_inicio()
    print("Removido: {}".format(removido))

    removido = lista.remover_do_inicio()
    print("Removido: {}".format(removido))

    print("")
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover(2)
    print("")
    print("Removido da posição 2: {}".format(removido))

    print("")
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover(2)
    print("")
    print("Removido da ultima posição: {}".format(removido))

    print("")
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover(0)
    print("")
    print("Removido da posição 0: {}".format(removido))

    print("")
    print(lista.quantidade)
    lista.imprimir()

    print("Item 0:")
    print(lista.item(0))

main()
