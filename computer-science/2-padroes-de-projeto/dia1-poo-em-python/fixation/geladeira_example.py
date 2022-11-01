class Geladeira:
    def __init__(self, cor, preco):
        self.preco = preco
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    # Setter

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    def __str__(self):
        return f"""
        - Cor da geladeira: {self.cor}
        - Preco: {self.preco}
        """

geladeira_branca = Geladeira("Branca", 500)

print(geladeira_branca)