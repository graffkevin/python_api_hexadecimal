from abc import ABC, abstractmethod

class DataOutPutPort(ABC):
    @abstractmethod
    def get_municipality_typology(self, code_insee: str) -> dict:
        pass