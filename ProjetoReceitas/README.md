# Comandos Help Django
    >>>> django-admin --help
    >>>> python manage.py --help

# Startando nosso primeiro projeto Django #

# OBSERVAÇÃO
    Antes de tudo, lembre-se de criar e ativar seu ambiente virtual, pois é nele que vamos fazer as intalações necessárias para nosso projeto.
    Se o ambiente virtual não estiver ativo, as instalações dos pacotes de bibliotecas serão feitas na máquina (geral) e não no ambiente.

    >>>> python -m venv venv
    >>>> venv\scripts\activate | .\venv\Scripts\Activate | .\venv\Scripts\Activate.ps1

# A próxima etapa é criar um arquivo .gitignore:
    Coloque no nome do seu ambiente virtual dentro desse arquivo para o git não trackear a pasta do ambiente, pois não queremos subir essas informações
    para o github. Na verdade esse arquivo deve conter muitas outras informações, pois são informações importantes que não queremos enviar para o github
    porém nesse aula aqui vamos deixar assim. Mas criarei uma pasta com o arquivo git com todos os arquivos a serem ignorados.

# Após realizar o processo a cima, vamos rodar o comando:
    python -m pip install setuptools wheel --upgrade

    Utilidade >>>> atualizar algumas ferramentas úteis.

    O Setuptools é uma biblioteca de processos de desenvolvimento de pacotes projetada para facilitar o empacotamento de projetos Python, aprimorando o distutils (distribution utilities, em português "utilitários de distribuição") da biblioteca padrão do Python. Ele inclui: Definições de pacote e módulo Python.

# Agora podemos instalar o django:
    >>>> pip install django

    Se você verificar na pasta lib, verá que foi acrescentada pastas referente aos arquivos do Django.

# Comandos do Django:
    django-admin --help >>> Esse comando vai listar para você no terminal, todos os comandos que o django possui
    django-admin startproject NomeDoProjeto . >>> Iniciar um Projeto Django (OBS: use o ponto final no final do comando para indicar para o Django criar o projeto na pasta raiz)
    python manage.py runserver >>> Para iniciar nosso projeto no servidor local (servidor de desenvolvimento)
    django-admin startapp NomeDoApp >>> Iniciar um App Django

    OBS: Após a criação do nosso projeto, passaremos a utilizar o manage.py ao invés do Django-admin, eles dois são bem parecidos, porém o manage.py carrega as informações do nosso projeto.

# Launch Debug
    É interessante criar um arquivo Json de configurações do debug para o Django, para fazer isso é simples, basta clicar na aba do debug e lá terá instruções e um link, clicando
    no link ele vai abrir o menu de pesquisa, basta clicar em "python" depois em "Django". Basicamente, isso fará com que você possa rexecutar o debug e ele já faça a ativação
    do seu ambiente virtual e já suba o servidor django automaticamente para você, caso queira fazer isso manualmente, não precisa criar esse arquivo json.

# URLS e Views
    Para definir uma URL, precisamos de uma view para retonar para o usuário, no caso desse projeto, como ainda está no inicio estamos testando isso, dentro do arquivo urls da pasta
    do projeto, criando uma view (função) dentro do mesmo arquivo e passando um path (caminho) para o site acessar aquela view, porém depois vamos utilizar nossas views e urls dentr
    dentro do nosso app, em arquivos separados para melhor organização.

# Vamos criar nosso primeiro App
    Nesse projeto, nosso App se chamará recipes (receitas), pois nosso site será um site de receitas.
    >>>> python manage.py startapp recipes
    
    O comando a cima vai criar nosso app. Perceba que foi criado uma pasta com o nome do nosso app após rodar o comando a cima, essa pasta já vem com alguns arquivos que iremos utilizar ao longo do projeto.

    Não esqueça de passar o nome do seu app dentro do arquivo settings do projeto!!!

# Configurações iniciais do meu App
    Primeiramente vou começar transferindo as views que foram criadas no arquivo urls.py do projeto para o arquivo views.py do App.
    Próximo passo é fazer o mesmo para as URLs, vamos criar um arquivo urls.py no nosso App e transferir as urls que criamos lá no projeto para esse novo arquivo do app.
    e dentro do arquivo urls.py do projeto vamos importar o módulo "include" para incluirmos no path o caminho das urls que criamos no App.

    Agora vamos criar nossos templates e rederizar eles nas nossas views! Comece criando uma pasta chamada "templates" e lá dentro crie seus arquivos html.

# Views e Função render
    Para que possamos renderizar um template HTML, vamos retornar dentro de nossas views uma função "render", essa render pede obrigatoriamente 2 argumentos, o primeiro deles
    é o "request" e o segundo é o nome do template HTML, além disso existem outros argumentos que podem ser passados mas não são obrigatórios. Um deles é o context, que possibilita
    inserirmos um dicionário para que possamos utilizar seus valores dentro de um template HTML para exibir na tela.
    Ex de utilização:
    
    Dentro da View >
    context = {'nome': 'David'}

    Dentro do HTML >
    {{nome}}

    Com isso você conseguirá puxar o valor do dicionário e exibir dentro da sua página HTML.

# Font Awesome
    Podemos usar o Font-Awesome para colocar icones no nosso arquivo HTML
    No site https://cdnjs.com/libraries/font-awesome/5.15.4 você encontrar as versões e os códigos para importar no seu arquivo HTML
    e no site https://fontawesome.com/icons você encontrará os icones e os códigos para usa-los.