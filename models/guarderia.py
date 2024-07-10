from models.boa import Boa_Constrictor
from models.huron import Huron

class Guarderia:
    def __init__(self) -> None:
        self.boas = [
            Boa_Constrictor('Boa1', 22, 5, 'Brasil', 15.0),
            Boa_Constrictor('Boa2', 25, 7, 'Colombia', 12.0)
        ]
        self.hurones = [
            Huron('Johan',25 , 15 , 'Col', 50.69),
            Huron('Johaniu',25 , 15 , 'Col', 50.69)
        ]

    def alimentar_boa(self, boa: Boa_Constrictor, ratones: int) -> str:
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.agregarRatonerComidos(ratones)
            return "Éxito"
        except ValueError as e:
            if str(e) == "Demasiados Ratones!":
                return "La boa está llena"
            else:
                raise
