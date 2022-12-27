# 3 operações: depósito, saque e extrato

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        valor = float(input('Informe o valor de depósito: '))
        if valor <= 0:
            print('Operação inválida, digite um valor positivo.')
            continue
        else:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

    elif opcao == 's':
        print('Saque')
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diário excedido.')
            continue
        else:
            valor = float(input('Que valor deseja sacar? '))
            if valor <= 0:
                print('Operação inválida, digite um valor positivo.')
                continue
            elif valor > 500:
                print('Valor de saque excede R$ 500.00')
                continue
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque: R$ {valor:.2f}\n'

    elif opcao == 'e':
        print('Extrato')
        extrato += '#--------------------\n'
        extrato += f'Saldo: R$ {saldo:.2f}'
        print(extrato)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')