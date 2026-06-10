def editar_livros():
    print("Editar Livros\n")

    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]

    if len(livros) == 0:
        print('Nenhum Livro encontrado')
        return
        
    print('\n Livros Cadastrados')

    for i, livro in enumerate(livros, start=1):
        print(f'{i} - {livro}')

    editar_livro = int(input('Digite o número do livro para Edita-lo: '))

    if 1 <= editar_livro <= len(livros):

        novo_nome = input("Digite o nome nome do Livro: ")

        livros[editar_livro - 1] = novo_nome

        with open("livros.txt", "w") as arquivo:
            for livro in livros:
                arquivo.write(f'{livro}\n')

        print('Livro atualizado com sucesso!')  

    else:
        print('Livro não encontrado.')
        return


    