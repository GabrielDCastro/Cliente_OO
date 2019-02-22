from cliente import Cliente
listacliente= []

def exibirMenu():
    print("1 - Inserir Pessoa")
    print("2 - Excluir Pessoa")
    print("3 - Listar")
    print("4 - Sair")
    opcao = int(input("Escolha uma opcao: "))
    return opcao

def inserir():
    nome=(str(input("Digite um nome: ")))
    idade=int(input("Digite a idade: "))
    cpf=int(input("Digite o CPF: "))
    cliente= Cliente(nome, cpf, idade)
    listacliente.append(cliente)

def listar():
    for elemento in listacliente:
        print('\033[34m{}\033[m'.format(elemento))

def excluir():
    nomes = input("Nome da pessoa que deseja excluir:")
    indice = -1
    encontrou = False
    for elemento in listacliente:
        indice += 1
        if elemento == nomes:
            encontrou = True
            break
    if (encontrou):
        del listacliente[indice]

while True:
    opcao = exibirMenu()
    if opcao == 4:
        break
    elif opcao == 3:
        listar()
    elif opcao == 1:
        inserir()
    elif opcao == 2:
        excluir()
