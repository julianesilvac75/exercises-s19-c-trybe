from abc import ABC, abstractmethod


class Combo(ABC):
    def __init__(self):
        self.itens = []
        self.criar_combo()

    @abstractmethod
    def criar_combo():
        pass

    def exibe_itens(self):
        self.itens

    def adicionar_itens(self, item):
        self.itens.append(item)