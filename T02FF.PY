soma_dias = 0 
mais_dias = -1
veiculo_mais_tempo = ""
total_veiculos = 0

while True:
    modelo = input("Digite o modelo do veiculo:").strip()

    dias = input("Digite o numero de dias que veiculo ficara estacionada: ")
    while not dias.isdigit():
        print("Entrada invalida. Digite um numero inteiro.")
        dias = input("Digite o numero de dias que o veiculo ficara estacionado: ")

    dias =  int(dias)
    soma_dias += dias
    total_veiculos += 1

    if dias > mais_dias:
        mais_dias = dias
        veiculo_mais_tempo = modelo

    continuar = input ("Deseja cadastrar outro veiculo? (s/n): ").strip().lower()
    if continuar != 's':
        break

if total_veiculos > 0: 
    media_dias = soma_dias / total_veiculos
    print("\n--- Resumo da Garagem ---")
    print(f"Total de veiculos cadastrados: {total_dias:.2f}")
    print(f"Media de dias dos veiculos na garagem: {media_dias:.2f}")
    print(f"Veiculo que ficara mais tempo: {media_mais_tempo} ({mais_dias} dias)")
else:
    print("Nenhum veiculo foi cadastrado.")