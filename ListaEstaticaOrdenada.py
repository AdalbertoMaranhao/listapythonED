class ListaEstatica:

    def __init__(self, tamanho):
        self.lista_nome = []
        self.lista_matricula = []
        self.lista_curso = []
        self.lista_final = []
        self.qtde = 0
        self.tamanho = tamanho

    def inserir(self, nome, matricula, curso):
        if(self.qtde == self.tamanho):
            return ("LISTA CHEIA")
        else:
            self.lista_matricula.append(matricula)
            self.lista_nome.append(nome)
            self.lista_curso.append(curso)
            self.lista_final = list(zip(self.lista_nome, self.lista_matricula, self.lista_curso))
            self.lista_final.sort()
            self.qtde += 1
            print(self.qtde)

    def mostrar(self):
        print(self.lista_final)

    def remover(self, remover_aluno):
        x = 0
        for i in range(len(self.lista_final)):
            x = i
            break
        print(x)
        del (self.lista_final[x])
        self.qtde -= 1

    def buscar(self, elemento):
        pos_i = 0
        pos_j = 0

        for i in range(len(self.lista_final)):
            for j in range(i):
                if elemento in self.lista_final[i][j]:
                    pos_i = i
                    pos_j = j
                    break
                break
        return (pos_i, pos_j)



    def limpar(self):
        self.lista_matricula.clear()
        self.lista_final.clear()
        self.lista_nome.clear()
        self.lista_curso.clear()
        self.qtde = 0