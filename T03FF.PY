total_livros = 0 
livros_novos = 0
titulo_mais_antigo = ""
ano_mais_antigo = None

while True:
    titulo = input("Digite o titulo do livro:").strip()

    ano =  input("Digite o ano de publicacao do livro:").strip()
    while not ano.isdigit() or int(ano) <= 0:
        print("Ano invalido. Digite um numero inteiro maior que zero.")
        ano = input("Digite o ano de publicaçao do livreo: ").strip()
    ano = int(ano)

    estado = input("Digite o estado do livro (novo/usado): ").strip().lower()
    while estado not in ["novo", "usado"]:
        print("Estado invalido. Digite apena 'novo' ou 'usado'.").strip().lower()

    total_livros +- 1
    
    if estado == "novo":
        livros_novos += 1
    
    if ano_mais_antigo is None or ano < ano_mais_antigo:
        ano_mais_antigo = ano
        titulo_mais_antigo = titulo

    continuar = input("Deseja cadastrar outro livro? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\n--- Resumo da Biblioteca ---")
print(f"Total de livros cafastrados: {total_livros}")
print(f"Total de livros novos: {livros_novos}")
if total_livros > 0:
    print(f"Livro mais antigo: '{titulo_mais_antigo}' (Ano: {livros_mais_antigos})")
else:
    print("Nenhum livro doi cadastrado.")