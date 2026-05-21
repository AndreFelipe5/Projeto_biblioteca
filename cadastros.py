import re

def validar_email(email):
    
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def cadastrar_usuario():
    print('Cadastro de Usuário')
    nome = input('Nome: ')
   
   
    while True:
        email = input('Email: ')
        if validar_email(email):
            break
        else:
            print('inválido, tente novamente.')
        

    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
    except FileNotFoundError:
        usuarios = []
    for linha in usuarios:
        dados = linha.strip().split(';')
        if len(dados) > 1 and dados[1] == email:
            print('Email já cadastrado!')
            return


    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f'{nome};{email}\n')

    print('Usuário cadastrado com sucesso!')