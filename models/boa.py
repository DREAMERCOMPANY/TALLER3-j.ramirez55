from models.animalExotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratonesComidos = 0
        
        
    
    def obtenerRatonerComidos(self):
        return  self.__ratonesComidos
    
    def agregarRatonerComidos(self, raton):
        if self.__ratonesComidos + raton > 20:
            raise ValueError("Demasiados Ratones!")
        self.__ratonesComidos += raton

    def hacer_sonido(self):
        return '¡Tsss!'
        
    

    