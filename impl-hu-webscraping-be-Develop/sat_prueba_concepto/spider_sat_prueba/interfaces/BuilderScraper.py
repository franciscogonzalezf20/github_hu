from abc import abstractmethod
from abc import ABC


class BuilderScraper(ABC):
    @abstractmethod
    def set_root(self, raiz: str):
        pass

    @abstractmethod
    def set_complement(self, complemento: str):
        pass
