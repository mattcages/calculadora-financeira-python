def menu():
    print("\n===== CALCULADORA FINANCEIRA =====")
    print("[1] Total de dinheiro")
    print("[2] Total de economia")
    print("[3] Economia com tempo")
    print("[4] Economia com juros (%)")
    print("[5] Economia com depósitos + juros (%)")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        total_dinheiro()
    elif opcao == 2:
        total_economia()
    elif opcao == 3:
        economia_tempo()
    elif opcao == 4:
        economia_juros()
    elif opcao == 5:
        economia_completa()
    else:
        print("Opção inválida!")


# -----------------------------

def total_dinheiro():
    saldo = float(input("Saldo atual: "))
    economia = float(input("Valor guardado: "))
    total = saldo + economia

    print(f"\n💰 Você tem no total: R$ {total:.2f}")


# -----------------------------

def total_economia():
    economia = float(input("Quanto você tem guardado: "))
    print(f"\n🏦 Total guardado: R$ {economia:.2f}")


# -----------------------------

def economia_tempo():
    economia = float(input("Quanto você já tem: "))
    meses = int(input("Por quantos meses vai guardar: "))
    valor_mensal = float(input("Quanto vai guardar por mês: "))

    total = economia + (valor_mensal * meses)

    print(f"\n📈 Em {meses} meses você terá: R$ {total:.2f}")


# -----------------------------

def economia_juros():
    valor = float(input("Valor inicial: "))
    meses = int(input("Quantidade de meses: "))
    juros = float(input("Juros mensal (%): "))

    for _ in range(meses):
        valor += valor * (juros / 100)

    print(f"\n📊 Total com juros: R$ {valor:.2f}")


# -----------------------------

def economia_completa():
    valor = float(input("Valor inicial: "))
    deposito = float(input("Depósito mensal: "))
    meses = int(input("Quantidade de meses: "))
    juros = float(input("Juros mensal (%): "))

    for _ in range(meses):
        valor += deposito
        valor += valor * (juros / 100)

    print(f"\n🚀 Total final: R$ {valor:.2f}")


# -----------------------------

menu()