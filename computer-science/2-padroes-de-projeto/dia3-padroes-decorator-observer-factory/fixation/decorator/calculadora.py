from struct import calcsize
from unicodedata import numeric


class Calculadora:
    def soma(self, x, y):
        return x + y

class CalculadoraDecorada:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def converter_numero(self, numero):
        if not isinstance(numero, str):
            return numero

        # Neste cenário, em vez de fazermos IF e else... podemos usar o dicionário
        # conseguimos acessar e obter o valor a partir da chave
        return {
            "um": 1, "dois": 2, "tres": 3, "quatro": 4, "cinco": 5,
            "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10
        }.get(numero)

    def soma(self, x, y):
        return self.calculadora.soma(
            self.converter_numero(x), self.converter_numero(y)
        )


class DecoratedCalculator:
    def __init__(self, calculator):
        self.calculator = calculator

    def convert_numer(self, number):
        if not isinstance(number, str):
            return number

        return {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
        }.get(number)

    def soma(self, x, y):
        return self.calculator.soma(
            self.convert_numer(x), self.convert_numer(y)
        )
        

if __name__ == "__main__":
    calculadora = Calculadora()
    print("10 + 20 =", calculadora.soma(10, 20))

    calculadora_decorada = CalculadoraDecorada(calculadora)
    print("'oito' + 'dois' =", calculadora_decorada.soma("oito", "dois"))
    print("'sete' + 'dez' =", calculadora_decorada.soma("sete", "dez"))

    decorated_calculator = DecoratedCalculator(calculadora)
    print("'nine' + 'three' =", decorated_calculator.soma("nine", "three"))
