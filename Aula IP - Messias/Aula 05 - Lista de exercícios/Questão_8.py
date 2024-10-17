def bonus_ouro():
    qtd_missoes = int(input("Quantas missões foram realizadas por você cavaleiro?"))

    if qtd_missoes > 10:
        print('Seu bônus pelas missões é de 100 moedas de ouro!!!')
    elif qtd_missoes < 5:
        print('Seu bônus pelas missões é de 10 moedas de ouro!!!')
    else:
        print('Seu bônus pelas missões é de 50 moedas de ouro!!!')

if __name__ == '__main__':

    print('--- --- Iniciando Programa --- ---')

    bonus_ouro()

    print('--- --- Fim do Programa --- ---')