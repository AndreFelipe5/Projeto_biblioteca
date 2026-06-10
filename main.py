import cadastro_users
import cadastro_livros
import emprestimo_livros
import devolucao_livros
import relatorio
import editar_livro

def menu():
    while True:
        print('Biblioteca LP')

        print(' 1 - Cadastrar Usuário')
        print(' 2 - Cadastrar Livro')
        print(' 3 - Editar Livros')
        print(' 4 - Emprestimo de Livros')
        print(' 5 - Devolução de Livros')
        print(' 6 - Relatorio da Biblioteca')
        print('7 - Sair')

        menu_opcoes = input('Digite a opção desejada: ')

        if menu_opcoes == '1':
             cadastro_users.cadastrar_usuario()

        elif menu_opcoes == '2':    
              cadastro_livros.cadastrar_livro()

        elif menu_opcoes == '3':
            editar_livro.editar_livros()

        elif menu_opcoes == '4':
             emprestimo_livros.emprestimo_livros()

        elif menu_opcoes == '5':
            devolucao_livros.devolver_livro()

        elif menu_opcoes == '6':
            relatorio.relatorio_biblioteca()

        elif menu_opcoes == '7':
            print('saindo...')
            break   

        else:
           print('Opção inválida.')

            
menu()