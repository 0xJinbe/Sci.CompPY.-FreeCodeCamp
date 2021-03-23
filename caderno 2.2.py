#inicio estudo de classes (modelagem)

class carro(): #qndo se cria classe coloca letra maiuscula

    def __init__(self):
        print('Eu sou um carro')

print(carro()) #call de classe como em função

#atributos sao caracteristicas de um objeto (variaveis da programação estruturada) #carro atrib: carro, modelo, ano, cor
#metodos sao comportamento ou açaõ dos obj de uma classe (funções ou procedimentos da prog estruturada) #met carro: ligarfarol(),acelerar()

class Carro():
    def __init__(self, marca, modelo, ano, cor, statusFarol = 'desligado'): #atributos
        self.marca = marca   #self liga o atributo a classe
        self.modelo = modelo
        self.ano_de_fabricação = ano
        self.cor = cor

        self.statusFarol = statusFarol
        self.velocimetro = 0
        self.__status = False #encapsulamento que fica oculto ao usuário (2 underline + atributo) True para ligado

    def ligarFarol(self):  #metodo ligar farol
        if(self.statusFarol == 'desligado'):
            self.statusFarol = 'ligado'
            print('Farol ligado')
        else:
            print('O farol já está ligado')

    def desligarFarol(self): #método desligar farol
        if(self.statusFarol == 'ligado'):
            self.statusFarol = 'desligado'
            print('Farol desligado')

    def acelerar(self, acresVelocidade): #método
        self.velocimetro = self.velocimetro + acresVelocidade

    def frear(self, decresVelocidade = 5):
        if (self.velocimetro > decresVelocidade):
            self.velocimetro = self.velocimetro - decresVelocidade

    def getStatus(self):#pega e retornar o valor da variavel __status
        return self.__status #o self referencia a classe e permite o acesso.

    def setStatus(self, novo_status, chave):

        chave_certa = self.__verifica_chave(chave)

        if chave_certa:
            self.__status = novo_status
        else:
            print('O status não pode ser alterado')

    def __verifica_chave(self, chave): #identificação da chave fica como metodo privado
        if chave == 123456:
            return  True
        else:
            return False




#instancia e objetos sao sinonimos. Reais e dinamicos. Mesmos atributos com valores diferentes.
#instanciando objetos
#carros iguais podem ter propriedades diferentes
gol = Carro('Wolks', 'gol', 2010, 'azul')
fusca = Carro('Wolks', 'fusca', 1990, 'laranja')
uno = Carro('Fiat', 'uno', 2000, 'azul escuro', statusFarol= 'ligado' )
gol2 = Carro('Wolks', 'gol', 2010, 'vermelho')

#utilizando objetos

print(gol.velocimetro)
gol.acelerar(10) #velocimentro de 0 passa a valer 10
print(gol.velocimetro)
print(gol2.velocimetro) #acelerei em 10 apenas o primeiro gol
gol2.acelerar(20)
print(gol2.velocimetro) #acelerando gol 2 em 20. valores diferentes ainda entre gol 1 e gol 2

gol.acelerar(30) #era 10 antes adiciona mais 30 = 40 no velocimentro de gol 1
print(gol.velocimetro)

print(fusca.ligarFarol()) #estava desligado ligou
print(fusca.ligarFarol()) #tentou ligar o ligado e ja estava ligado

fusca.desligarFarol() #desligou o farol
print('---------------------------------------')
#mudando a variavel de um objeto a mesma variavel de outro objeto nao e mudada

print('Farol Uno antes:', uno.statusFarol)
print('Farol fusca antes:', fusca.statusFarol)
print('---------------')
uno.desligarFarol()
fusca.ligarFarol()

print('Farol uno depois:', uno.statusFarol)
print('Farol fusca depois:', fusca.statusFarol)

print(gol.velocimetro)
print(gol2.velocimetro)

print('---------------')
gol.frear() #sem parametro ele vme a frear 5 unidades (foi colocado como padrao la em cima)
print(gol.velocimetro)

gol2.frear(15)
print(gol2.velocimetro) #desacelerou agr gol 2

print('---------')
gol2.frear(15) #estava o velocimetro a a 15. desacelerou mais 15... valor continua 5 que foi colocado como padrao em cima
print(gol2.velocimetro)

print(gol.velocimetro) #objetos diferentes n tem interação.

#iteração com objetos
#criando uma lista de objetos da classe carro

#i = 0
#lista = [] #itinerando 3 vezes para cada input e fazendo append dos dados para uma lista
#while i < 3:
#    marca = input('Digite a marca: ')
#    modelo = input('Digite o modelo: ')
#    ano = int(input('Digite o ano de fabricação: '))
#    cor = input('Digite a cor: ')

#    carro = Carro(marca, modelo, ano, cor)
#    lista.append(carro)
#    i = i+1

#print(lista[0].marca) # serve para acessar ano, modelo, cor etc...
#print(lista)
#primeiro carro index [0], segundo carro index [1] etc...

#lista[1].ligarFarol() #usou método ligar farol no carro index[1] da lista.

#encapsulamento #atributos privados #encapsulamento usa __ antes

jeep = Carro('jeep', 'renegade', 2015, 'branco') #quando prito isso o __status la de cima n aparece
#jeep.   (no jeep. aparece varios atributos e métodos disponíveis para 'jeep' na 'clase Carro')

##get e set da acesso as variaveis privadas (__status)

fox = Carro('Wolks', 'fox', 2009, 'prata')
print(fox.velocimetro) #zero pq foi igualado na classe como padrao
print('-----------------')

print(fox.getStatus()) #falso para desligado #true para ligado
fox.setStatus(True, 123456) #n obedecendo a chave status n altera... tem q colocar a chave 123456

print(fox.getStatus()) #mudando com o set, pega com o get(status agr = True)
print('------------------')

palio = Carro('Fiat', 'palio', 2003, 'prata')
print(palio.getStatus())

palio.setStatus(True, 123456)     #n tem o verifica a chave nem __status. n se cosegue acessar o metodo internamente. apenas a propria classe pode acessar.
print(palio.getStatus())  #transformando o false em true atraves do set status. get para verificar




