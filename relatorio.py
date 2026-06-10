def relatorio_biblioteca():
    print("Relatorio da Biblioteca\n")

    with open("livros.txt", "r") as arquivo:
        livros=[linha.strip() for linha in arquivo]

    with open("livros_emprestado.txt", "r") as arquivo:
        livros_emprestados =[linha.strip() for linha in arquivo]

    with open("usuarios.txt", "r") as arquivo:
        usuarios =[linha.strip() for linha in arquivo]    

    print("\n===Livros Disponíveis===\n")

    if len(livros) == 0:
        print("Nenhum Livro está Disponivel no momento. ")
    else:
        for i,livro in enumerate(livros, start=1):
            print(f'{i} - {livro}\n')

    print("\n===Livros Emprestados===\n")

    if len(livros_emprestados) == 0:
        print("Nenhum livro foi Emprestado.")
    else:
        for i, livro in enumerate(livros_emprestados, start=1):
            print(f'\n{i} - {livro}\n')

    print("\n===Usúarios===\n")

    if len(usuarios) == 0:
        print("Nenhum Usuário encontrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f'\n{i} - {usuario}\n')                       