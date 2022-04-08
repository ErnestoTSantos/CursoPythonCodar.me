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
    * Precisamos utilizar o comando heroku run bash, para acessarmos uma máquina virtual, para que possamos criar um super usuário.
    * Podemos ver as variáveis de ambiente configuradas pelo comando env.
    * Precisamos adicionar nas urls principais as urls do drf, para conseguirmos mexer com as validações na web na aplicação rodando.
    * Precisamos criar uma view para verificarmos a "saúde" do nosso projeto. Geralmente chamada de helthcheck.

4. Variáveis e ambientes no Postman:
    * Podemos ficar trocando os links para fazer as requisições, mas não é a melhor forma.
    * Podemos ter variáveis no postman.
    * Precisamos configurar dois ambientes diferentes, para podermos utilizar as variáveis deles nas requests.
    * Para usarmos as variáveis, na request colocamos o nome da variável em questão.
    * Precisamos selecionar o ambiente que queremos usar, o "environment".
    * Para salvarmos as variáveis, precisamos persistir elas.
    * Podemos definir como padrão a autorização a ser utilizada.

5. Release e Rollback:
    * Release é um incremento de versão do software, trazendo atualizações e novas possibilidades.
    * Podemos visualizar os releases da nossa aplicação usando o comando "heroku releases".
    * Rollback é retornar a aplicação para uma versão em que o código estava funcionando.
    * Para fazer o rollback usamos o comando "heroku rollback v(número da versão)".
    * Os rollbacks, são uteis para que possamos recuperar possiveis problemas subidos para a produção.

6. Gerando backups do banco de dados:
    * Ao fazermos um rollback, os dados do db não são retornados.
    * O heroku nos permite fazer backups, pelo comando "heroku pg:backups:capture --app drf-api-codar".
    * Podemos verificar as informações do projeto pelo comando "heroku apps:info".
    * Podemos verificar os backups e restores, pelo comando "heroku pg:backups".
    * Para restaurarmos as informações dos backups do db, utilizamos o comando "heroku pg:backups:restore".
    * Podemos agendar a nossa aplicação, para fazer backups diários, para que possamos evitar grandes perdas caso seja necessário fazer um restore.
    * Para agendarmos esses backups diários, utilizamos o comando "heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Sao_Paulo' --app drf-api-codar".
    * Realizar os backups demonstram uma maturidade com os códigos, faz com que sejamos vistos com outros olhos pelos recrutadores.

7. Criando o ambiente de homologação:
    * É comum as empresas criarem um abiente chamado de staging. Esse ambiente é um intermédio entre o ambiente de desenvolvimento e produção.
    * É importante que os dados sejam os mais próximos possíveis entre o ambiente de staging e o de produção.
    * As informações vão primeiro para o ambiente staging, para serem validadas, para depois irem para a produção.
    * Precisamos criar um outro ambiente, utilizando o comando "heroku create --remote staging".
    * Ao criarmos esse outro ambiente, o git irá poder fazer push para ambos, tanto o de produção quanto o de staging.
    * Podemos renomear os remotes pelo comando "git remote rename 'old name' 'new name'"
    * Precisamos configurar as variáveis de ambiente também.
    * Nesse caso como temos muitos remotes, precisamos escrever qual o remote que desejamos utilizar para fazer o set das coisas.
    * Para copiar um banco de dados para outra aplicação, ex a de staging precisamos rodar o comando "heroku pg:backups:restore sushi::b101 DATABASE_URL --app sushi-staging"..

8. Deploy e CI-CD:
    * CDD = Continuous Deployment/Delivery:
        * Continuous deployment significa que podemos fazer deploys continuos.
        * Continuous delivery significa que o processo de entrega da aplicação para outro ambiente também é continuo.
    * Para ajustarmos precisamos criar um novo repositório no git.
    * Podemos ajustar no próprio site do heroku, para que o projeto fique linkado para quando realizamos alterações nele já irem para a produção.
    * Para que os deploys automáticos aconteçam, precisamos fazer com que o git conect com o heroku.

9. Fluxo de trabalho com Git(Git Workflow):
    * Como o git poderá nos auxiliar com o desenvolvimento de software.
    * Feature branching:
        * Criamos uma ramificação de acordo com a feature que estamos implementando.
    * É um estilo que facilita a colaboração e ter a noção de qual código está sendo utilizado no momento.
    * É uma maneira de de manter os códigos do staging mais estáveis.

10. Integração Contínua com GitHub Actions:
    * Continuous integration: É quando fazemos com que os nossos testes, estilizações de códigos e padrões estejam aplicados.
    * Podemos ter a criação do arquivo de maneira mais rápida e fácil pelo próprio repositório, na parte de actions.
    * Podemos verificar possíveis problemas no actions.
    * O próprio github actions faz a verificação, para saber se o sucesso está igual ou acima do que configuramos no pytest.ini.
    * Todas as vezes que fizemos o push, esses testes serão realizados.
    * Podemos ter multiplos checks.
    * Podemos configurar para que todos os checks tenham a obrigatoriedade de passar
    * Precisamos ir em settings, branches e add rule.
    * Podemos criar um status badge, para demonstrar a "qualidade" do nosso código.

11. Revisão:
    * Deploys automáticos.
    * Testes automáticos.
    * Backups e backups agendados, para evitarmos grandes perdas.
    * Releases/rollbacks.
    * Software development life cycle(sdlc):
        * Ambientes de desenvolvimento, staging, produção...
        * Caminhos para a produção do software.
