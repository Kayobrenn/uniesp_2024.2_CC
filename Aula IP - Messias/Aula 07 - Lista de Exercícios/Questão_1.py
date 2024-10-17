# Calculadora de Média de Notas:

# Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. 
# Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).
    
cont = 0
soma = 0
nota = 0

while nota!=-1:
        
    nota = float(input('Insira a nota do aluno: '))
        
    if nota!=-1:
        
        soma += nota
        cont += 1
    
print(f'A média do aluno é: {soma/cont:.1f}')
    
        