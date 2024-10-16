#Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
#guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
#Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
#vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
#considerar a defesa como critério de desempate.

def julgamento():
    
    ataque_guerreiro_um = int(input('Informe o valor de ataque do Guerreiro 01: '))
    defesa_guerreiro_um = int(input('Informe o valor de defesa do Guerreiro 01: '))
    ataque_guerreiro_dois = int(input('Informe o valor de ataque do Guerreiro 02: '))
    defesa_guerreiro_dois = int(input('Informe o valor de defesa do Guerreiro 02: '))
    
    soma_guerreiro_um = ataque_guerreiro_um + defesa_guerreiro_um
    soma_guerreiro_dois = ataque_guerreiro_dois + defesa_guerreiro_dois
    
    if soma_guerreiro_um > soma_guerreiro_dois:
        print('O Guerreiro 01 é o vencedor!')
    elif soma_guerreiro_dois > soma_guerreiro_um:
        print('O Guerreiro 02 é o vencedor!')
    elif soma_guerreiro_um == soma_guerreiro_dois:
        if defesa_guerreiro_um > defesa_guerreiro_dois:
            print('O Guerreiro 01 é o vencedor!')
        elif defesa_guerreiro_dois > defesa_guerreiro_um:
            print('O Guerreiro 02 é o vencedor!')
        else:
            print('Duelo empatado! Ambos são vencedores!')
        
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    julgamento()
   
    print('...Fim do programa...') 