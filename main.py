clientes = []


def mostrar_menu():
    print('='*35)
    print('  AGENDA DA BARBEARIA')
    print('=' *35)
    print('1 - Cadastrar cliente')
    print('2 - Agendar horário')
    print('3 - Listar Clientes')
    print('4 - Sair')


def cadastrar_cliente():
    nome = input('Qual é seu nome:')

    if nome in clientes:

        print('Cliente já cadastrado!')

    else:
        clientes.append(nome)

        print('Cliente cadastrado com sucesso!')


def agendar_horario():
    print('Agendar horário')
    

def listar_clientes():
    print ('\nCLIENTES CADASTRADOS')
    print('='*35)

    for cliente in clientes:
        print(cliente)


def sobre_sistema():
    print('Agenda Barbearia \n versão 1.00 \n autor: kauan')    


while True:

    mostrar_menu()


    opçao = input('Escolha uma opção:')


    if opçao == '1':
        cadastrar_cliente()

    elif opçao == '2':
        agendar_horario()

    elif opçao == '3':
        listar_clientes()

    elif opçao == '4':
        print ('Programa encerrado.')
        break

    else:

        print('opção invalida')