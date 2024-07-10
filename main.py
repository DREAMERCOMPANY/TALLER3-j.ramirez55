import unittest

# Descubrir y ejecutar todas las pruebas
if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = 'pruebas'  # Directorio donde están los archivos de prueba
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)