from models.animalExotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
    
    def hacer_sonido(self):
        return '¡Eek Eek!'