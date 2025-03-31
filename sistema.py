menu = """

    [w] Depositar
    [a] Sacar
    [s] Extrato
    [d] Sair

    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "w":
        deposito = float(input("""Digite o valor a ser depositado => """))
        if deposito > 0:
            saldo += deposito
            print(saldo)
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        
        
        else:
            print("Valor invalido, tente novamente")


    elif opcao == "a":
        saque = float(input("""Digite o valor a ser sacado => """))
        if saque > 0:
            if numero_saques < 3:
                if saque <= saldo:
                    saldo -= saque
                    print(saldo)
                    numero_saques += 1
                    print(f"{numero_saques} saque(s) foram realizados")
                    extrato += f"Saque: R$ {saque:.2f}\n"

                else:
                    print("Saldo insuficiente, tente novamente.")
            else:
                print("Limite de saques atingido, tente novamente mais tarde")
        else:
            print("Valor invalido, tente novamente")

        
    elif opcao == "s": 
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "d":
        break

    else:
        print("Operacao invalida, seleciona a operacao desejada")
