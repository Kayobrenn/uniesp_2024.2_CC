# Escreva um programa em Python que leia o arquivo de texto vingadores.txt e 
# mande uma mensagem convidando-os para uma festa na sua casa.
    

with open('aula06//TED//vingadores.txt', 'r', encoding='utf-8') as texto:
     
    for line in texto:
        print(line)
        
with open('aula06//TED//vingadores.txt', 'a', encoding='utf-8') as texto:     
    
    texto.write('Estão todos convidados para uma festa na minha casa hoje de 20h!\n')

