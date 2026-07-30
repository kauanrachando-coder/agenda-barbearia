def mostar_menu():
    print('='*35)
    print('  AGENDA DA BARBEARIA')
    print('=' *35)
    print('1 - Cadastrar cliente')
    print('2 - Agendar horário')
    print('3 - Listar agendamentos')
    print('4 - Sair')


def cadastar_cliente():
    print('Cadastro de cliente')


def agendar_horario():
    print('Agendar horário')
    

def listar_agendamentos():
    print('Listar de agendamentos')


def sobre_sistema():
    print('Agenda Barbearia \n versão 1.00 \n autor: kauan')    


while True:

    mostar_menu()


    opçao = input('Escolha uma opção:')


    if opçao == '1':
        print('Cadastro de cliente')

    elif opçao == '2':
        print('Agendar horário')

    elif opçao == '3':
        print('Listar agendamentos')

    elif opçao == '4':
        print ('Sair')
        break

    else:
        print('opção invalida')