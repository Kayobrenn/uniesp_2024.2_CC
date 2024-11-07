lista_de_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(lista_de_numeros)
print(lista_de_numeros[1])
print(lista_de_numeros[1][2])

# Range tem o valor final não inclusivo
# O len() calcula o tamanho de um objeto
#for i in range(len(lista_de_numeros)):

print(f'Tamanho da lista: {len(lista_de_numeros)}')

''' O for externo está iterando sobre a matriz
ele assume o indice de cada um das listas da matriz'''
for linha in range(len(lista_de_numeros)):

    '''O for interno itera a lista selecionada da vez'''
    for coluna in range(len(lista_de_numeros[linha])):
        print(f'Linha:{linha} - Coluna:{coluna} -> {lista_de_numeros[linha][coluna]}')

        if linha == coluna:
            print('Diagonal Principal')