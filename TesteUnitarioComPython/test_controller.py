import unittest
from unittest.mock import patch
from unittest import TestCase
import controller 
class CalculatorTests(unittest.TestCase):
    def teste_format_number_BR(self):
        self.assertEqual(controller.controller.format_number_for_BR("1,6"),"1.6")
        self.assertEqual(controller.controller.format_number_for_BR("1.6"),"1.6")
        self.assertEqual(controller.controller.format_number_for_BR(".1.6"),"Digite um numero valido")
        self.assertEqual(controller.controller.format_number_for_BR("1\n6"),"Digite um numero valido")
   



if __name__ == '__main__':
    unittest.main()        
