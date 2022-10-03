
from linkedlist import LinkedList
from queuePas import Queue
from passageiro import Passageiro
import random
from operator import attrgetter


listaPassageiros = LinkedList()
filaOverbooking = Queue()
listaDesistentes = LinkedList()

def gerarPassageiro(qtdPassageiros, statusPass):
    #gera os dados de passageiros
    for x in range(1,(qtdPassageiros + 1)):
        listaNomes = ['Miguel', 'Arthur', 'Theo', 'Heitor', 'Gael', 'Davi', 'Bernardo', 'Gabriel', 'Ravi', 'Noah', 'Samuel', 'Pedro', 'Benicio', 'Benjamin', 'Matheus', 'Isaac', 'Anthony', 'Joaquim', 'Lucas', 'Lorenzo', 'Rafael', 'Nicolas', 'Henrique', 'Murilo', 'Miguel', 'Lucca', 'Guilherme', 'Henry', 'Bryan', 'Gustavo', 'Felipe', 'Pietro', 'Levi', 'Daniel', 'Bento', 'Vicente', 'Leonardo', 'Caleb', 'Pedro', 'Matteo', 'Gabriel', 'Joao', 'Antonio', 'Emanuel', 'Enzo', 'Davi', 'Caio', 'Eduardo', 'Lucas']
        listaSobrenomes = ['Silva', 'Santos', 'das Dores', 'Pinto', 'Coelho', 'Oliveira', 'Souza', 'Alves', 'Lima', 'Pereira', 'Burgarelli', 'de Jesus', 'dos Reis', 'Gomes', 'Costa', 'Martins', 'Ribeiro', 'Almeida', 'Carvalho', 'Lopes', 'Fernandes']
        listaRuas = ['Rua 10 de Abril', 'Rua Adelina Dossi Becevelli', 'Avenida Adolfo Correia da Silva', 'Travessa Advalter Braganca', 'Rua Afonso Claudio', 'Rua Alexandre Vargas', 'Beco Alexandrino Coelho Araujo', 'Rua Alfredo Pereira de Chagas', 'Rua Alice Laranja', 'Rua Alice Nunes Kull', 'Rua Algas Marinhas', 'Avenida Esperanca', 'Rua Ana Pestana']
        listaCidades = ['Colatina', 'Vitoria', 'Vilha-Velha', 'Linhares', 'Serra', 'Guarapari', 'Afonso Pena']
        nomeCompleto = listaNomes[random.randint(0, (len(listaNomes) - 1))] + " " + listaSobrenomes[random.randint(0, (len(listaSobrenomes) - 1))]
        cpf = str(random.randint(10000000000, 11000000000))
        rg = str(random.randint(1000000, 1100000))
        celular = str(random.randint(990000000, 999999999))
        telefone = str(random.randint(10000000, 20000000))
        numero = str(random.randrange(1,3000))
        endereco = ''.join(listaRuas[random.randint(0, (len(listaRuas) - 1))]) + ", " + numero + ", " + ''.join(listaCidades[random.randint(0, (len(listaCidades) - 1))]) + ", ES"
        assento = str(x)
        #Cria passageiro na fila de overbooking
        if statusPass == "Overbooking":
            passageiro = Passageiro(''.join(nomeCompleto), cpf, rg, endereco, celular, telefone)
            filaOverbooking.push(passageiro)
        #Cria passageiro na lista de passageiros
        elif (statusPass == "Confirmado" or statusPass == "Confirmado da fila"):
            passageiro = Passageiro(''.join(nomeCompleto), cpf, rg, endereco, celular, telefone, statusPass, assento)
            listaPassageiros.addNode(passageiro)
listaTemp = []
listaSemOrdem = []
assentosVagos = []
    
    
#Criando passageiros na lista de passageiros
gerarPassageiro(30, "Confirmado")
print("\nLISTA DE PASSAGEIROS:\n")
print(listaPassageiros)

#Criando passageiros na fila de passageiros
gerarPassageiro(10, "Overbooking")
print("\nFILA DO OVERBOOKING:\n")
print(filaOverbooking)

for i in range(5):
    #Escolhendo desistentes
    listaPassageiros.posNode(random.randint(1,30))
    #alterando status para desistente
    listaPassageiros.listIterator.data.statusVoo = "Desistente"
    #adicionando na lista de desistente temporária
    listaTemp.append(listaPassageiros.listIterator.data)
    #removendo da lista de passageiros
    listaPassageiros.elimNode()
#colocando em ordem alfabetica na lista temporária
listaTemp.sort(key = attrgetter('nomeCompleto'))

#atribuindo os assentos dos desistentes para seren utilizados pelos novos passageiros
for i in listaTemp:
    assentosVagos.append(i.assento)
#adicionando na lista de desistentes em ordem alfabetica
for i in range(5):
    listaDesistentes.addNode(listaTemp[i])

print("\nLISTA DE DESISTENTES:\n")
print(listaDesistentes)

#adicionando da lista de passageiros finais os passageiros da fila overbooking
for i in range(5):
    novoPas = filaOverbooking.first
    novoPas.data.assento = assentosVagos[i]
    novoPas.data.statusVoo = "Confirmado da fila"
    listaPassageiros.addNode(novoPas.data)
    filaOverbooking.pop()

print("\nLISTA DE PASSAGEIROS FINAL:\n")
print(listaPassageiros)
