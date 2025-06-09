soma_notas = 0 
maior_nota = -1
aluno_maior_nota = ""
total_alunos = 0 

while True:
    nome = input ("Digite o nome do aluno: ").strip()

    nota = input("Digite a nota final do aluno (inteiro): ")
    while not nota.isdigit():
        print("Nota invalida. Digite um numero inteiro.")
        nota = input("Digite a nota final do alujno (inteiro): ")
    
    nota = int(nota)
    soma_notas += nota
    total_alunos += 1

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = nome
    
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break
if total_alunos > 0:
    media = soma_notas / total_alunos
    print("\n--- Resumo da Turma ---")
    print(f"Total de alunos cadastrados: {total_alunos}")
    print(f"Media das notas : {media:.2f}")
    print(f"Aluno com maior nota: {aluno_maior_nota} (Nota: {maior_nota})")
else:
    print("Nenhum aluno foi cadastrado")