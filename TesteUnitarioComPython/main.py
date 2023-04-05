import math
import validations
import controller

#raiz quadrada
def raizquadrada(num1):
  try:
    if validations.validations.is_number(num1):
      raise ValueError("Todos os parametros tem que ser string")
    
    
    num1 = controller.controller.format_number_for_BR(num1)    
    num1 = float(num1.replace(",","."))

    raiz = math.sqrt(num1)

    return raiz
  
  except ValueError as erro:
    return str(erro)
  

# Adição
def soma (num1=3,num2=3):

  try:
    if validations.validations.is_number(num1,num2):
      raise ValueError("Todos os parametros tem que ser string")
    num1 = controller.controller.format_number_for_BR(num1)
    num2 = controller.controller.format_number_for_BR(num2)
   
      
    num1 = float(num1.replace(",","."))
    num2 = float(num2.replace(",","."))
    return num1 + num2
  except ValueError as erro:
     return str(erro)
# Subtração
def subtracao(num1=3,num2=3):

  try:
    if validations.validations.is_number(num1,num2):
      raise ValueError("Todos os parametros tem que ser string")
    num1 = controller.controller.format_number_for_BR(num1)
    num2 = controller.controller.format_number_for_BR(num2)
      
    num1 = float(num1.replace(",","."))
    num2 = float(num2.replace(",","."))
    return num1 - num2
  except ValueError as erro:
    return str(erro)

# Multiplicação
def multiplicacao(num1=3,num2=3):
  try:
    if validations.validations.is_number(num1,num2):
      raise ValueError("Todos os parametros tem que ser string")

    for key,i in enumerate(num1):
        if not i.isdigit() :
          if (i == "." or i == ",") and key > 0:
            num1.replace(",",".")
          elif not (i == "-" and key == 0) :
            raise ValueError("Digite um numero valido")
            break
    for key,i in enumerate(num2):
        if not i.isdigit() :
          if (i == "." or i == ",") and key > 0:
            num2.replace(",",".")
          elif not (i == "-" and key == 0) :
            raise ValueError("Digite um numero valido")
            break
      
    num1 = float(num1.replace(",","."))
    num2 = float(num2.replace(",","."))
    return num1 * num2
  except ValueError as erro:
    return str(erro)

# Divisão
def divisao(num1=3,num2=3):
  try:
    if validations.validations.is_number(num1,num2):
      raise ValueError("Todos os parametros tem que ser string")

    if not num2 == '0':
      num1 = controller.controller.format_number_for_BR(num1)
      num2 = controller.controller.format_number_for_BR(num2)
      
      num1 = float(num1.replace(",","."))
      num2 = float(num2.replace(",","."))
      return num1 / num2
    else:
      raise ValueError("o denominador não pode ser 0")
  except ValueError as erro:
    return str(erro)