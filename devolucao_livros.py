def devolver_livro():

    print("Livros Emprestados \n")

   
    with open("livros_emprestado.txt", "r") as arquivo:
        livros_emprestados = [linha.strip() for linha in arquivo]
    print("Lista de Livros:\n ")

    for i, livro in enumerate(livros_emprestados, start=1):
        print(f'{i} - {livro}\n')

    livro_escolhido = int(input('Qual Livro deseja devolver? '))

    if 1 <= livro_escolhido <= len(livros_emprestados):
        livro_devolvido = livros_emprestados.pop(livro_escolhido - 1)

        with open("livros_emprestado.txt", "w") as arquivo:
            for livro in livros_emprestados:
                arquivo.write(livro + "\n")

        with open("livros.txt", "a") as arquivo:
            arquivo.write(livro_devolvido + "\n")
        print(f'\nO livro escolhido foi:\n{livro_devolvido}\nDevolvido!\n')          
  
                
    else:
        print('Opção inválida, Escolha um dos Livros Listado')      