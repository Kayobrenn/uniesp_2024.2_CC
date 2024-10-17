# Verificador de Número Primo:

# Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. 
# Utilize um loop para testar a divisibilidade do número por outros números menores.

num = int(input('Insira um número qualquer: '))

cont = 1

for i in range(num):

    if num%cont == 0:
        
        cont+=1

if cont == 2 and num!=2:
    print('Número não é primo!')
else:
    print('Número é primo!')   