from models.animal import Animal
from abc import ABC , abstractmethod

class Animal_Exotico(Animal, ABC):
    def __init__(self, nombre, peso, edad, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        
        

    def calcular_flete(self):
        return self._impuestos * self._peso

    @abstractmethod
    def hacer_sonido(self):
        pass
