# Função de processamento do programa
def funcao_processamento():
    print('Digite o seu tipo de animal favorito:')
    print('1 - Mamífero \n2 - Réptil')
    opcao = int(input('Qual sua opção:'))

    if opcao == 1:
        print('Ah! Certeza que é um doguinho')
    else:
        print('Caramba! Você curte tartarugas!')

if __name__=='__main__':
    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")