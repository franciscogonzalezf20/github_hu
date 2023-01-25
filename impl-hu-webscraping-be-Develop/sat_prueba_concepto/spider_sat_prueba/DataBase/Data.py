from abc import abstractmethod
from abc import ABC

class Data(ABC):

    @abstractmethod
    def save_data(self):
        pass
