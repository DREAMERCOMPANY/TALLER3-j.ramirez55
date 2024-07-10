import unittest
from models.boa import Boa_Constrictor

class Test_Boa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constrictor('Luqui', 22, 10, 'Col', 22.5)
        self.assertEqual(boa.hacer_sonido(), '¡Tsss!')
    
    def test_calcular_flete(self):
        boa = Boa_Constrictor('Luqui', 22, 10, 'Col', 22.5)
        self.assertEqual(boa.calcular_flete(), 22.5 * 22)
    
    def test_agregar_ratones_comidos(self):
        boa = Boa_Constrictor('Luqui', 22, 10, 'Col', 22.5)
        boa.agregarRatonerComidos(3)
        self.assertEqual(boa.obtenerRatonerComidos(), 3)
        boa.agregarRatonerComidos(2)
        self.assertEqual(boa.obtenerRatonerComidos(), 5)
    
    def test_agregar_ratones_comidos_demasiados(self):
        boa = Boa_Constrictor('Luqui', 22, 10, 'Col', 22.5)
        boa.agregarRatonerComidos(8)
        self.assertEqual(boa.obtenerRatonerComidos(), 8)
        with self.assertRaises(ValueError) as context:
            boa.agregarRatonerComidos(13)  # Intentar agregar 13 ratones debería lanzar ValueError
        self.assertTrue('Demasiados Ratones!' in str(context.exception))

if __name__ == '__main__':
    unittest.main()



