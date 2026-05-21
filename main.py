import cadastros



def menu():
    while True:
        print('Biblioteca')

        print(' 1 - Cadastrar Usuário')
        print(' 2 - Cadastrar Livro')
        print(' 3 - Empréstimo de Livros')
        print(' 4 - Devolução de Livros')
        print(' 5 - Relatório da Biblioteca')
        print(' 6 - Sair')

        menu_opcoes = input('Digite a opção desejada: ')

        if menu_opcoes == '1':
             cadastros.cadastrar_usuario()

        elif menu_opcoes == '2':    
             cadastrar_livro()

        elif menu_opcoes == '3':
             emprestimo_livros()

        elif menu_opcoes == '4':
            devolucao_livros()

        elif menu_opcoes == '5':
            relatorio_biblioteca()

        elif menu_opcoes == '6':
            print('saindo...')
            break   

        else:
           print('Opção inválida.')

            
menu()