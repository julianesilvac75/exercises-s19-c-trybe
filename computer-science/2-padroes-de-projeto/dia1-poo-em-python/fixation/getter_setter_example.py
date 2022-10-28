class Liquidificador:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__amperagem_atual_no_motor = 0

    # Getter

    @property
    def cor(self):
        return self.__cor

    # Setter

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


    def __str__(self):
        return f"""
        - Cor: {self.__cor}
        - Preco: {self.preco}
        """


liquidificador = Liquidificador("Azul", "110", "127", "200")

# print(f"A cor atual do liquidificador eh {liquidificador.__cor}")
# AttributeError: 'Liquidificador' object has no attribute '__cor'

print(f"A cor atual do liquidificador eh {liquidificador.cor}")
liquidificador.cor = "Vermelho"
print(f"Apos pintarmos, a nova cor eh {liquidificador.cor}")

