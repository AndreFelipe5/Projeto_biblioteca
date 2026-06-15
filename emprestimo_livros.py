def emprestimo_livros():
    print("\n--------> Empréstimo de Livros <--------\n")

    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]

    if len(livros) == 0:
        print("Não há livros disponiveis para emprestimo\n")
        return

    print("Lista de Livros disponíveis para Empréstimo:\n")

    for i, livro in enumerate(livros, start=1):
        print((f"{i} - {livro}"))

    while True:

        livro_escolhido = input("\nDigite o número do Livro para Empréstimo: ")

        if livro_escolhido.isdigit():
            livro_escolhido = int(livro_escolhido)

            if 1 <= livro_escolhido <= len(livros):
                break

            else:
                print("\nOpção invalida, Escolha um número dos livros listados.")
        else:
            print("\nDigite apenas números.")

    livro_emprestado = livros.pop(livro_escolhido - 1)

    with open("livros.txt", "w") as arquivo:
        for livro in livros:
                arquivo.write(livro + "\n")

    with open("livros_emprestado.txt", "a") as arquivo:
        arquivo.write(livro_emprestado + "\n")

    print(f"\nO livro escolhido foi: {livro_emprestado}")
    print("Livro emprestado com sucesso!\n")
