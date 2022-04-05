# Deploy e CI/CD

1. O que é deploy:
    * Como fazer para outras pessoas vizualizarem o projeto:
        * Fazendo um deploy.
        * Um deploy é quando, subimos uma aplicação que está no ambiente de desenvolvimento para o ambiente de produção.
    * Todos os projetos precisam ter um ambiente de produção e um de desenvolvimento.
    * As versões que sobem para o ambiente de produção precisam ser estáveis.    
    * Deploy manual é extremamente cansativo e custoso.   
    * Utilizando o heroku precisamos fazer apenas um git push, para que o repositório já seja enviado para a produção.

2. Fazendo deploy do projeto no Heroku:
    * Inicialmente precisamos instalar o cli do heroku.
    * Depois já no projeto precisamos fazer um heroku login, para acessarmos nossa conta heroku no projeto.
    * Precisamos fazer um heroku create, para criarmos um repositório para o projeto.
    * Precisamos criar um requirements.txt na raiz do projeto para termos tudo que é necessário.
    * Fazemos com que esse requirements.txt herde do requirements/common.txt.
    * Precisamos criar um arquivo de configurações para o heroku.
    * Nesse arquivo de configuração do heroku, chamamos a biblioteca django_on_heroku e dela utilizamos o settings(locals()), para que a própria lib facilite a configuração dos servidores no heroku.
    * Podemos configurar o arquivo que iremos passar utilizando o comando "heroku config:set DJANGO_SETTINGS_MODULE=marked.settings.heroku".
    * Ao usarmos o comando heroku config, vamos ver uma lista das variáveis que configuramos.
    * Precisamos configurar uma secret key para o heroku, utilizamos a variável de ambiente para facilitar isso.
    * Precisamos criar um arquivo runtime.txt, para que possamos setar que é um programa em python.
    * Precisamos colocar nesse arquivo a versão do python que queremos utilizar.
    * É necessário ter também um arquivo chamado Procfile.
    * Precisamos colocar no arquivo Procfile as seguintes coisas:
        * release: "comando para realizar algo após o deploy" -> python manage.py migrate
        * web: "informa que é uma aplicação web" -> gunicorn marked.wsgi

3. Interagindo com nosso app em produção:
    * Utilizamos heroku logs, para verificar as requests da aplicação em produção.
    * Precisamos utilizar o comando heroku run bash, para acessarmos outra máquina, para que possamos criar um super usuário.
    * Podemos ver as variáveis de ambiente configuradas pelo comando env.
    * Precisamos adicionar nas urls principais as urls do drf, para conseguirmos mexer com as validações na web na aplicação rodando.
    * Precisamos criar uma view para verificarmos a "saúde" do nosso projeto. Geralmente chamada de helthcheck.

4. Variáveis e ambientes no Postman:
    * 