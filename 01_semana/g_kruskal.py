import matplotlib.pyplot as plt
import networkx as nx
import heapq  # Usado para a fila de prioridade do Dijkstra

def add_vertice(grafo, num_vertice):
    for _ in range(num_vertice):
        vertice = input("Vértice: ")
        if vertice not in grafo.nodes:
            grafo.add_node(vertice)
            print(f'Vértice {vertice} adicionado.')
        else:
            print(f'Vértice {vertice} já existe.')

def add_aresta(grafo, num_aresta):
    print('Adicione as arestas no formato "v1 v2 peso" (sem aspas, separados por espaço: a b 4)')
    for _ in range(num_aresta):
        try:
            v1, v2, peso = input('ARESTA: ').split()
            peso = float(peso)
            if v1 in grafo.nodes() and v2 in grafo.nodes():
                grafo.add_edge(v1, v2, weight=peso)
                print(f'Aresta {v1}-{v2} peso:{peso} foi adicionada.')
            else:
                if v1 not in grafo.nodes():
                    print(f'Primeiro insira {v1} como vértice.')
                if v2 not in grafo.nodes():
                    print(f'Primeiro insira {v2} como vértice.')
        except ValueError:
            print("Entrada inválida! Insira dois vértices e um peso separados por espaço.")

def show(grafo):
    if grafo.number_of_nodes() == 0:
        print("O grafo está vazio. Adicione vértices e arestas primeiro.")
    else:
        pos = nx.spring_layout(grafo)
        labels = nx.get_edge_attributes(grafo, 'weight')

        nx.draw(
            grafo, pos, with_labels=True, 
            node_color='lightblue', edge_color='gray', 
            node_size=700, font_size=10
        )
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
        plt.title("Grafo")
        plt.show()

def kruskal(grafo):
    print("\nIniciando o algoritmo de Kruskal...")
    edges = list(grafo.edges(data=True))
    sorted_edges = sorted(edges, key=lambda edge: edge[2]['weight'])

    print("\nArestas ordenadas por peso:")
    for (u, v, peso) in sorted_edges:
        print(f"({u}, {v}) - Peso: {peso['weight']}")

    mst = nx.Graph()
    mst.add_nodes_from(grafo.nodes)

    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Inicialização de conjuntos disjuntos
    for node in grafo.nodes:
        parent[node] = node
        rank[node] = 0

    for (u, v, peso) in sorted_edges:
        if find(u) != find(v):
            mst.add_edge(u, v, weight=peso['weight'])
            union(u, v)
            print(f"Aresta adicionada: ({u}, {v}) - Peso: {peso['weight']}")

    print("\nÁrvore Geradora Mínima:")
    for (u, v, peso) in mst.edges(data=True):
        print(f"({u}, {v}) - Peso: {peso['weight']}")

    # Mostrar a AGM
    pos = nx.spring_layout(mst)
    labels = nx.get_edge_attributes(mst, 'weight')

    nx.draw(
        mst, pos, with_labels=True, 
        node_color='lightgreen', edge_color='blue', 
        node_size=700, font_size=10
    )
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.title("Árvore Geradora Mínima (Kruskal)")
    plt.show()

def menu():
    grafo = nx.Graph()  # Inicializar grafo

    while True:
        print("\n| GRAFO | --- | KRUSKAL |")
        print("1. Adicionar vértices")
        print("2. Adicionar arestas")
        print("3. Mostrar o grafo")
        print("4. Executar Kruskal")
        print("0. Sair")

        try:
            op = int(input("Opção: "))
            if op == 0:
                print("Saindo...")
                break
            elif op == 1:
                num_vertice = int(input("Quantos vértices deseja adicionar? "))
                add_vertice(grafo, num_vertice)
            elif op == 2:
                num_aresta = int(input("Quantas arestas você deseja adicionar? "))
                add_aresta(grafo, num_aresta)
            elif op == 3:
                show(grafo)
            elif op == 4:
                if grafo.number_of_edges() == 0:
                    print("O grafo está vazio! Adicione vértices e arestas antes.")
                else:
                    kruskal(grafo)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira uma entrada válida.")

menu()
