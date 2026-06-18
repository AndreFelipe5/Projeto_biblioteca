def relatorio_biblioteca():

    print("\n--------> Relatorio da Biblioteca <--------\n")

    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]

    with open("livros_emprestado.txt", "r") as arquivo:
        livros_emprestados = [linha.strip() for linha in arquivo]

    print("---> Livros Disponíveis <---\n")

    if len(livros) == 0:
        print("Nenhum Livro está Disponivel no momento. ")

    else:
        for i, livro in enumerate(livros, start=1):
            titulo,autor = livro.split(';')
            print(f'Titulo: {titulo}\n Autor: {autor}\n')
    print(f"\nTotal de Livros Disponíveis: {len(livros)}\n")

    print("---> Livros Emprestados <---\n")

    if len(livros_emprestados) == 0:
        print("Nenhum livro foi Emprestado.\n")

    else:
        for i, livro in enumerate(livros_emprestados, start=1):
            print(f"{i} - {livro}")

    print(f"Total de livros emprestados: {len(livros_emprestados)}")

    total_livros = len(livros) + len(livros_emprestados)

    print(f"\nTotal de Livros cadastrados na biblioteca: {total_livros}\n")
    
