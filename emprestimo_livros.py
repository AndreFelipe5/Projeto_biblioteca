def emprestimo_livros():
    print("Empréstimo de Livros")
    nome_usuario = input("Nome do usuário: ")
    titulo_livro = input("Nome do livro: ")


    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    usuario_encontrado = False

    for linha in usuarios:
        dados = linha.strip().split(";")
        if nome_usuario in dados:
            usuario_encontrado = True
            

    if not usuario_encontrado:
        print("Usuário não encontrado, tente novamente.")
        return


    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

        livro_encontrado = False

        for linha in livros:
            dados = linha.strip().split(";")
            if titulo_livro in dados:
                livro_encontrado = True
                print("Livro indisponivel, tente novamente.")
                break

        if not livro_encontrado:
            with open("usuarios.txt", "a") as arquivo:
                arquivo.write(f"{nome_usuario};{titulo_livro}\n")
                print("Empréstimo registrado com sucesso!")
