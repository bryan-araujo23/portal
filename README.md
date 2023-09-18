# portal

Mini Sistema Q&amp;A feito em Python/Django

Mini Sistema Q&A (forum) de perguntas e respostas  feito com Python/Django



Primeiros requisitos

- Sistema Q&A / identidade visual

  Simples Utilizando Bootstrap



- Linguagem do site

  PT-BR



- Principal objetivo

  Exibir perguntas e respostas de cada postagens feita pelo usuario.


- Controle de acesso

  Usuários podem postar suas perguntas e respostas.


- Registro de usuários

  Cadastro livre porem com aprovação do administrador

PORTAL(Perguntas e Respostas): muito parecido com um help desk. Principal Objetivo: Exibir perguntas e respostas de cada postagens feita pelo usuario, onde teremos um controle de acesso: cada usuário pode postar suas perguntas e respostas. Registro de usuários: Cadastro livre, porém com aprovação do administrador. Aplicação inicia-se com a tela de Registro e Login, onde usuário aprovados pelo ADMINISTRADOR da aplicação será direcionado para pagina inicial com todas as perguntas e resposta. Após o cadastro usuário inserir seu post, pode pesquisar, pode filtrar pela barra de pesquisa ou por tags os posts. Lá ele terá detalhes da postagem: foto, dia e hora e comentários das postagem. Cada Perfil do usuario contém: foto, ocupação e descrição sobre usuário.

*Como Executar*

1 - Crie Seu ambiente virtual: python -m venv venv
2 - Ative: venv/Scripts/activate
3 - Entre na pasta do projeto: cd portal
4 - pip install -r requirements.txt
5 - No terminal execute este comando, depois copie a chave gerada: python generate_secret_key.py
6 - Copie e cole o arquivo env_exemplo: ctrl-c ctrl-v  na pasta env_exemplo
7 - renomeie o arquivo env_exemplo_copy: para .env
8 - adc o formato do arquivo no .gitignore
9 - Instale a seguinte lib: python -m pip install Pillow
10 - No termional, execute este comando: python manage.py makemigrations
11 - No termional, execute este comando: python manage.py migrate
12 - Crie um super usuário python manage.py createsuperuser
13 - Seu email: email
14 - Seu Username: Username
15 - Seu primeiro nome: First name
16 - Last name
17 - type user: ad
18 - User Active: True
19 - Sua senha: Password
20 - Depois rode o servidor: python manage.py runserver
    

