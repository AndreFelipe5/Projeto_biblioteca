def emprestimo_livros():
    print("Empréstimo de Livros")

   
    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()
        for lista_livros in livros:
            print(lista_livros.strip())

        livro_emprestado = input('Digite o Numero do Livro')  
        for linha in livros:
            
                
            