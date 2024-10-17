# Calculadora de Fatorial:

# Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. 
# Utilize um loop para realizar as multiplicações necessárias.

num = int(input('Insira um número: '))

fat = 1

for i in range (num):
    
    fat*=num
    num-=1
    
print(fat)
