from abc import ABC, abstractmethod

from item_cardapio import ItemFritas, ItemHamburger, ItemRefrigerante, ItemSorvete


class Combo(ABC):
    def __init__(self):
        self.itens = []
        self.criar_combo()

    @abstractmethod
    def criar_combo(self):
        pass

    def exibe_itens(self):
        return self.itens

    def adicionar_itens(self, item):
        self.itens.append(item)


class ComboTudo(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemSorvete())
        self.adicionar_itens(ItemFritas())
        self.adicionar_itens(ItemRefrigerante())


class ComboFeliz(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemFritas())
        self.adicionar_itens(ItemRefrigerante())


class ComboGelado(Combo):
    def criar_combo(self):
        self.adicionar_itens(ItemHamburger())
        self.adicionar_itens(ItemSorvete())
        