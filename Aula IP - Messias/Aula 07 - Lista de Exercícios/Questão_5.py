# Sequência de Fibonacci:

# Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário. 
# Utilize um loop para calcular e exibir os termos da sequência.

qtd = int(input('Insira a quantidade de números da sequência: '))

a = 0
b = 1
c = 0

for i in range(qtd):

    print (a)
    c = a + b 
    b = a
    a = c
 
    
    
  