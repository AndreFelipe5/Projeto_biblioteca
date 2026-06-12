

def cadastrar_livro():
    print('\n--------> Cadastro de Livros <--------')

    with open('livros.txt', 'r') as arquivo:
       livros = [linha.strip().lower() for linha in arquivo]

    while True:

        titulo = input('\nTítulo do livro: ').strip()

        if titulo.lower() in livros:
            print(f'o Livro {titulo} já está cadastrado, tente novamente.' )

        else:
            with open("livros.txt", "a") as arquivo:
                arquivo.write(f'{titulo}\n')
            print(f'\nO Livro {titulo} foi cadastrado com sucesso!\n')
            break