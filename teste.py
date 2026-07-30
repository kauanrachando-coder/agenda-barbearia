agendamentos = []

agendamento1 = {
    "cliente": "Carlos",
        "data": "30/07/26",
        "horario": "17:00",
        "servico": "Corte"

}
agendamento2 = {
    'cliente': 'claudio',
    'data': '31/07/26',
    'horario':'19:00',
    'servico': 'barba'
}
agendamentos.append(agendamento1)
agendamentos.append(agendamento2)

print(agendamentos)
for agendamento in agendamentos:
    print('-'*35)
    print('Cliente:',agendamento['cliente'])
    print('Data:',agendamento['data'])
    print('Horário:',agendamento['horario'])
    print('Serviço:',agendamento['servico'])