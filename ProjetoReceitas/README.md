# Problemas com Ambiente virtual (Leia isso antes de criar seu ambiente virtual python)
    Inicialmente eu estava utilizando o interpretador padrão do python no VsCode, porém na hora de quando criei meu ambiente virtual e ativei
    ele não estava utilizando minhas configurações do ambiente, estava sendo utilizado minha configurações globais, então algumas instalações
    de bibliotecas que havia feito no meu ambiente virtual não estava funcionando, o código acusava que eu não possuia aquela biblioteca mesmo
    ela estando instalada no ambiente virtual ele não estava identificando, pois estava utilizando minha configs globais.

    Para evitar isso, quando você estiver dentro de um arquivo '.py', no canto inferior direito do VsCode irá mostrar a versão do interpretador
    que está utilizando, no meu caso, aqui consta para mim, duas versões:

    > Python 3.11.4 64-bit
    > Python 3.11.4 ('venv':venv)

    A versão que eu estava utilizando inicialmente era 'Python 3.11.4 64-bit', porém estava constando o problema relatado a cima, alterando para a
    versão 'Python 3.11.4 ('venv':venv)' o problema foi resolvido e o meu código passou a usar as configs do meu ambiente virtual, além disso, com
    esse interpretador, o próprio VsCode já ativa automaticamente o ambiente.

# Iniciando nosso Ambiente virtual
    Antes de tudo, lembre-se de criar e ativar seu ambiente virtual, pois é nele que vamos fazer as intalações necessárias para nosso projeto.
    Se o ambiente virtual não estiver ativo, as instalações dos pacotes serão feitas na máquina (geral) e não no ambiente, precisamos isolar
    esses pacotes dentro do nosso ambiente.

    Criar:
    >>>> python -m venv venv

    Ativar (Qualquer um dos três comandos):
    >>>> venv\scripts\activate | .\venv\Scripts\Activate | .\venv\Scripts\Activate.ps1

# A próxima etapa é criar um arquivo .gitignore:
    Projetos como esse vão requerir um gitignore mais robusto, para que alguns arquivos não sejam enviados pro nosso GitHub, recomendo que procure
    algum modelo de arquivo gitignore para projetos Django.

# Agora podemos instalar o django:
    Comando de instalação da distribuição Django (Antes de rodar esse comando observe se o ambiente virtual está ativo)
    >>>> pip install django

    Se você verificar na pasta lib, verá que foi acrescentada pastas referente aos arquivos do Django, além disso, você também pode rodar o comando:
    >>>> pip freeze

    Com esse comando, você obterá a lista de pacotes instalados e as versões de cada pacote.

# Comandos do Django:
    > django-admin --help >>> Esse comando vai listar para você, todos os comandos que o django-admin possui

    > python manage.py --help >>> Esse comando vai listar para você, todos os comandos que o manage.py possui

    > django-admin startproject NomeDoProjeto . >>> Iniciar um Projeto Django
    OBS: use o ponto no final do comando para indicar para o Django criar o projeto na pasta raiz

    > python manage.py runserver >>> Para iniciar nosso projeto no servidor local (servidor de desenvolvimento)

    > django-admin startapp NomeDoApp >>> Iniciar um App Django

    OBS: Após a criação do nosso projeto, passaremos a utilizar o manage.py ao invés do Django-admin, eles dois são bem parecidos, porém o manage.py carrega as informações do nosso projeto.

# Vamos criar nosso primeiro App
    Nesse projeto, nosso App se chamará recipes (receitas), pois nosso site será um site de receitas.
    >>>> python manage.py startapp recipes
    
    O comando a cima vai criar nosso app. Perceba que foi criado uma pasta com o nome do nosso app após rodar o comando a cima, essa pasta já vem com alguns arquivos que iremos utilizar ao longo do projeto.

    Não esqueça de passar o nome do seu app dentro do arquivo settings do projeto!!

