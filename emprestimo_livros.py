def emprestimo_livros():
    print("\n--------> Empréstimo de Livros <--------\n")

   
    with open("livros.txt", "r") as arquivo:
        livros = [linha.strip() for linha in arquivo]
    print("Lista de Livros disponíveis para Empréstimo:\n ")

    for i, livro in enumerate(livros, start=1):
        print((f'{i} - {livro}'))



        livro_escolhido = int(input('\nDigite o número do Livro para Empréstimo: '))

        if 1 <= livro_escolhido <= len(livros):
            livro_emprestado = livros.pop(livro_escolhido - 1)

            with open("livros.txt", "w") as arquivo:
                for livro in livros:
                    arquivo.write(livro + "\n")

            with open("livros_emprestado.txt", "a") as arquivo:
                arquivo.write(livro_emprestado + "\n")
            print(f'\nO livro escolhido foi: {livro_emprestado}\n\nLivro emprestado com sucesso!\n')          
            break
                
        else:
            print('\nOpção inválida, Escolha um número dos Livros Listado\n')
              