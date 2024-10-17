# Contador de Vogais e Consoantes:

# Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela. 
# Utilize um loop para percorrer cada caractere da frase e realizar a contagem.

frase = input('Insira uma frase: ')

cont = 0

for i in frase: 
    
    if i.isalpha():
        
        cont +=1

print(cont)