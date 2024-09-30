def jornada_deserto():
    qtd_agua = float(input("Qual a quantidade de água disponível em litros? "))
    distancia_km = float(input("Qual a distância até o oásis em quilômetros? "))

    if qtd_agua >= distancia_km * 2:
        print("A quantidade de água é suficiente para chegar ao próximo oásis!")
    else:
        print("A quantidade de água é insuficiente para chegar ao próximo oásis!")

if __name__ == '__main__':
    print('--- --- Iniciando Programa --- ---')
    jornada_deserto()
    print('--- --- Fim do Programa --- ---')