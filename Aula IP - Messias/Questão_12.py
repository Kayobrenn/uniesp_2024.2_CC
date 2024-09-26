def validar_arma(ataque, durabilidade, nome_arma):
    if ataque > 50 and durabilidade > 70:
        print('Arma Validada!')
        return nome_arma
    else: 
        return 'erro'

if __name__ == '__main__'

espada_ataque = int(input('Digite o ataque da espada: '))
espada_durabilidade = int(input('Digite a durabilidade da espada: '))

arco_ataque = int(input('Digite o ataque do arco: '))
arco_durabilidade = int(input('Digite a durabilidade do arco: '))

lanca_ataque = int(input('Digite o ataque da lança: '))
lanca_durabilidade = int(input('Digite a durabilidade da lança: '))

if espada_ataque > 50 and espada_durabilidade > 70:
    print('Utilize a espada!')

elif arco_ataque > 50 and arco_durabilidade > 70:
    print('Utilize o arco!')

elif lanca_ataque > 50 and lanca_durabilidade > 70:
    print('Utilize a lança!')

else: # Se nenhuma atender, o programa deve sugerir que o heroi busque uma nova arma
    print('Escolha outra arma!')
