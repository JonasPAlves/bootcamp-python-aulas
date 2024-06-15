def menu():
    menu = """\n
    ================ MENU ================
    
    Selecione a opção desejada!
    
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova Conta
    [lc]Listar Contas
    [nu]Novo usuário
    [q]Sair
    => """
    return input((menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso! ")
    else:
        print("\nOperação falhou! O valor informado é menor que zero.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Você não tem saldo suficiente! Por favor realize um depósito e tente novamente.")

    elif excedeu_limite:
        print("\n Operação falhou! Por favor realize um depósito e tente novamente.")

    elif excedeu_saques:
        print("\n Número máximo de saques excedido. Tente novamente amanhã!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! ")

    else:
        print("\nO valor informado é inválido. Digite um valor maior que zero")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")
    
    print("\n Deseja cadastrar um novo usuário? ")
    
    menu_criar_usuário = """\n
   
    Selecione a opção desejada!
    
    [s]SIM
    [n]NÃO
    => """
    return input((menu_criar_usuário))     
 


def listar_contas(contas):
    print("Não existem contas cadastradas." if not contas else contas)     
    
    for conta in contas:
        
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual valor deseja depositar? R$: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor que deseja sacar: R$  "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc": 
                       
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
