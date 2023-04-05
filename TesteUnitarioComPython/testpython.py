from unittest.mock import patch
import unittest 
import main as calculadora


class CalculatorTests(unittest.TestCase):

    # pega os valores dos inputs da soma
    def test_input_value_number_one_and_number_two_and_sum(self):
    # Testa o metodo por unidade, teste da função deve retornar parametros para realizar os testes
        action = calculadora.soma(2 + 2)
        expected = 4
        self.assertEqual(action, expected)
    # A classe onde possui as funções não possui parametros, bem como o input onde não possui    
    def test_input_value_number_one_and_number_two_and_sub(self):
        action = calculadora.subtracao()
        expected = 4 + 4
        self.assertEqual(action, expected)

    def test_input_value_number_one_and_number_two_and_div(self):
        action = calculadora.subtracao(2 / 2)
        expected = 1
        self.assertEqual(action, expected)

    def test_input_value_number_one_and_number_two_and_mult(self):
        action = calculadora.subtracao(2 * 2)
        expected = 4
        self.assertEqual(action, expected)

if __name__ == '__main__':
    unittest.main() 
        

     