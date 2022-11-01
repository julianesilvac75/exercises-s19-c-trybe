from abc import ABC, abstractmethod


class Grafico(ABC):
    @abstractmethod
    def desenhar(self):
        raise NotImplementedError