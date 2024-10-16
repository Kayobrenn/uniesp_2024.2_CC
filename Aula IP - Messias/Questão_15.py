#Um cientista está criando um portal de viagem no tempo que só pode ser ativado se
#todos os parâmetros estiverem corretos: energia acima de 80%, coordenadas de destino
#precisas, e o tempo ajustado corretamente. Crie um programa que receba esses valores e use
#operadores lógicos para verificar se o portal pode ser ativado. Se qualquer parâmetro estiver
#incorreto, o programa deve indicar qual é o problema.

def viagem_tempo():
    
    energia = int(input('Informe a porcentagem de energia: '))
    coordenadas = input('As coordenadas de destino estão precisas: ')
    tempo = input('O tempo está ajustado corretamente: ')
    
    if energia>80 and coordenadas == 'sim' and tempo == 'sim':
        print('Portal de viagem no tempo ativado!')
    else: #os if vão verificar cada condição separadamente
        if energia<80: 
            print('Energia abaixo de 80%!')
        if coordenadas == 'não': 
            print('Coordenadas de destino imprecisas!')
        if tempo == 'não': 
            print('Tempo ajustado incorretamente!')
    
    
if __name__ == '__main__':
    
    print('...Iniciando programa...') 
   
    viagem_tempo()
   
    print('...Fim do programa...') 