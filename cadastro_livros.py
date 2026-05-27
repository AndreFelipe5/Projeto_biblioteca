

def cadastrar_livro():
    print('Cadastro de Livros')
    titulo = input('Título do livro: ')


    with open('livros.txt', 'r') as arquivo:
       livros = arquivo.readlines()

    livro_duplicado = False
        
    for linha in livros:
        dados = linha.strip().split(';')
        if titulo in dados:
            print('Livro já cadastrado, tente novamente.')
            livro_duplicado = True
            break

    if not livro_duplicado:
        with open('livros.txt', 'a') as arquivo:
            arquivo.write(f'{titulo}\n')
            print('Livro cadastrado com sucesso!')