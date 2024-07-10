from huron import Huron
from boa import Boa_Constrictor

huroncito = Huron('Xavier', 55 , 20, 'Holanda', 20.6)
print(huroncito.calcular_flete())
huroncito.comer(20)
huroncito.comer(15)
print(huroncito.obtener_kilos_comidos())
print(huroncito.hacer_sonido())
print(huroncito.obtener_edad())
print(huroncito.obtener_peso())

boaAniquiladora = Boa_Constrictor('Aniqui', 55 , 25 , 'Col', 25.8)
boaAniquiladora.agregarRatonerComidos(2)
boaAniquiladora.agregarRatonerComidos(5)
print(boaAniquiladora.obtenerRatonerComidos())
