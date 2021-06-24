# Trabalho de Grafos

**Antes de mais nada, é necessário criar um ambiente virtual e instalar as dependências de pacotes...**

```bash
# ambiente virtual
python -m venv venv
# dependências de pacotes
pip install -r requirements.txt
```

## Estrutura do projeto

```bash
├── assets
│   └── graphEnter.csv   # Arquivo para entrar com seus grafos
│   └── K5.csv          
│   └── n3e2.csv
│   └── n4e5.csv
│   └── weight.csv
├── graphs
│   └── bellmanFord.py
│   └── bfs.py
│   └── dijkstra.py
│   └── kruskal.py
│   └── headMinimum.py  # Algoritmo necessário para o algoritmo de dijkstra funcionar
│   └── infoGraph.py    # Arquivo com algumas informações basicas do grafo, só é utilizado no mainGraph.py
├── README.md
└── mainGraph.py
└── requeriments.txt # Arquivo com os pacotes utilizados
```


## Entrando com seu grafos

Em nossas implementações utilizamos apenas matriz de adjacências, ou seja, é necessário passar apenas matrizes para os algoritmos funcionarem,entre com sua matriz no arquivo ```graphEnter.csv``` 

**Lembre-se de manter uma linha inicial, pois pelo uso do pandas, setamos que a primeira linha é para titulos das colunas**

### Exemplo

```csv
A;B;C;D;E;F;G;H;I;J;K
0;8;5;7;0;0;0;0;0;0;0
8;0;0;0;6;2;0;0;0;0;0
5;0;0;0;4;5;0;0;0;0;0
7;0;0;0;0;4;2;0;0;0;0
0;6;4;0;0;0;0;4;0;0;0
0;2;5;4;0;0;0;4;2;4;0
0;0;0;2;0;0;0;0;2;4;0
0;0;0;0;4;4;0;0;0;0;4
0;0;0;0;0;2;2;0;0;0;5
0;0;0;0;0;4;4;0;0;0;4
0;0;0;0;0;0;0;4;5;4;0
```

É necessário ter essa linha inicial que no exemplo é: ```A;B;C;D;E;F;G;H;I;J;K```

## Algoritmos

- Dijkstra
- Bellman Ford
- Kruskal
- BFS

## Arquivo mainGraph.py

Este arquivo é uma ajuda para rodar todos os algoritmos implementados, ao executa-lo ele explicará seu funcionamento. Todos os algoritmos possuem no final uma parte de teste, caso deseje executa-los individualmente, basta entrar com a matriz no arquivo ```graphEnter.csv``` e executar o algoritmo 

## PS: O algoritmo de dijkstra usa outro arquivo para seu funcionamento, lembre-se de ler o comentário no inicio do arquivo caso execute ele isoladamente
