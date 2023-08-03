from abc import ABC, abstractmethod
class ComType(ABC):
    @abstractmethod
    def data(self,jsonData,player):
        pass

