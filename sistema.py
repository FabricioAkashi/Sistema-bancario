from datetime import date, datetime


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
cpf_cadastrados = set()
contas = []
LIMITE_DE_SAQUES = 3

def deposito():
    global saldo, extrato    
    try:
        deposito = float(input("""Digite o valor a ser depositado => """))
        if deposito > 0:
                saldo += deposito
                print(saldo)
                extrato += f"{datetime.now()} Depósito: R$ {deposito:.2f}\n"
            
            
        else:
                print("Valor invalido, tente novamente")
    except ValueError:
         print("Entrada invalida, tente novamente")

def saque():
    global saldo, extrato, numero_saques   
    try:
        saque = float(input("""Digite o valor a ser sacado => """))
        if saque > 0:
            if numero_saques < 3:
                if saque <= saldo:
                    saldo -= saque
                    print(saldo)
                    numero_saques += 1
                    print(f"{numero_saques} saque(s) foram realizados")
                    extrato += f"{datetime.now()} Saque: R$ {saque:.2f}\n"

                else:
                    print("Saldo insuficiente, tente novamente.")
            else:
                print("Limite de saques atingido, tente novamente mais tarde")
        else:
            print("Valor invalido, tente novamente")
    except ValueError:
         print("Entrada invalida, tente novamente")

def extra():
    global saldo, extrato
    try:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    except ValueError:
         print("Entrada invalida, tente novamente")

def cadastro_de_usuario():
    global usuarios, cpf_cadastrados
    
    try:
        cpf = int(input("""Informe o CPF do usuario (Apenas numeros) => """).strip())

        if cpf in cpf_cadastrados:
            print("CPF em uso, digite novamente")
        else:
            cpf_cadastrados.add(cpf)
            nome = input("""Informe o nome do usuário => """)
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
            print(usuarios)
        
    except ValueError:
        print("Entrada invalida, tente novamente")

# def criar_conta(agencia, numero_conta, usuarios):
#     global cpf_cadastrados

#     cpf = int(input("""Informe o CPF do usuario (Apenas numeros) => """))
    
#     if cpf in cpf_cadastrados:
#         print("Conta criada com sucesso!")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


menu = """

    [w] Depositar
    [a] Sacar
    [s] Extrato
    [f] Cadastrar usuario
    [g] Listar usuarios
    [d] Sair

    => """



while True:

    opcao = input(menu)

    if opcao == "w":
        deposito()

    elif opcao == "a":
        saque()

    elif opcao == "s": 
        extra()

    elif opcao == "f":
        cadastro_de_usuario()

    elif opcao == "d":
        break

    else:
        print("Operacao invalida, seleciona a operacao desejada")