# URLS | Views | App > Configs (Preparando e configurando o ambiente)
    Agora que temos nosso projeto e App criados, vamos criar seguir alguns passos de configuração de Urls e Views:

    > Crie um arquivo 'urls.py' dentro da pasta do App

    > Crie dentro da pasta do App uma pasta chamada 'templates', a mesma servirá para armazenar nossos templates HTML

    > Crie dentro da pasta do App uma pasta chamada 'static', a mesma servirá para armazenar nossos arquivos estáticos (CSS, IMG, JS)

    > Criar pasta/arquivo 'base_static/global/css/style.css' e configura-la no settings.py (STATICFILES_DIRS)

    > Criar pasta 'base_templates/global' e configura-la no settings.py (TEMPLATES DIRS)

    > Configurar o STATIC_ROOT no arquivo settings.py

    > No arquivo 'settings.py' do projeto, adicione o nome do nosso App criado dentro da lista 'INSTALLED_APPS'

    > Dentro do nosso arquivo 'views.py' do nosso App, vamos criar nossas views, definidas funções que retornam um template HTML
    | Obs: Utilizaremos a função 'render' para renderizar nossos templates | Ex: return render(request, 'recipes/pages/index.html', context=utils)

    > Dentro do arquivo 'urls.py' criado na pasta do nosso App, vamos importar o módulo 'path' e as nossas views
    | Ex: from django.urls import path | from recipes.views import home

    > Importe o módulo 'include' dentro do arquivo urls.py do projeto
    | Ex: from django.urls import path, include

    > Dentro do 'urls.py' do App, precisamos criar uma lista chamada 'urlpatterns' e passar dentro dela o path das nossas views
    | Ex: path('', home) |> (Rota, NomeDaView)

    > Agora vamos configurar o 'urls.py' do projeto, passando o path com nossas rotas criadas no 'urls.py' do App
    | Ex: path('', include('recipes.urls'))

# Views e Função render
    Para que possamos renderizar um template HTML, vamos retornar dentro de nossas views a função "render". Essa função pede obrigatoriamente 2 argumentos,
    o primeiro deles é o "request" e o segundo é o nome do template HTML, além disso existem outros argumentos que podem ser passados mas não são obrigatórios.
    Um deles é o context, que possibilita inserirmos um dicionário para que possamos utilizar seus valores dentro de um template HTML e utilizar como "variaveis".

    Exemplo de utilização:
        Dentro da View >
            | context = {'nome': 'David'}

        Dentro do HTML >
            | {{nome}}

    Com isso você conseguirá puxar o valor do dicionário e exibir dentro da sua página HTML.

# Ícones em nossas páginas
    Podemos usar o Font-Awesome para colocar ícones no nosso arquivo HTML e exibir na nossa página

    No site https://cdnjs.com/libraries/font-awesome/5.15.4 você encontrará as versões e os códigos para importar no seu arquivo HTML
    e no site https://fontawesome.com/icons você encontrará os ícones e os códigos para usa-los.

# Emmet Abreviation
    Vamos supor que eu queira criar 10 divs iguais de uma única vez, sem precisar digitar 10x, eu posso fazer assim:

    >>>> div*10

    Após pressionar enter, ele vai criar 10 div de uma única vez para você, o mesmo vale para qualquer outra tag e até mesmo se quiser criar com classe definida. ex:

    >>>> div.temp*10

# Arquivos Estáticos
    Arquivos estáticos são arquivos que são entregues exatamente como estão salvos. Esses arquivos quase não sofrem alterações, por isso, o navegador pode salvá-los em cache para que o conteúdo da página carregue mais rapidamente para o usuário final. Alguns provedores de Internet também adicionam servidores no meio da rede que também podem fazer cache desse arquivos, assim o próprio provedor economiza sua banda de Internet externa.

    Frequentemente, sites adicionam seu conteúdo estático em CDNs (Content Delivery Network) que são servidores otimizados para entrega de arquivos estáticos tanto em velocidade de entrega quando em manter os arquivos na localização mais próxima do usuário final.

    Nós usamos CDN quando adicionamos "font-awesome" ao nosso site, lembra? O Django consegue lidar com arquivos estáticos no seu servidor ou em CDNs.

    Alguns tipos de arquivos que podem ser considerados estáticos: imagens, vídeos, HTML, CSS, JavaScript, arquivos para download e assim por diante.

    Vamos entender melhor como configurar os arquivos estáticos do nosso site Django ao longo das aulas dessa seção.

    Documentação do Django sobre arquivos estáticos: https://docs.djangoproject.com/en/4.2/howto/static-files/

    É importante entender como carregar arquivos estáticos utilizando funcionalidade do Django, pois vamos mover nossos static files para uma pasta chamada 'static'
    para melhor organização, essa pasta, quando criada dentro da pasta do App, o próprio django já consegue identificar, assim como a pasta 'templates', qualquer pasta
    criada fora da pasta do App é necessário informar no 'settings.py' para que o Django consiga buscar os arquivos.

    Seu projeto provavelmente também terá recursos estáticos que não estão vinculados a um aplicativo específico. Além de usar um static/diretório dentro de seus aplicativos, você pode definir uma lista de diretórios (STATICFILES_DIRS) em seu arquivo de configurações onde o Django também procurará por arquivos estáticos. Por exemplo:

    STATICFILES_DIRS = [
        BASE_DIR / "static",
        "/var/www/static/",
    ]

    Consulte a documentação da STATICFILES_FINDERS (https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATICFILES_FINDERS) para obter detalhes sobre como staticfiles localiza seus arquivos.

