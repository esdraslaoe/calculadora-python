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

if __name__ == "__main__":
    print("Teste da função soma:")
    print(f"2 + 3 = {soma(2, 3)}") 
    print(f"5.5 + 4.5 = {soma(5.5, 4.5)}") 

    print(f'1900111 + 2025111 = {soma(1900111, 2025111)}')  # Adicionando segundo comentário.
    print(f'70 + 100 = {soma(70, 100)}')

    print('tudo certo nada errado')