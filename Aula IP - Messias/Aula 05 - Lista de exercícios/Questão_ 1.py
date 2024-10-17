# Função de processamento do programa
def funcao_processamento():
    # Valores Aleatórios
    qtd_norte = float(input('Digite a quantidade de passos para o Norte: ')) #
    qtd_lest = float(input('Digite a quantidade de passos para o Leste: '))
    # Soma da quantidade de passos
    qtd_passos = qtd_norte + qtd_lest
    # Apresentação do resultado
    print(f'A quantidade de passos para o pirata chegar até o tesouro será de {qtd_passos} passos!')

 

if __name__=='__main__':

    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")