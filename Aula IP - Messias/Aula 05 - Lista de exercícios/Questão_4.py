def calculo_moedas():
    qtd_m1 = float(input("Qual a quantidade de moedas de R$1,00 real? "))
    qtd_m50 = float(input("Qual a quantidade de moedas de R$0,50 centavos? "))
    qtd_m25 = float(input("Qual a quantidade de moedas de R$0,25? "))

    qtd_moedas = qtd_m25*0.25 + qtd_m50*0.5 + qtd_m1 # A variavel qtd_moedas recebe o valor de todas as moedas e caulcula

    print(f"O valor total das moedas é de R${qtd_moedas}!")
    
if __name__=='__main__':

    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    calculo_moedas()

    # Mensagem de fim do programa
    print("--- --- Fim do programa --- ---")