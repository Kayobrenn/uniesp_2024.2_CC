def class_plantas():
    altura_planta = float(input("Digite a altura da planta: "))

    if (altura_planta) <1:
        print("Planta de porte pequeno!")
    elif altura_planta >3:
        print("Planta de porte grande!")
    else:
        print("Planta de porte médio!")

if __name__=='__main__':

    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    class_plantas()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")