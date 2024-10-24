lista_de_nota = [8, 10, 5.6, 7, 4.8]

# média soma dos itens / quantidade dos itens
soma = 0

# Acumular os valores na variavel soma
for i in range(len(lista_de_nota)):
    soma +=lista_de_nota[i]

# Pergunta: Qual a média da turma?
media = soma / len(lista_de_nota)

contadora = 0

# Pergunta 2: Quantos alunos acima da média?
for i in range(len(lista_de_nota)):
    if lista_de_nota[i] > media:
        contadora += 1

print(f'A média da turma é: {media:.2f}')
print(f'{contadora} alunos acima da média.')