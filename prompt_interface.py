abertura = 'Para tipos de comandos disponíveis, digite "cmd".\nPara sair digite "sair"'

lista_de_comandos = []


def print_lista(lista):
    for x in lista:
        print(x)


def prompt():

    while True:

        print(abertura)

        prompt = input('prompt:')

        if prompt == 'cmd':
            print_lista(lista_de_comandos)

        elif prompt == 'selic':
            pass

        elif prompt == 'sair':
            break

        else:
            print('\nDigite um comando válido')


prompt()
