class Cliente:
    def __init__(self,nome, cpf, idade):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf

    def __str__(self):
        return "Nome: " +str(self.nome) + "\nCPF: " + str(self.cpf) + "\nIdade: " + str(self.idade)
