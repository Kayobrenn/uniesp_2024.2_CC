# Tabuada Personalizada:

# Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10). 
# Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.


num = int(input('Insira um número entre 1 e 10: '))

for i in range (10):
    
    i = i+1 
    
    print(f'{num} x {i} = {num*i}')
