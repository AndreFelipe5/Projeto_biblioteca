def devolver_livro():

    print("--------> Livros Emprestados <--------\n")

    with open("livros_emprestado.txt", "r") as arquivo:
        livros_emprestados = [linha.strip() for linha in arquivo]
    print("Lista de Livros:\n ")

    for i, livro in enumerate(livros_emprestados, start=1):
        print(f"{i} - {livro}")

    while True:

        livro_escolhido = input("\nQual Livro deseja devolver? ")

        if livro_escolhido.isdigit():
            livro_escolhido = int(livro_escolhido)

            if 1 <= livro_escolhido <= len(livros_emprestados):
                break

            else:
                print("Opção inválida, Escolha um número dos livros listados")
        else:
            print("Digite apenas Números.")

    livro_devolvido = livros_emprestados.pop(livro_escolhido - 1)

    with open("livros_emprestado.txt", "w") as arquivo:
        for livro in livros_emprestados:
              arquivo.write(f"{livro}\n")

    with open("livros.txt", "a") as arquivo:
                arquivo.write(f"{livro_devolvido}\n")

    print(f"\nO livro escolhido foi: {livro_devolvido}")
    print("Devolvido com sucesso!\n")
