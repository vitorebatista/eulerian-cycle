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
        self.visitedEdges = []
        self.adjacent = []
        self.edges = []
        self.eulerCycle = []
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

    def add_vertex(self, ident):
        self.vertices.append(ident)
        self.visitedVertices.append(0)
        self.adjacent.append([])

    def add_edge(self, v1, v2):
        """ Adiciona a lista de arestas"""
        self.edges.append([v1, v2])
        self.visitedEdges.append(0)

    def __create_adjacency_list(self):
        for edge in self.edges:
            v1 = self.vertices.index(edge[0])
            v2 = self.vertices.index(edge[1])
            self.adjacent[v1].append(edge[1])
            self.adjacent[v2].append(edge[0])

    def import_file(self, file):
        self.file = file
        line = 0
        with open(file, newline='') as inputfile:
            for row in csv.reader(inputfile):
                line += 1
                if (line == 1):  # na primeira linha encontra todos os vertices
                    for i in row:
                        self.add_vertex(int(i))
                else:  # nas demais linhas encontra as arestas (edges)
                    self.add_edge(int(row[0]), int(row[1]))
        self.__create_adjacency_list()

    def __depth_search(self, index):
        """ Recebe o index do vertice a fazer a busca em profundidade """

        # marca vertice como visitado (pelo seu indice)
        self.visitedVertices[index] = 1
        # para cada vértice adjacente (busca pelo índice)
        for adj in self.adjacent[index]:
            # verifica se ainda não foi visitado
            if (self.visitedVertices[self.vertices.index(adj)] == 0):
                # busca nos vertices ligados, passando o index
                self.__depth_search(self.vertices.index(adj))

    def is_connected(self):
        """verifica se grafo é conexo"""
        # busca nos vertices ligados, passando o index de um elemento qualquer
        self.__depth_search(0)
        # verifica se algum vertice nao foi visitado após a busca
        return (self.visitedVertices.count(0) == 0)

    def is_all_pair(self):
        """verifica se todos os vertices tem grau par"""
        for i in self.adjacent:
            if (len(i) % 2) > 0:
                return False
        return True

    def find_edge(self, v1, v2):
        """passa o valor dos vértices v1 e v2 e retorna o índice da aresta em self.edges"""
        position = self.edges.count([v1, v2])
        return self.edges.index([v2, v1] if position == 0 else [v1, v2])

    def __mark_edge_as_visited(self, v1, v2):
        """passa o valor dos vérticies v1 e v2 e marca aresta como visitada em self.visitedEdges"""
        position = self.find_edge(v1, v2)
        self.visitedEdges[position] = 1
        return position

    def __already_visited_edge(self, v1, v2):
        """passa o valor dos vértices v1 e v2 e verifica se a aresta já foi visitada"""
        nPos = self.find_edge(v1, v2)
        return (self.visitedEdges[nPos] == 1)

    def __get_next_vertex_index(self, index):
        """retorna o próximo vértice que pode visitar a partir de um vértice de origem (índice)"""
        v1 = self.vertices[index]
        for v2 in self.adjacent[index]:
            if not self.__already_visited_edge(v1, v2):
                self.__mark_edge_as_visited(v1, v2)
                break
        return self.vertices.index(v2)

    def __get_next_vertex_with_unvisited_edge(self, tour):
        """procura o próxima vértice que tem uma aresta (edge) não visitada, dentro de uma lista incremental (tour)"""
        index = -1
        for i in tour:
            if index < 0:
                for j in self.adjacent[self.vertices.index(i)]:
                    if not self.__already_visited_edge(i, j):
                        index = self.find_edge(i, j)
                        break
                if index >= 0:
                    for m in self.edges[index]:
                        if m == i:
                            index = m
                            break
        if index < 0:
            return index
        return self.vertices.index(index)

    def __depth_search_subcycle(self, index):
        tour = []  # armazena o tour completo
        subtour = []  # armazena o subciclo

        # adiciona o valor do vértice ao circuito de controle
        tour.append(self.vertices[index])
        # adiciona o valor do vértice ao circuito final
        self.eulerCycle.append(self.vertices[index])

        # percorre o grafo até que todos os vértices tenham sido visitados
        while True:

            # da lista de vértices já percorridos, retorna o que ainda tem alguma aresta a visitar
            currentIdx = self.__get_next_vertex_with_unvisited_edge(tour)
            # se não houver, encerra a busca pois o ciclo está pronto
            if currentIdx < 0:
                break

            startIdx = currentIdx
            subtour.append(self.vertices[currentIdx])

            while True:
                uidx = self.__get_next_vertex_index(currentIdx)
                subtour.append(self.vertices[uidx])
                currentIdx = uidx
                if (startIdx == currentIdx):
                    break

            # faz a aglutinação dos subciclos no ciclo de euler
            # troca o vértice isolado pela nova subsequência
            position = self.eulerCycle.index(subtour[0])
            self.eulerCycle.pop(position)
            for i in subtour:
                tour.append(i)
                self.eulerCycle.insert(position, i)
                position += 1
            
            self.subtours.append(subtour)
            subtour = []

    def Hierholzer(self, start = 0):
        """funcao para identificar circuito euleriano
        start - posição inicial para iniciar a pesquisa
        """
        self.__depth_search_subcycle(start)
