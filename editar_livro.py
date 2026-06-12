def editar_livros():
    print("\n--------> Editar Livros <--------")

    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]

    if len(livros) == 0:
        print("\nNenhum Livro Disponivel\n")
        return

    print("\nLivros Cadastrados:\n")

    for i, livro in enumerate(livros, start=1):
        print(f"{i} - {livro}")

    while True:

        editar_livro = input("\nDigite o número do livro para Edita-lo: ")

        if editar_livro.isdigit():
            editar_livro = int(editar_livro)

            if 1 <= editar_livro <= len(livros):
                break
            else:
                print("Livro não encontrado, Escolha um número da lista")

        else:
            print("Digite apenas números.")

    novo_nome = input("\nDigite o Novo nome do Livro: ")

    livros[editar_livro - 1] = novo_nome

    with open("livros.txt", "w") as arquivo:
        for livro in livros:
            arquivo.write(f"{livro}\n")

    print("\nLivro atualizado com sucesso!\n")
