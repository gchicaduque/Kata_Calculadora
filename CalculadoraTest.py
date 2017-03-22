from unittest import TestCase

from Calculadora import Calculadora

__author__ = 'German Chica'

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un numero")