# STATIC_ROOT e collectstatic
    Enquanto estamos em desenvolvimento, não há problema em usar nossos arquivos estáticos dessa maneira, dentro da pasta do App ou até mesmo na raiz. Porém quando nosso
    projeto for para produção, precisaremos fazer algumas configurações de segurança e após isso, os nossos arquivos estáticos não serão mais buscados pelo Django, devido
    isso vamos precisar configurar e entender o 'STATIC_ROOT' e o comando 'collectstatic'

    Dentro do arquivo settings.py, vamos passar a variável " STATIC_ROOT = BASE_DIR / 'static' "
    com isso o STATIC_ROOT já estará configurado, esse comando, basicamente, configura ONDE e o NOME da pasta a ser criada com nossos arquivos estáticos
    nesse caso, nossa pasta será criada na Raiz com o nome de 'static'

    Após isso, quando formos entrar em produção, vamos rodar o comando:
    
    >>>> python manage.py collectstatic

    E esse comando vai coletar todos os arquivos estáticos do nosso projeto, e vai criar a pasta configurada com STATIC_ROOT e jogar esse arquivos dentro dessa pasta
    para que a gente possa usar esses arquivos quando entrar em produção.

# Banco de dados (Models)

    # SOBRE IMAGENS
    Para trabalhar com imagens no banco de dados, você precisará instalar a biblioteca 'pillow'
    >>>> pip install pillow

    Assim que você fizer sua primeira tabela, se ela conter um campo para imagens, ao tentar subir o servidor o django irá solicitar que instale essa biblioteca.

    # SOBRE MIGRATIONS
    Assim que você relizar alterações no banco de dados, como a criação de uma tabela ou até mesmo a edição de uma tabela, você precisará dos comandos:
    >>>> 1| python manage.py makemigrations
    >>>> 2| python manage.py migrate

    Os comandos são executados na ordem a cima, o primeiro cria as migrações e o segundo faz a aplicação no banco de dados, caso o Django informe no terminal alguma mensagem em vermelho, falando sobre 'migrations', é porque existem migrações que não foram aplicadas, basta rodar o segundo comando (migrate).

    Quando criamos nosso projeto Django e rodamos o servidor pela primeira vez, ele mostra essa mensagem informando das migrações que precisam ser aplicadas, isso acontece
    devido o Django criar as tabelas do Admin e as migrações ficam pendentes de aplicação, basta rodar o segundo comando (migrate) que a mensagem sairá.

    Isso é necessário para fazer a sinconização do seu código com a base de dados e atualizar e aplicar as alterações realizadas.
    Sempre que houver migrações a serem aplicadas, o django te avisará no terminal quando você subir o servidor, para resolver, basta rodar o comando 'migrate'.
    Sempre que você rodar o comando makemigrations, dentro da pasta 'migrations' do App, será criado um arquivo com as informações da migração realizada.

    # SOBRE ADMIN E MODELS
    Para que meus models (banco de dados) apareçam na minha área administrativa, é necessário registrar eles no arquivo 'admin.py' do App.

    OBS: Quando criar suas tabelas, não é necessário criar um campo 'id' pois o Django faz isso automaticamente para você no momento em que você rodar o makemigrations.

# Super Usuário (superuser)
    O Django possui uma área de administrador, para acessar essa área, basta colocar na url do seu site '/admin'
    porém você não irá conseguir logar, pois não possui um usuário registrado, devido isso vamos criar um.

    Para criar um super usuário (Usuário com todos os privilégios de admin) você precisa rodar o comando:
    >>>> python manage.py createsuperuser

    Assim que você fizer isso, no próprio terminal, será solicitado alguns dados para a criação do seu usuário administrador:
    > Nome de usuário
    > E-mail
    > Senha (2x)

    Com esse dados você já pode acessar a área de admin do Django.