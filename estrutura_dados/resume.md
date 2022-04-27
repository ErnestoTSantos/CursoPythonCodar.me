# Estrutura de dados

* Podemos utilizar um laço for para verificar elementos de um em um, ou podemos fazer um for gerando um elemento randomico, verificando. O problema do elemento randomico, é que ele pode ser o primeiro, ou rodar infinitamente o código.
* Bio-O seria uma escala para buscas lineares, onde podemos saber qual seria o pior caso encontrado para a resolução de um programa.
* Podemos utilizar uma lista binária, para encontrarmos os elementos. Neste caso a forma que os dados foram passados, influência diretamente na forma de procurar.

# Busca binária:
    * A melhor forma de armazenarmos elementos nas listas é ordenadamente, para que possamos deixa-la organizada e possamos dividir ela nos pedaços.
    * A melhor forma de encontrarmos elementos, é chutando no valor que está no meio da lista.
    * Podemos utilizar o O(logn) para chegarmos a um elemento de uma lista, dependendo de seu tamanho, precisamos adicionar apenas um passo a mais.
    * Precisamos somar o inicio + fim e dividir por 2, assim teremos o meio e poderemos fazer a comparação.

### Modulo timeit, executa um programa várias vezes. Já é um módulo padrão do python, precisamos passar como uma string o código que queremos executar.

### Para fazermos a comparação dos casos, utilizamos geralmente o pior caso das buscas.
### Podemos usar o comando time.perfcounter(), precisamos colocar no início e no fim da execurção.

#### A busca linear é muito mais ineficiente comparada a busca binária, comparando ao pior caso.

#### Podemos fazer tradeoffs, para verificar qual a melhor estrutura para realizar a operação.
    * Comparam o Tempo X Espaço.
    * Legibilidade
