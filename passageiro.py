
class Passageiro:
    
    def __init__(self, nomeCompleto, cpf, rg, endereco, telCelular, telFixo, statusVoo="Overbooking", assento="-"):
        #construtor da classe
        self.nomeCompleto = nomeCompleto
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.telCelular = telCelular
        self.telFixo = telFixo
        self.statusVoo = statusVoo
        self.assento = assento

    def __repr__(self):
        #configura o print do desenvolvedor
        data = ' '
        data = "Nome: " + self.nomeCompleto + '\n'
        data = data + "cpf: " + self.cpf + '\n'
        data = data + "rg: " + self.rg + '\n'
        data = data + "endereco: " + self.endereco + '\n'
        data = data + "Celular: " + self.telCelular + '\n'
        data = data + "Telefone: " + self.telFixo + '\n'
        data = data + "Status do Voo: " + self.statusVoo + '\n'
        data = data + "Assento: " + self.assento + '\n'
        data = data + "--------------------------------------\n"
        
        return data
    
    def __str__(self):
        #configura o print do usuario
        data = ' '
        data = "Nome: " + self.nomeCompleto + '\n'
        data = data + "cpf: " + self.cpf + '\n'
        data = data + "rg: " + self.rg + '\n'
        data = data + "endereco: " + self.endereco + '\n'
        data = data + "Celular: " + self.telCelular + '\n'
        data = data + "Telefone: " + self.telFixo + '\n'
        data = data + "Status do Voo: " + self.statusVoo + '\n'
        data = data + "Assento: " + self.assento + '\n'
        data = data + "--------------------------------------\n"
        return data