#Escolha de Feitiços
#a. Descrição: Um mago tem três feitiços: fogo, terra e ar. Crie um programa que receba a
#escolha do usuário (1 para fogo, 2 para terra, 3 para ar) e use o comando match-case para
#exibir o feitiço escolhido.
def escolha():
    
    num_feitico = int(input("1-Fogo 2-Água 3-Terra, Digite o número que corresponde a opção desejada:"))

    match num_feitico:
        case 1:
            print('O feitiço escolhido foi Fogo!')
        case 2:
            print('O feitiço escolhido foi de água!')
        case 3:
            print('O feitiço escolhido foi terra!')

if __name__ == '__main__':
    
    print('--- --- Iniciando Programa --- ---')

    escolha()

    print('--- --- Fim do Programa --- ---')