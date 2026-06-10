def emprestimo_livros():
    print("Empréstimo de Livros\n")

   
    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]
    print("Lista de Livros:\n ")
    for i, livro in enumerate(livros, start=1):
        print(f'{i} - {livro}\n')

    livro_escolhido = int(input('Digite o número do Livro para Empréstimo: '))

    if 1 <= livro_escolhido <= len(livros):
        livro_emprestado = livros.pop(livro_escolhido - 1)

        with open("livros.txt", "w") as arquivo:
            for livro in livros:
                arquivo.write(livro + "\n")

        with open("livros_emprestado.txt", "a") as arquivo:
            arquivo.write(livro_emprestado + "\n")
        print(f'O livro escolhido foi:\n{livro_emprestado}\n  Emprestado com sucesso!')          
  
                
    else:
        print('Opção inválida, Escolha um dos Livros Listado')        