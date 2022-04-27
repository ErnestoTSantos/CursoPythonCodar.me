# Resumo do módulo 18
## Tarefas assíncronas com Celery 18

1. Gerando relatórios em CSV:
    * É comum exportarmos consultas que são muito longas em arquivos csv.
    * Precisamos importar a biblioteca csv.
    * Ao usarmos o csv, não utilizaremos mais as generics na view em questão.
    * Precisamos refatorar a view, para uma fbv, para verificarmos qual o padrão que está sendo requerido pelo usuário.
    * Precisamos utilizar o HttpResponse e alterar manualmente o estilo e o que é o conteúdo.
    * Precisamos escrever com o writer do csv.
    * Construimos dinamicamente o nosso csv.
    * Ao utilizarmos no navegador, o próprio navegador irá fazer o dowload do arquivo.

2. Delegando tarefas para workers(Tarefas assíncronas):
    * Gargalo é quando nos referimos de operações que demoram mais, como a consulta no db e a geração do csv.
    * Workers é um processo separado que irá realizar uma tarefa mais custosa de maneira assíncrona.
    * O servidor irá delegar a tarefa para o worker e o cliente receberá um 200.
    * O worker enviará um e-mail para o cliente com o csv.
    * SMTP é um protocólo para envio de e-mails.
    * Precisaremos do Celery, para gerenciar a fila de tarefas.
    * Precisamos também do Redis, para armazenar a chave e o valor dos elementos, ele é um intermediador das mensagens. Pode ser utilizado com um db para os resultados das respostas do worker.
    * O Celery pode ser usado para um results back-end.

3. Setup do Redis:
    * Precisamos instalar o Redis, no meu caso no wsl2
    * O link do Redis é: https://redis.io/docs/getting-started/installation/install-redis-on-windows/
    * Para iniciarmos o Redis utilizamos o comando: "sudo service redis-server start"
    * Para acessarmos o db, utlizamos o comando: "redis-cli"
    * Todos os comandos devem ser realizados no wsl/ubuntu.

4. Primeira tarefa assíncrona com Celery:
    * Precisamos intalar o celery, mas de uma maneira diferente. Pelo comando: 'pip install "celery[redis]"', para que o celery já saiba com o que irá trabalhar.
    * Precisamos criar um arquivo na pasta do projeto e não na raiz chamado: celery.py
    * Utilizamos decorators para ajustarmos que a função deve ser assíncrona.
    * Para executarmos o celery utilizamos o comando: "celery -A marked worker -Q celery --loglevel=INFO" ou "celery -A marked worker -P solo --loglevel=INFO".
    * O -A do comando remete à aplicação.
    * Utilizamos o método delay(), na função que queremos que o celery atue. Nesse caso receberemos o identificador da tarefa que foi executada.
    * O celery nos permite performar outras ações quando utilizamos ele.
    * Podemos definir o backend no redis da mesma maneira que configuramos o broker.

5. Gerando relatório em uma task:
    * Precisamos criar o arquivo tasks.py
    * Nesse arquivo vamos declarar as tarefas de maneira assíncrona.
    * Não precisamos utilizar o HttpResponse para fazer com que seja retornada a chave do arquivo.
    * Utilizamos o StringIO, para receber os elementos do output.
    * Para registrar as tarefas de maneira que o worker consiga rodar elas, utilizamos "app.autodiscover_tasks()"
    * Precisamos dizer qual a "configuração" que o celery precisa usar.
    * Precisamos utilizar o os com o setdefault, para organizarmos essa questão da configuração que o celery irá utilizar.
    * O autodiscover, precisa visualizar que é uma aplicação django.

6. Enviando e-mail com anexo:
    * Precisamos arrumar primeiramente a variável EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' ou EMAIL_BACKEND='django.core.mail.backends.smpt.EmailBackend'.
    * SMTP é o servidor que utilizamos para fazer o protocolo de envio de emails.
    * MailHog é o "programa" que utilizaremos para fazer o envio dos emails.
    * MailHog é basicamente um servidor usado para o desenvolvimento para facilitar a visualização dos emails.
    * Além disso precisamos passar o EMAIL_HOST='0.0.0.0'.
    * E precisamos dizer a porta em que ele está sendo executado pela variável EMAIL_PORT='1025'
    * Precisamos usar o EmailMessage do django par aajustarmos o arquivo.
    * Precisamos utilizar attach para nomearmos o arquivo, receber o tipo e o valor a ser enviado.
    * Precisamos usar o send para enviar o email.

7. Configurando envio de e-mail em produção:
    * Podemos colocar os valores do nossos redis nas variáveis de ambiente.
    * Precisamos colocar no arquivo de base settings e criar as variáveis para configurar o celery.
    * Algumas das variáveis são, CELERY_BROKER_URL e CELERY_RESULT_BACKEND.
    * Podemos fazer toda a base de valores para o redis pelas variáveis de ambiente.
    * Precisaremos ter uma conta no SendGrid, para que possamos fazer o link com o enviador de emails.
    * A senha do sendgrid deve ser posta em outro local, por ser uma variável sensível.
    * Para enviarmos e-mails para o smtp no django, com o windows precisamos utilizar no EMAIL_HOST a palavra localhost, para que ele possa fazer a comunicação com o MailHog. 

8. Testando o envio de e-mails:
    * O método por padrão faz duas coisas.
    * Precisamos quebrar essa tarefa em multiplas tarefas... Para dividirmos as responsábilidades do código e podermos fazer os testes de maneira correta.
    * As funções chamadas não precisam ser celery tasks.
    * Podemos testar com o TestCase os emails.
    * Link para a demonstração dos testes: https://docs.djangoproject.com/pt-br/4.0/topics/testing/tools/#email-services.

9. Deploy do celery e redis no heroku:
    * Precisamos modificar os requirements e o Procfile.
    * No Procfile, precisamos fazer a iniciação do worker.
    * Precisamos fornecer o redis para o heroku, utilizamos o comando "heroku addons:create heroku-redis --remote production", para fazer isso, precisamos ter elementos pagos no heroku.
    * Podemos colocar como uma variável de ambiente o e-mail de quem irá enviar para os usuários. Para evitar que seja visivel para outras pessoas o e-mail que está enviando e ter mais segurança.
