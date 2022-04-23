# Resumo módulo 19: Docker e Docker Compose

1. O que são Containers:
    * Mais fácil para configurar e instalar a infra estrutura.
    * Garantir um ambiente consistente, ajustando para diferentes sistemas operacionais e versões.
    * Evitar sobrecarregar o cache da máquina do desenvolvedor.
    * As máquinas virtuais tem a desvantagem de serem muito pesadas.
    * Containers é uma versão muito mais leve do sistema, utiliza apenas o que é extremamente necessário.
    * Podemos limitar a memória para as ações.
    * Evitar problemas de não funcionamento.

2. Instalando o docker:
    * Link para instalar o docker: https://docs.docker.com/get-docker/

3. Executando um container Ubuntu:
    * Usamos o comando docker run, para iniciar um container, a partir de uma instalação, ex:"docker run ubuntu".
    * Caso não tenhamos a máquina, o docker irá buscar a máquina e instalar ela.
    * Para que o container continue sendo executado, precisamos utilizar o comando "docker run -i -t ubuntu /bin/bash".
    * Executar o projeto no container e não na máquina.

4. Criando nossa imagem com dockerfile:
    * Imagens podem ser construídas sobre outras.
    * Precisamos criar o arquivo Dockerfile, que é especifico do docker, para construirmos a nossa imagem.
    * Temos que fazer "docker build .", para gerarmos a imagem a partir do nosso dockerfile.
    * Podemos colocar o nome da nossa build ao criarmmos pelo comando "docker build --tag 'nome' ."

5. Criando a imagem do servidor Django:
    * Podemos utilizar a imagem "FROM python:3.10.4-slim-buster", que será uma imagem reduzida do python, fazendo com que menos recursos sejam consumidos.
    * Podemos utilizar os id's dos containers, para iniciarmos eles e também deleta-los.
    * O comando "docker ps" lista todos os containers que estão rodando algo, já o comando "docker ps --all" lista todos os containers.
    * Queremos emular o projeto no container.
    * Para ajustarmos o comando no CMD, para o dockerfile, precisamos colocar todos os elementos em partes de uma lista, não podemos escrever o comando completo em um único espaço dela.

6. Acessando o container a partir do host:
    * Queremos fazer com que a requisição seja roteada para o server do Docker.
    * Para isso precisamos configurar as portas dele para o host principal(computador).
    * Utilizamos o comando "docker run --publish 8000:8000 python-docker", assim fazemos com que todas as requisições feitas para a porta 8000 do meu localhost sejam encaminhadas para o docker.
    * Precisamos fazer o docker rodar na porta 0.0.0.0:8000, para que o docker aceite as requisições do host, que para o docker é outra máquina.
    * Por estamos usando o sqlite3, o docker irá ter acesso ao db.
    * Os valores criados no docker ficam apenas nele, não interferem no db que está na máquina local.

7. Persistindo dados entre containers:
    * O banco de dados não persiste os arquivos por padrão, mantém apenas o que foi copiado.
    * para persistirmos os dados dos containers, precisamos utilizar os volumes.
    * Precisamos usar o comando "docker volume create schedule-db", para criarmos esse volume.
    * Para listarmos os volumes utilizamos o comando "docker volume ls"
    * Fazemos o volume rodar com o comando "docker run -d -p 8000:8000 -v schedule-db:/app python-docker" e a partir disso, tudo o que acontece na pasta /app, fica salvo nesse volume, fazendo com que seja persistido. Esse volume pode ser utilizado por diferentes containers.
    * Utilizar isso, facilita o compartilhamento de dados entre servidores.

8. Autoreload com Docker:
    * Precisamos ter o caminho do projeto.
    * No run, precisamos utilizar o comando "docker run --publish 8000:8000 -v E:\Cursos\Workspace\Codar.meJuntos\drf-api:/app python-docker".
    * Neste caso, o docker estará utilizando o mesmo db que estamos utilizando no host, então todas as modificações ocorrerão nas duas partes.
    * Precisamos configurar o redis.

9. Orquestrando serviços com Docker Compose:
    * Poderiamos criar um container para cada uma das tarefas, mas não é muito fácil e existem maneiras mais práticas para isso.
    * Temos que orquestrar os containers, para isso utilizamos o docker compose.
    * Para ajustar o docker compose, ajustamos por serviços, precisamos criar um arquivo chamado "docker-compose.yml", para fazer as configurações.
    * Para rodar com o docker compose, utilizamos o comando "docker-compose up 'nome do serviço'"
    * Precisamos dizer quais os volumes que serão utilizados.
    * Podemos utilizar a rede criada para conectar em outros serviços.
    * Para configurarmos outros serviços, utilizamos a imagem deles que já é pré existente no docker hub.
    * Os nomes das coisas enquanto estamos criado, não importam muito, o que mais importa é o build e a imagem.
    * Para o celery, o docker indica utilizarmos uma versão do python que já possa fazer a sua instalação e utilização.
    * Para que o celery suba, podemos orquestrar que ele irá depender do app e do redis.
    * Podemos rodar o container também pelo comando "docker-compose up"
    * Vamos ter todos os logs em um único shell.
    * Para fazermos o rebuild, precisamos fazer "docker-compose up --build"
