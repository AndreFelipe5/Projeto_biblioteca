def editar_livros():
    print("\n--------> Editar Livros <--------")

    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]

    if len(livros) == 0:
        print("\nNenhum Livro Disponivel\n")
        return

    print("\nLivros Cadastrados:\n")

    for i, livro in enumerate(livros, start=1):
        titulo, autor = livro.split(";")
        print(f'{i} - Titulo: {titulo}')
        print(f' Autor: {autor}')

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

    titulo_antigo, autor_antigo = livros[editar_livro - 1].split(";")

    print("\n1 - Editar Titulo")
    print("\n2 - Editar Autor")
    print("\n3 - Editar Titulo e Autor")

    livro_escolhido = int(input(" Digite a Opção: "))

    if livro_escolhido == 1:
        novo_titulo = input("Novo Titulo: ").strip()
        livros[editar_livro - 1] = f"{novo_titulo};{autor_antigo}"

    elif livro_escolhido == 2:
        novo_autor = input("Novo Autor: ").strip()
        livros[editar_livro - 1] = f"{titulo_antigo};{novo_autor}"

    elif livro_escolhido == 3:
        novo_titulo = input("Novo Titulo: ").strip()
        novo_autor = input("Novo Autor: ").strip()
        livros[editar_livro - 1] = f"{novo_titulo};{novo_autor}"

    elif livro_escolhido == 0:
        return

    else:
        print('Opção Invalida')    
        return

    with open("livros.txt", "w") as arquivo:
        for livro in livros:
            arquivo.write(f"{livro}\n")

    print("\nLivro atualizado com sucesso!\n")
