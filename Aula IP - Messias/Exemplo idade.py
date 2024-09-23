def idade_mae(idade_m):
    idade_padrao = 42  # Valor idade mâe

    if idade_m == idade_padrao:
        print('Idade correta!')
    elif idade_m > idade_padrao:
        print('Idade maior que a correta!')
    else:
        print('Idade menor que a correta!')

if __name__ == '__main__':
    idade1 = float(input("Digite a idade da sua mãe: "))
    idade_mae(idade1)
