from unittest import TestCase

from Calculadora import Calculadora

__author__ = 'German Chica'

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
