import unittest
from unittest.mock import patch
from unittest import TestCase
import main as calculadora
class CalculatorTests(TestCase):
#-------------------------------- teste da soma---------------
    def test_soma(self):
        self.assertEqual(calculadora.soma('2.60','2'),4.60)

    def test_soma_com_virgula(self):
        self.assertEqual(calculadora.soma('2,60','2'),4.60)

    def test_soma_com_gigitos(self):
        self.assertEqual(calculadora.soma('2/60','2'),'Digite um numero valido')
        self.assertEqual(calculadora.soma('.260','2'),'Digite um numero valido')

    def test_soma_is_string(self):
       self.assertEqual(calculadora.soma(2,'2'),"Todos os parametros tem que ser string")
       self.assertEqual(calculadora.soma(2,2),"Todos os parametros tem que ser string")
       self.assertEqual(calculadora.soma('2',2),"Todos os parametros tem que ser string")
#------------------------------------------------------------------------------------------
#----------------------- Teste Raiz quadrada --------------------------------------------
    def test_raizquadrada_is_string(self):
      self.assertEqual(calculadora.raizquadrada(4),"Todos os parametros tem que ser string")

    def test_raizquadrada(self):
      self.assertEqual(calculadora.raizquadrada('4'),2)
      self.assertEqual(calculadora.raizquadrada('4,0'),2)
      self.assertEqual(calculadora.raizquadrada('4.0'),2)


    def test_raizquadrada_digits(self):
       self.assertEqual(calculadora.raizquadrada("4/4"),'Digite um numero valido')
       self.assertEqual(calculadora.raizquadrada("4a4"),'Digite um numero valido')
#------------------------------------------------------------------------------------------
#----------------------- Teste Subtração --------------------------------------------   
    def test_subtracao(self):
      self.assertEqual(calculadora.subtracao("2","2"),0)
      self.assertEqual(calculadora.subtracao("2","5"),-3)

    def test_subtracao_is_istring(self):
       self.assertEqual(calculadora.subtracao(1,2),"Todos os parametros tem que ser string")
       self.assertEqual(calculadora.subtracao('1',2),"Todos os parametros tem que ser string")
    
# -----------------------------Teste de divisao ----------------------------------
    def test_divisao(self):
       self.assertEqual(calculadora.divisao('1','0'),"o denominador não pode ser 0")
       self.assertEqual(calculadora.divisao('2','2'),1)
    def teste_digit_divissao(self):
       self.assertEqual(calculadora.divisao("2.2","1.1"),2)
       self.assertEqual(calculadora.divisao("2,2","1.1"),2)
       self.assertEqual(calculadora.divisao("2,2",".1.1"),'Digite um numero valido')
# ---------------------------------------------------------------------
#----------------Test de multiplicação ------------------------------------------------
    def test_multplicacao(self):
       self.assertEqual(calculadora.multiplicacao("2","2"),4)
    def test_multplicacao_is_string(self):
       self.assertEqual(calculadora.multiplicacao(2,2),"Todos os parametros tem que ser string")
    def test_muntplicacao_digit(self):
       self.assertEqual(calculadora.multiplicacao('2.2','2.2'),4.840000000000001)
       self.assertEqual(calculadora.multiplicacao('2,2','2.2'),4.840000000000001)
       self.assertEqual(calculadora.multiplicacao('2-2','2-2'),'Digite um numero valido')
       


if __name__ == '__main__':
    unittest.main()        
