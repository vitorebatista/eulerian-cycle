# -*- coding: utf-8 -*-
""" Exercício utilizando grafos
Objetivo: verificar se o grafo tem ciclo euleriano e qual é o ciclo
1 - montar um grafo simples não direcionado
2 - verificar se é conexo (se todos os vértices estão conectados)
3 - verificar se os vértices estão em grau par
4 - procurar o ciclo euleriano (não é caminho euleriano)
5 - dar a complexidade da implementação dos itens 2, 3 e 4
"""
import csv


class Graph:
    def __init__(self):
        self.file = ""
        self.vertices = []
        self.visitedVertices = []
        # Lista das arestas visitadas 
        self.visitedEdges = []
        # Lista com as adjacentes
        self.adjacent = []
        # Lista com as arestas
        self.edges = []
        # Ciclo euleriano completo
        self.eulerCycle = []
        # Subciclos euleriano
        self.subtours = []
        

    def get_vertices(self):
        return self.vertices

    def get_adjacent(self):
        return self.adjacent

    def get_edges(self):
        return self.edges

    def get_euler_cycle(self):
        return self.eulerCycle

    def get_sub_tours(self):
        return self.subtours

    def image_file(self):
        return self.file

    def add_vertex(self, ident): # O(1)
        self.vertices.append(ident) # O(1)
        self.visitedVertices.append(0) # O(1)
        self.adjacent.append([]) # O(1)

    def add_edge(self, v1, v2): # O(1)
        """ Adiciona a lista de arestas"""
        self.edges.append([v1, v2]) # O(1)
        self.visitedEdges.append(0) # O(1)

    def __create_adjacency_list(self):
        for edge in self.edges: # O(|A|)
            v1 = self.vertices.index(edge[0]) # O(|V|)
            v2 = self.vertices.index(edge[1]) # O(|V|)
            self.adjacent[v1].append(edge[1]) # O(1)
            self.adjacent[v2].append(edge[0]) # O(1)

    def import_file(self, file): # O(|A|)
        self.file = file # O(1)
        line = 0 # O(1)
        with open(file, newline='') as inputfile: # O(1)
            for row in csv.reader(inputfile): # O(|A|)
                line += 1 # O(1)
                # na primeira linha encontra todos os vertices
                if (line == 1):  # O(1)
                    for i in row: # O(|V|)
                        self.add_vertex(int(i)) # O(1)
                else:  # nas demais linhas encontra as arestas (edges)
                    self.add_edge(int(row[0]), int(row[1]))
        self.__create_adjacency_list() # O(|A|)

    def __depth_search(self, index): # O(|Vˆ2|)
        """ Recebe o index do vertice a fazer a busca em profundidade """

        # marca vertice como visitado (pelo seu indice)
        self.visitedVertices[index] = 1 # O(1)
        # para cada vértice adjacente (busca pelo índice)
        for adj in self.adjacent[index]: # O(|A|)
            # verifica se ainda não foi visitado
            if (self.visitedVertices[self.vertices.index(adj)] == 0): # O(|V|)
                # busca nos vertices ligados, passando o index
                self.__depth_search(self.vertices.index(adj)) # O(|V|)

    def is_connected(self): # O(|Vˆ2|)
        """verifica se grafo é conexo"""
        # busca nos vertices ligados, passando o index de um elemento qualquer
        self.__depth_search(0)
        # verifica se algum vertice nao foi visitado após a busca
        return (self.visitedVertices.count(0) == 0) # O(1)

    def is_all_pair(self): # O(|A|)
        """verifica se todos os vertices tem grau par"""
        for i in self.adjacent: # O(|A|)
            if (len(i) % 2) > 0: # O(1)
                return False
        return True

    def find_edge(self, v1, v2): # O(|A|)
        """passa o valor dos vértices v1 e v2 e retorna o índice da aresta em self.edges"""
        position = self.edges.count([v1, v2]) # O(|A|)
        return self.edges.index([v2, v1] if position == 0 else [v1, v2]) # O(|A|)

    def __already_visited_edge(self, v1, v2, mark = False): # O(|A|)
        """passa o valor dos vértices v1 e v2 e verifica se a aresta já foi visitada
            mark - define se deve marcar como visitado
        """
        position = self.find_edge(v1, v2) # O(|A|)
        visited = self.visitedEdges[position] == 1 # O(1)
        if (mark): # O(1)
            self.visitedEdges[position] = 1 # O(1)
        return visited

    def __get_next_vertex_index(self, index): # O(|A|^2)
        """retorna o próximo vértice que pode visitar a partir de um vértice de origem (índice)"""
        v1 = self.vertices[index] # O(1)
        for v2 in self.adjacent[index]: # O(|A|)
            if not self.__already_visited_edge(v1, v2, True): # O(|A|)
                break
        return self.vertices.index(v2) # O(|V|)

    def __get_next_vertex_with_unvisited_edge(self, tour): # O(|A|^2)
        """ Procura o próxima vértice que tem uma aresta (edge) não visitada,
            dentro de uma lista incremental (tour)
        """
        index = -1
        for i in tour: # O(|V|)
            if index < 0: # O(1)
                for j in self.adjacent[self.vertices.index(i)]: # O(|A|)
                    if not self.__already_visited_edge(i, j): # O(|A|)
                        index = self.find_edge(i, j) # O(|A|)
                        break
                if index >= 0: # O(1)
                    for m in self.edges[index]: # O(1)
                        if m == i:
                            index = m
                            break
        if index < 0: # O(1)
            return index
        return self.vertices.index(index)

    def euler_cycle(self, index  = 0): # O(|A|^2)
        """ Função para identificar circuito euleriano utilizando o método de Hierholzer
        index - posição para iniciar a pesquisa
        """
         # armazena o tour completo
        tour = []
        # armazena o subciclo
        subtour = []

        # adiciona o valor do vértice ao circuito de controle
        tour.append(self.vertices[index]) # O(1)
        # adiciona o valor do vértice ao circuito final
        self.eulerCycle.append(self.vertices[index]) # O(1)

        # percorre o grafo até que todos os vértices tenham sido visitados
        while True:

            # da lista de vértices já percorridos, retorna o que ainda tem alguma aresta a visitar
            currentIdx = self.__get_next_vertex_with_unvisited_edge(tour) # O(|A|^2)
            # se não houver, encerra a busca pois o ciclo está pronto
            if currentIdx < 0: # O(1)
                break

            startIdx = currentIdx # O(1)
            subtour.append(self.vertices[currentIdx]) # O(1)

            while True: # O(|A|^2)
                uidx = self.__get_next_vertex_index(currentIdx) # O(|A|^2)
                subtour.append(self.vertices[uidx]) # O(1)
                currentIdx = uidx # O(1)
                if (startIdx == currentIdx): # O(1)
                    break

            # faz a aglutinação dos subciclos no ciclo de euler
            # troca o vértice isolado pela nova subsequência
            position = self.eulerCycle.index(subtour[0]) # O(|V|)
            self.eulerCycle.pop(position) # O(1)
            for item in subtour: # O(|V|^2)
                tour.append(item) # O(1)
                self.eulerCycle.insert(position, item) # O(|V|)
                position += 1 # O(1)
            
            self.subtours.append(subtour) # O(1)
            subtour = [] # O(1)
