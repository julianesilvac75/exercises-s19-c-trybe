class liquidificador:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__amperagem_atual_no_motor = 0

    
    def ligar(self, velocidade):
        self.__velocidade = velocidade
        self.__amperagem_atual_no_motor = (
            (self.__potencia / self.__voltagem) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True
    

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0


    def esta_ligado(self):
        return self.__ligado


# liquidificador_azul = liquidificador('Azul', 200, 127)

liquidificador_vermelho = liquidificador('Vermelho', 250, 220, 100)
liquidificador_vermelho.ligar(1)
print("Esta ligado?", liquidificador_vermelho.esta_ligado()) 

liquidificador_vermelho.desligar()

print("Esta ligado?", liquidificador_vermelho.desligar())