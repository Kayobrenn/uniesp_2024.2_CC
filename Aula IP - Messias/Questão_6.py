def funcao_processamento():
    Distancia = 1000

    dragao1 = float(input("Digite o tempo do dragão 1:"))
    dragao2 = float(input("Digite o tempo do dragão 2:"))

    vel_dga1 = Distancia / dragao1
    vel_dga2 = Distancia / dragao2

    if vel_dga1 > vel_dga2:
        print("O Banguela é o mais veloz!")
    elif vel_dga2 > vel_dga1:
        print("O Banguela é fraco!")
    else:
        print("Os dois dragão tem a mesma velocidade!")

if __name__=='__main__':

    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")