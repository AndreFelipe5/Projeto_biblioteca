Biblioteca LP

Projeto desenvolvido como avaliação da disciplina de Lógica de Programação, ministrada pela Professora Viviane.

Descrição

O sistema simula o gerenciamento básico de uma biblioteca, permitindo o cadastro de usuários e livros, realização de empréstimos, devoluções, edição de livros e geração de relatórios.

As informações são armazenadas em arquivos ".txt", permitindo a persistência dos dados entre as execuções do programa.

Funcionalidades

Usuários

- Cadastro de usuários

Livros

- Cadastro de livros
- Edição de livros
- Consulta de livros disponíveis

Empréstimos

- Empréstimo de livros
- Devolução de livros

Relatórios

- Visualização de livros disponíveis
- Visualização de livros emprestados

Conceitos Aplicados

- Variáveis
- Estruturas condicionais ("if", "elif", "else")
- Estruturas de repetição ("while" e "for")
- Funções
- Módulos
- Manipulação de arquivos TXT
- Listas
- "enumerate()"
- CRUD (Create, Read, Update e Delete)

Estrutura do Projeto

BibliotecaLP/
│
├── menu.py
├── cadastro_users.py
├── cadastro_livros.py
├── editar_livros.py
├── emprestimo_livros.py
├── devolucao_livros.py
├── relatorio.py
│
├── usuarios.txt
├── livros.txt
└── emprestados.txt

Como Executar

Execute o arquivo principal do projeto:

python menu.py

Menu do Sistema

1. Cadastrar Usuário
2. Cadastrar Livro
3. Empréstimo de Livros
4. Devolução de Livros
5. Editar Livro
6. Relatório da Biblioteca
7. Sair

Objetivo Acadêmico

Este projeto foi desenvolvido com o objetivo de aplicar os conhecimentos adquiridos na disciplina de Lógica de Programação, explorando conceitos fundamentais da linguagem Python e a construção de sistemas utilizando arquivos para armazenamento de dados.

Autor

André Felipe

Disciplina

Lógica de Programação

Professora: Viviane