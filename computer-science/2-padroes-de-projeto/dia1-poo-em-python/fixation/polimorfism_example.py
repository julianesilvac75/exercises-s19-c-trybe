class Grafico:
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self, tipo_de_grafico):
        if tipo_de_grafico == "GraficoBarras":
            self.__desenhar_grafico_barras()

        if tipo_de_grafico == "GraficoRadar":
            self.__desenhar_grafico_radar()

        if tipo_de_grafico == "GraficoPizza":
            self.__desenhar_grafico_pizza()

    def __desenhar_grafico_barras(self):
        print("Logica para grafico de barras")

    def __desenhar_grafico_radar(self):
        print("Logica para grafico radar")

    def __desenhar_grafico_pizza(self):
        print("Logica para grafico pizza")


grafico_1 = Grafico([1, 2])
grafico_1.desenhar("GraficoRadar")