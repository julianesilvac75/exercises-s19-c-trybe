from heranca_example import Eletrodomestico

class Liquidificador(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco):
        super().__init__(cor, potencia, voltagem, preco)

    
class Geladeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, voltagem, preco)

        # sobrescrita do metodo da classe mae
        self.quantidade_de_portas = quantidade_de_portas


class Pessoa():
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permitindo a aquisicao de qualquer eletrodomestico

    def comprar_eletrodomestico(self, eletrodomestico: Eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomesticos.append(eletrodomestico)