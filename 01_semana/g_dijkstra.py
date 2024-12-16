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

# Algoritmo de Dijkstra
def dijkstra(grafo, start, end):
    dist = {node: float('inf') for node in grafo.nodes()}
    dist[start] = 0
    previous_nodes = {node: None for node in grafo.nodes()}
    
    priority_queue = [(0, start)]  # (distância, nó)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > dist[current_node]:
            continue
        
        for neighbor, attrs in grafo[current_node].items():
            weight = attrs.get('weight', 1)
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruir o caminho
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    
    path = path[::-1]  # Reverter a lista para ter o caminho de start a end
    return dist, path

def menu():
    grafo = nx.Graph()  # Inicializar grafo

    while True:
        print("\n| GRAFO | --- | DIJKSTRA |")
        print("1. Adicionar vértices")
        print("2. Adicionar arestas")
        print("3. Mostrar o grafo")
        print("4. Executar Dijkstra")
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
                    start = input("Informe o vértice de início: ")
                    end = input("Informe o vértice de destino: ")
                    dist, path = dijkstra(grafo, start, end)
                    print(f"\nDistâncias: {dist}")
                    print(f"Caminho mais curto de {start} até {end}: {path}")
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira uma entrada válida.")

menu()
