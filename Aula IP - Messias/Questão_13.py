#O sistema de defesa de um castelo mágico precisa estar sempre ativo quando o
#exército do rei está fora. Crie um programa que receba a posição do exército (dentro ou fora
#do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente.

def defesa_castelo():
    
    posicao_exercito = input('O exército está dentro ou fora do castelo? ')
    
    match posicao_exercito:
        case 'fora':
            print('Ativar sistema de defesa do castelo!')
        case 'dentro':
            print('Desativar sistema de defesa do castelo!')


if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    defesa_castelo()
   
    print('...Fim do programa...') 