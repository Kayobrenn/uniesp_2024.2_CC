from time import sleep

def enviar_lembrete():

    spam = 0

    while spam < 6:

        print(f'Altere sua senha. Lmbrete nº  {spam}')
        spam = spam + 1
        sleep(2)

if __name__ == '__main__':

    enviar_lembrete()