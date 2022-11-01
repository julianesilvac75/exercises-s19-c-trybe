from geladeira_example import Geladeira
from getter_setter_example import Liquidificador
from class_example import liquidificador_vermelho
from geladeira_example import geladeira_branca


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None
        self.geladeira = None

    def comprar_liquidificador(self, liquidificador: Liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_geladeira(self, geladeira: Geladeira):
        if geladeira.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= geladeira.preco
            self.geladeira = geladeira

    def __str__(self):
        return f"""
        Jacquin:
        - Saldo na conta: {self.saldo_na_conta}
        - Possui liquidificador? { self.liquidificador != None}
        - Possui geladeira? { self.geladeira != None }
        """


pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)
pessoa_cozinheira.comprar_geladeira(geladeira_branca)

print(pessoa_cozinheira)
