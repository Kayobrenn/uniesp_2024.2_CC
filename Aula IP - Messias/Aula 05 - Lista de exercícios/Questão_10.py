#Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
#de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
#escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.

def desafio():
    num_porta = int(input('Qual porta escolhida de 1 á 5?'))

    match num_porta:
        case 1:
            print('Você escolheu a porta Nº1 e enfrentará o desafio da corda bamba!!')
        case 2:
            print('Você escolheu a porta Nº2 e enfrentará o desafio do piso de vidro!!')
        case 3:
            print('Você escolheu a porta Nº3 e enfrentará o desafio do cabo de guerra!!')
        case 4:
            print('Você escolheu a porta Nº4 e enfrentará o desafio da batatinha frita!!')
        case 5:
            print('Você escolheu a porta Nº5 e enfrentará o desafio do biscoito!!')

if __name__ == '__main__':
    
    print('--- --- Iniciando Programa --- ---')

    desafio()

    print('--- --- Fim do Programa --- ---')