import unittest

from kalkulator import sestej, odstej, pomnozi, deli


class TestKalkulator(unittest.TestCase):

    def test_sestevanje(self):
        self.assertEqual(sestej(5, 3), 8)

    def test_odstevanje(self):
        self.assertEqual(odstej(10, 4), 6)

    def test_mnozenje(self):
        self.assertEqual(pomnozi(6, 7), 42)

    def test_deljenje(self):
        self.assertEqual(deli(20, 4), 5)

    def test_deljenje_z_nic(self):
        with self.assertRaises(ValueError):
            deli(10, 0)


if __name__ == "__main__":
    unittest.main()