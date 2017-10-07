from No import No

class ListaDuplamenteEncadeada(No):

    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazio(self):
        return self.inicio is None

    def buscar(self, valor):
        if(self.vazio() == True):
            return ("Lista Vazia")
        i = self.inicio
        while(i != None):
            if(valor in i.getConteudo()):
                return i
            i = i.getProximo()
        return ("não Encontrado")

    def inserir(self, valor):
        novoNo = No(valor)
        if(self.vazio() == True):
            self.inicio = novoNo
            self.fim = novoNo
        else:
            novoNo.setProximo(self.inicio)
            self.inicio.setAnterior(novoNo)
            self.inicio = novoNo

    def inserirFim(self, valor):
        novoNo = No(valor)
        if (self.vazio() == True):
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.setProximo(novoNo)
            novoNo.setAnterior(self.fim)
            self.fim = novoNo

    def remover(self, valor):
        x = self.buscar(valor)
        if(x == None):
            return ("não encontrado")
        if(self.inicio != self.fim):
            if(x == self.inicio):
                p = self.inicio.getProximo()
                p.setAnterior(None)
                self.inicio = p
            elif(x == self.fim):
                a = self.fim.getAnterior()
                a.setProximo(None)
                self.fim = a
            else:
                a = x.getAnterior()
                p = x.getProximo()
                p.setAnterior(a)
                a.setProximo(p)
        else:
            self.inicio = None
            self.fim = None

    def mostrar(self):
            s = "Lista:"
            i = self.inicio
            while(i != None):
                s += "\n"+str(i.getConteudo())
                i = i.getProximo()
            return s

    def mostrarInvertido(self):
        s = "Lista:"
        i = self.fim
        while(i != None):
            s += "\n"+str(i.getConteudo())
            i = i.getAnterior()
        return s

    def limpar(self):
        self.inicio = None
        self.fim = None