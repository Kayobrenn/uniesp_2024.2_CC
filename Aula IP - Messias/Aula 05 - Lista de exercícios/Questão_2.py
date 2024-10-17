# Função de processamento do programa
def funcao_processamento():
    qtd_ferro = float(input('Digite a quantidade de ferro: '))
    qtd_ouro = float(input('Digite a quantidade de ouro: '))

    total_liga_metalica = qtd_ferro + qtd_ouro

    if (total_liga_metalica) >=70:
        print('A sua armadura tem a combinação esperada!!!')
    else:
        print('A sua armadura não atende aos críterios!!!')

if __name__=='__main__':

    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")