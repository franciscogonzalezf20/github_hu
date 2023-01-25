from abc import abstractmethod
from abc import ABC


class Validador(ABC):

    @abstractmethod
    def validar(self):
        pass
