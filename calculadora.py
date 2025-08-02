def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da soma
    """
    return a + b
    
def multiplicacao(a, b):
    """
    Realiza a multiplicação de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da multiplicação
    """
    return a * b

def divisao (a, b):
    return a / b   

def subtracao(a, b):
    return a - b    
  
if __name__ == "__main__":
  print("Teste da função soma:")
  print(f"2 + 3 = {soma(2, 3)}") 
  print(f"5.5 + 4.5 = {soma(5.5, 4.5)}") 

  print(f'1900 + 2025 = {soma(1900, 2025)}')
  print("Teste da função divisao:")
  print(f"6 / 3 = {divisao(6, 3)}")  #comentario teste
  print('Teste de subtração')
  print(f'10 - 7 = {subtracao(10, 7)}')