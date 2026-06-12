import cadastro_livros
import emprestimo_livros
import devolucao_livros
import relatorio
import editar_livro



def menu():
    while True:
        
        print('<=====> Biblioteca LP <=====>\n')
       
        print(' 1 - Cadastrar Livro')
        print(' 2 - Editar Livros')
        print(' 3 - Emprestimo de Livros')
        print(' 4 - Devolução de Livros')
        print(' 5 - Relatorio da Biblioteca')
        print(' 6 - Sair')

        menu_opcoes = input('\nDigite a opção desejada: ')

        if menu_opcoes == '1':
            cadastro_livros.cadastrar_livro()
        
        elif menu_opcoes == '2':
            editar_livro.editar_livros()

        elif menu_opcoes == '3':
             emprestimo_livros.emprestimo_livros()

        elif menu_opcoes == '4':
            devolucao_livros.devolver_livro()

        elif menu_opcoes == '5':
            relatorio.relatorio_biblioteca()

        elif menu_opcoes == '6':
            print('saindo...')
            break   

        else:
           print('Opção inválida.')

            
menu()