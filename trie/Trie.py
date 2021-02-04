from NoTrie import NoTrie


class Trie:

    def __init__(self):
        self.raiz = NoTrie("")

    def inserir(self, palavra):
        no = self.raiz

        for letra in palavra:
            if letra in no.filhos:
                no = no.filhos[letra]
            else:
                novo_no = NoTrie(letra)
                no.filhos[letra] = novo_no
                no = novo_no

        no.palavracompleta = True

        no.contador += 1

    def dfs(self, no, prefixo):
        if no.palavracompleta:
            self.saida.append((prefixo + no.caracter, no.contador))

        for filho in no.filhos.values():
            self.dfs(filho, prefixo + no.caracter)

    def buscar(self, valor):

        self.saida = []
        no = self.raiz
        for letra in valor:
            if letra in no.filhos:
                no = no.filhos[letra]
            else:
                return []

        self.dfs(no, valor[:-1])

        return sorted(self.saida, key=lambda valor: valor[1], reverse=True)
