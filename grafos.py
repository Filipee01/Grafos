import queue

class Grafo:
    
    def __init__(self, num_vertices):
        """ Inicializa as variáveis do grafo """

        self.num_vertices = num_vertices
        self.matriz_adjacentes = [[0] * num_vertices for _ in range(num_vertices)] # Cria uma matriz quadrada preenchida com zeros
        self.vetor_adjacentes = {i: [] for i in range(num_vertices)} # Cria um dicionário com listas vazias para cada vértice

    def exibir_grafo(self):
        """ Mostra as informações do grafo """

        print("Matriz de adjacência:")
        for i in range(self.num_vertices):
            print(self.matriz_adjacentes[i])

        print()

        print("Lista de adjacência:") 
        for i in range(self.num_vertices):
            print(self.vetor_adjacentes[i])

    def busca_em_largura(self, source):
        """ Realiza a busca em largura (BFS) """

        explorados = [False] * self.num_vertices # Lista para marcar os vértices já visitados

        distancia = [-1] * self.num_vertices  # Lista para armazenar a distância do vértice inicial até os demais

        predecessor = [-1] * self.num_vertices  # Lista para guardar o predecessor de cada vértice

        explorados[source] = True # Marca o vértice inicial como visitado

        fila = queue.Queue() # Fila para gerenciar os vértices a serem explorados
        fila.put(source)
        distancia[source] = 0

        # Enquanto houver vértices na fila
        while not fila.empty():
            v = fila.get()  # Remove o próximo vértice da fila

            for a in self.vetor_adjacentes[v]:
                
                # Se o vizinho ainda não foi visitado
                if not explorados[a]:
                    fila.put(a)  # Adiciona o vizinho à fila
                    explorados[a] = True  # Marca o vizinho como visitado
                    predecessor[a] = v  # Define o vértice atual como predecessor do vizinho
                    distancia[a] = distancia[v] + 1  # Calcula a distância do vizinho a partir do inicial

        # Retorna as listas de distâncias e predecessores
        return distancia, predecessor

    def caminho(self, p, d):
        """ Mostra o caminho até o vértice de destino """
        # p é a lista de predecessores dos vértices 
        
        visitados = [] # Lista para armazenar os vértices do caminho
        
        # Enquanto não alcançar o vértice inicial
        while p[d] != -1:

            visitados.append(d) # Adiciona o vértice atual à lista
            d = p[d] # Move para o predecessor do vértice atual

        if not visitados:
            print("Não existe caminho entre os vértices")
        else:  
            visitados.append(d) # Adiciona o vértice inicial à lista
            print(visitados) # Exibe o caminho encontrado

    def busca_em_profundidade(self):
        """ Realiza a busca em profundidade (DFS) """

        visitados = [] # Lista para armazenar os vértices já visitados

        # Percorre todos os vértices do grafo
        for v in range(self.num_vertices):
            # Verifica se o vértice já foi explorado
            if v in visitados: 
                continue

            stack = [v] # Adiciona o vértice inicial na pilha

            # Enquanto a pilha não estiver vazia
            while stack:
                vertice = stack[-1] # Obtém o vértice no topo da pilha

                # Se o vértice ainda não foi visitado, exibe e marca como visitado
                if vertice not in visitados:
                    print(f"Vértice: {vertice}")
                    visitados.append(vertice)

                encontrou_vizinho = False # Variável para verificar se há vizinhos não visitados

                # Percorre os vizinhos do vértice atual
                for i in self.vetor_adjacentes[vertice]:
                    if i not in visitados:
                        stack.append(i) # Adiciona o vizinho à pilha
                        encontrou_vizinho = True
                        break
                
                # Se não houver vizinhos não visitados, remove o vértice do topo da pilha
                if not encontrou_vizinho:
                    stack.pop()