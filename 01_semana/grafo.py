import matplotlib.pyplot as plt
import networkx as nx

# Inicializa o grafo globalmente para ser usado pelas funções
grafo = nx.Graph()

def add_vertice(num_vertices):
    """Adiciona vértices ao grafo."""
    for _ in range(num_vertices):
        vertice = input("Vértice: ")
        if vertice not in grafo.nodes:
            grafo.add_node(vertice)
            print(f"Vértice '{vertice}' adicionado.")
        else:
            print(f"O vértice '{vertice}' já existe.")

def add_aresta(num_arestas):
    """Adiciona arestas ao grafo."""
    print('Adicione as arestas no formato "v1 v2" (sem aspas, separados por espaço):')
    for _ in range(num_arestas):
        try:
            v1, v2 = input("Aresta: ").split()
            if v1 in grafo.nodes and v2 in grafo.nodes:
                grafo.add_edge(v1, v2)
                print(f"Aresta '{v1}-{v2}' adicionada.")
            else:
                print(f"Erro: Um ou ambos os vértices '{v1}' e '{v2}' não existem no grafo.")
        except ValueError:
            print("Entrada inválida! Insira dois vértices separados por espaço.")

def show():
    """Exibe o grafo."""
    if grafo.number_of_nodes() == 0:
        print("O grafo está vazio. Adicione vértices e arestas primeiro.")
    else:
        pos = nx.spring_layout(grafo)
        nx.draw(
            grafo, pos, with_labels=True,
            node_color='lightgreen',
            edge_color='blue',
            node_size=600, font_size=10
        )
        plt.title('Grafo')
        plt.show()

def menu():
    """Exibe o menu e gerencia as operações do grafo."""
    while True:
        print("\n| GRAFO |- - --- - -| SIMPLES |")
        print("1. Adicionar vértice")
        print("2. Adicionar ligação")
        print("3. Visualizar grafo")
        print("0. SAIR")
        try:
            op = int(input("Opção: "))
            if op == 0:
                print("Saindo do programa...")
                break
            elif op == 1:
                num_vertices = int(input("Quantos vértices deseja adicionar? "))
                add_vertice(num_vertices)
            elif op == 2:
                num_arestas = int(input("Quantas arestas você deseja adicionar? "))
                add_aresta(num_arestas)
            elif op == 3:
                show()
            else:
                print("OPÇÃO INVÁLIDA! TENTE UMA OPÇÃO VÁLIDA.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Executa o menu
menu()
