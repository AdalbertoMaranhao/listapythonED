from ListaEstaticaOrdenada import ListaEstatica
lista = ListaEstatica(3)
continua = True
while(continua):


    msg =input("Informe o numero da operação:\n"
				"1 - Inserir um Aluno na lista\n"
				"2 - Remover um Aluno da lista\n"
				"3 - Buscar um Aluno\n"
				"4 - Mostra lista de Alunos\n"
				"5 - Limpar a lista\n"
				"6 - Sair\n")
    op = int(msg)
    if(op == 1):
        if(lista.qtde != lista.tamanho):
            lista.inserir(input("Digite a Matricula do Aluno:"), input("Digite o Nome do Aluno:"), input("Digite o Curso do Aluno:"),)
        else:
            print ("Lista Cheia")
    elif(op == 2):
        aluno = str(input("Digite a Matricula do Aluno:"))
        lista.remover(aluno)
    elif(op == 3):
        aluno = str(input("Digite a Matricula do Aluno:"))
        aluno = lista.buscar(aluno)
        if(aluno != None):
            matricula = lista.lista_final[aluno[0]][aluno[1]]
            nome = lista.lista_final[aluno[0]][aluno[1]+1]
            curso = lista.lista_final[aluno[0]][aluno[1]+2]
            print("Aluno Encontrado: Matricula:{} Nome:{} Curso:{}".format(matricula, nome, curso))
        else:
            print("Aluno não Encontrado")
    elif(op == 4):
        print(lista.mostrar())
    elif(op == 5):
        lista.limpar()
    elif(op == 6):
        continua = False
    else:
        print("Opção Invalida")


