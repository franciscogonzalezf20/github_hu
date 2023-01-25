from abc import abstractmethod
from abc import ABC


class BuilderScraper(ABC):

    @abstractmethod
    def set_root(self):
        pass
    @abstractmethod
    def build(self):
        pass