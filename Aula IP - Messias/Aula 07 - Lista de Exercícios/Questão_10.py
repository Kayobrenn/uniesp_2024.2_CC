# Simulador de Lançamento de Dados:

# Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. 
# Utilize um loop para realizar os lançamentos e exibir os resultados.

import random

def lancar_dados(vezes):
    resultados = []
    for _ in range(vezes):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
        print(f"Lançamento {_+1}: {resultado}")
    return resultados

vezes = int(input("Quantas vezes você quer lançar o dado? "))
resultados = lancar_dados(vezes)
print(f"Resultados dos lançamentos: {resultados}")