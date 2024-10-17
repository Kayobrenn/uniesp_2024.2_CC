#O conselho real precisa tomar uma decisão crítica: selecionar o próximo
#governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
#programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
#Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
#que há um empate.
#O conselho real precisa tomar uma decisão crítica: selecionar o próximo
#governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
#programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
#Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
#que há um empate.

def decisao_coroa():
    
    cand_um_nota_um = float(input('Informe a 1ª nota do candidato 01: '))
    cand_um_nota_dois= float(input('Informe a 2ª nota do candidato 01: '))
    cand_um_nota_tres = float(input('Informe a 3ª nota do candidato 01: '))
    
    cand_dois_nota_um = float(input('Informe a 1ª nota do candidato 02: '))
    cand_dois_nota_dois= float(input('Informe a 2ª nota do candidato 02: '))
    cand_dois_nota_tres = float(input('Informe a 3ª nota do candidato 02: '))
    
    cand_tres_nota_um = float(input('Informe a 1ª nota do candidato 03: '))
    cand_tres_nota_dois = float(input('Informe a 2ª nota do candidato 03: '))
    cand_tres_nota_tres = float(input('Informe a 3ª nota do candidato 03: '))
    
    media_cand_um = (cand_um_nota_um + cand_um_nota_dois + cand_um_nota_tres)/3
    media_cand_dois = (cand_dois_nota_um + cand_dois_nota_dois + cand_dois_nota_tres)/3
    media_cand_tres = (cand_tres_nota_um + cand_tres_nota_dois + cand_tres_nota_tres)/3

    if media_cand_um > media_cand_dois and media_cand_um > media_cand_tres:
        print('O candidato 01 teve a maior média!')
    elif media_cand_dois > media_cand_um and media_cand_dois > media_cand_tres: 
        print('O candidato 02 teve a maior média!')
    elif media_cand_tres > media_cand_um and media_cand_tres > media_cand_dois: 
        print('O candidato 03 teve a maior média!')
    else:
        print('Houve um empate!')
        
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    decisao_coroa()
   
    print('...Fim do programa...') 
    