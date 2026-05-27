import re

def validar_email(email):
    
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None


def cadastrar_usuario():
    print('Cadastro de Usuário')
    nome = input('Nome: ')
   

    email = input('Email: ')
    if not validar_email(email):
      print('inválido, tente novamente.')
      return  

   
    with open('usuarios.txt', 'r') as arquivo:
       usuarios = arquivo.readlines()

    email_duplicado = False
        
    for linha in usuarios:
        dados = linha.strip().split(';')
        if email in dados:
            print('Email já cadastrado, tente novamente.')
            email_duplicado = True
            break

    if not email_duplicado:
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f'{nome};{email}\n')
            print('Usuário cadastrado com sucesso!')
    
