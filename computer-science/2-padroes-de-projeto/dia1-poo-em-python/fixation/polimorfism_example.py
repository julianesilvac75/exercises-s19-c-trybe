from interface_example import Grafico


class GraficoBarras(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Logica para grafico de barras")


class GraficoRadar(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Logica para grafico radar")


class GraficoPizza(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Logica para grafico de pizza")


grafico_1 = GraficoRadar([1, 2])
grafico_1.desenhar()