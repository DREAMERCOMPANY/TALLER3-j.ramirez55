import unittest
from models.guarderia import *

class TestGuarderia(unittest.TestCase):
    def setUp(self):
        self.guarderia = Guarderia()

    def test_alimentar_boa_exito(self):
        boa = self.guarderia.boas[0]
        resultado = self.guarderia.alimentar_boa(boa, 3)
        self.assertEqual(resultado, "Éxito")
        self.assertEqual(boa.obtenerRatonerComidos(), 3)

    def test_alimentar_boa_llena(self):
        boa = self.guarderia.boas[0]
        boa.agregarRatonerComidos(8)
        resultado = self.guarderia.alimentar_boa(boa, 3)
        self.assertEqual(resultado, 'Éxito')

    def test_alimentar_boa_no_existente(self):
        resultado = self.guarderia.alimentar_boa(None, 3)
        self.assertEqual(resultado, "Esta Boa no existe!")

if __name__ == '__main__':
    unittest.main()
