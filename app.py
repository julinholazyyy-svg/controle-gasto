gastos = []

def adicionar_gasto():
    nome = input("Nome do gasto: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")

    gastos.append({
        "nome": nome,
        "valor": valor,
        "categoria": categoria
    })

    print("Gasto adicionado com sucesso!\n")

def listar_gastos():
    if len(gastos) == 0:
        print("Nenhum gasto registrado.\n")
        return

    total = 0
    for gasto in gastos:
        print(f"{gasto['nome']} - €{gasto['valor']} ({gasto['categoria']})")
        total += gasto['valor']

    print(f"\nTotal gasto: €{total}\n")

def menu():
    while True:
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida\n")

menu()
