import unittest
from models.huron import Huron

class Test_Boa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron('huroncin',15, 8 , 'Col', 16.5)
        self.assertEqual(huron.hacer_sonido(), '¡Eek Eek!')
    
    def test_calcular_flete(self):
        huron = Huron('huroncin',15, 8 , 'Col', 16.5)
        self.assertEqual(huron.calcular_flete(), 16.5 * 15)
    
    
    if __name__ == '__main__':
        unittest.main()
