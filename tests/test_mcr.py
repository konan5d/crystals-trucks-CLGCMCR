from turtle import width
import unittest

class read_initiale_information(unittest.TestCase):

    def test_truck_is_instance_of_game(self):
        t = "truck".upper()
        self.assertIsInstance("truck", t)

    def test_nb_cristals_is_positive(self):
        nb_c = nb_cristals
        self.assertGreater(nb_c., 0)

    def test_upper(self):
        resultat = "cristal".upper()
        self.assertEqual("cristal", resultat)

    def test_upper(self):
        resultat = "width".upper()
        self.assertEqual("width", resultat)

    def test_upper(self):
        resultat = "height".upper()
        self.assertEqual("height", resultat)

    def test_upper(self):
        resultat = "nb_trucks".upper()
        self.assertEqual("nb_trucks", resultat)

    def test_upper(self):
        resultat = "nb_cristals".upper()
        self.assertEqual("nb_cristals", resultat)


if __name__ == '__main__':
    unittest.main()




//Rapeler init_game + self.seed
//def init_game(seed: int)