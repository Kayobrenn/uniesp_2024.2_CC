# Conversor de Decimal para Binário:
# Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. 
# Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.

decimal = int(input('Informe um número decimal: '))

num = ''

while decimal>0: 

    resto = decimal%2
    num = str(resto) + num #concatena em cada loop o resto + num (conforme o loop vai passando vai acumulando os restos deixando o 1º por último na sequência)
    decimal = decimal//2

print(num)