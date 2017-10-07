class No:

    def __init__(self, conteudo):
        self.proximo = None
        self.conteudo = conteudo
        self.anterior = None

    def getConteudo(self):
        return self.conteudo
    def setConteudo(self, novo):
        self.conteudo = novo
    def getProximo(self):
        return self.proximo
    def setProximo(self, novo):
        self.proximo = novo
    def getAnterior(self):
        return self.anterior
    def setAnterior(self, novo):
        self.anterior = novo

    def __str__(self):
        return str(self.conteudo)

