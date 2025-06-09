Total_clientes = 0 
soma_gastos = 0
maior_gasto = -1
cliente_maior_gasto = ""

while True:
    nome = input("Digite o nome do cliente: ").strip()

    valor = input("Digite o valor total gasto pelo cliene (em reais): ").strip()
    while not valor.isdigit():
        print("Valor invalido. Digite apenas numeros inteiros (sem virgula ou ponto).")
        valor = input("Digite o valor total gasto pelo liente (em reais): ").strip()

        valor = int(valor)
        soma_gastos += 1 
        total_clientes += 1

        if valor > maior_gasto:
            maior_gasto = valor
            cliente_maior_gasto =nome
        continuar = input("Deseja cadastrar outro cliente? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print("\n--- Resumo das Compras ---")
    print(f"Total de clentes cadastrados: {Total_clientes}")
    print(f"Soma total dos valores gasto: R$ {soma_gasto}")
    if total_clientes > 0:
        print(f"Cliente que mais gastou: {cliente_maior_gasto} (R$ {maior_gasto})")
    else:
        print("Nenhum cliente foi cadastrado.")