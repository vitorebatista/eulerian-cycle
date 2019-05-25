# -*- coding: utf-8 -*-
# Exercício utilizando grafos
# Objetivo: verificar se o grafo tem ciclo euleriano e qual é o ciclo
# 1 - montar um grafo simples não direcionado
# 2 - verificar se é conexo (se todos os vértices estão conectados)
# 3 - verificar se os vértices estão em grau par
# 4 - procurar o ciclo euleriano (não é caminho euleriano)
# 5 - dar a complexidade da implementação dos itens 2, 3 e 4

# grafo = Grafo() -> ok
# grafo.importFromTxt() -> ok
# isConnected = grafo.isConnected() -> ok
# isPair = grafo.isAllPair() -> ok
# grafo.Hierholzer() -> aqui o bixo pega

import csv


class Graph:
    def __init__(self, direcionado=False):
        self.vertices = []
        self.visitedVertices = []
        self.visitedEdges = []
        self.adjacent = []
        self.edges = []
        self.eulerCycle = []

    def addVertex(self, ident):
        self.vertices.append(ident)
        self.visitedVertices.append(0)
        self.adjacent.append([])

    def addEdge(self, v1, v2):
        self.edges.append([v1, v2])
        self.visitedEdges.append(0)

    def createAdjacencyList(self):
        for edge in self.edges:
            v1 = self.vertices.index(edge[0])
            v2 = self.vertices.index(edge[1])
            self.adjacent[v1].append(edge[1])
            self.adjacent[v2].append(edge[0])

    def importFile(self, fileDir):
        line = 0
        with open(fileDir, newline='') as inputfile:
            for row in csv.reader(inputfile):
                line += 1
                if (line == 1):  # na primeira linha encontra todos os vertices
                    for i in row:
                        self.addVertex(int(i))
                else:  # nas demais linhas encontra as arestas (edges)
                    self.addEdge(int(row[0]), int(row[1]))
        self.createAdjacencyList()

    def depth_search(self, vIndex):  # recebe o index do vertice a fazer a busca em profundidade
        # marca vertice como visitado (pelo seu indice)
        self.visitedVertices[vIndex] = 1
        # para cada vértice adjacente (busca pelo índice)
        for adj in self.adjacent[vIndex]:
            # verifica se ainda não foi visitado
            if (self.visitedVertices[self.vertices.index(adj)] == 0):
                # busca nos vertices ligados, passando o index
                self.depth_search(self.vertices.index(adj))

    def isConnected(self):  # verifica se grafo é conexo
        # busca nos vertices ligados, passando o index de um elemento qualquer
        self.depth_search(0)
        # verifica se algum vertice nao foi visitado após a busca
        return (self.visitedVertices.count(0) == 0)

    def isAllPair(self):  # verifica se todos os vertices tem grau par
        for i in self.adjacent:
            if (len(i) % 2) > 0:
                return False
        return True

    # passa o valor dos vértices v1 e v2 e retorna o índice da aresta em self.edges
    def getEdgePosition(self, v1, v2):
        nPos = self.edges.count([v1, v2])
        if nPos == 0:
            nPos = self.edges.index([v2, v1])
        else:
            nPos = self.edges.index([v1, v2])
        return nPos

    # passa o valor dos vérticies v1 e v2 e marca aresta como visitada em self.visitedEdges
    def markEdgeAsVisited(self, v1, v2):
        nPos = self.getEdgePosition(v1, v2)
        self.visitedEdges[nPos] = 1
        return nPos

    # passa o valor dos vértices v1 e v2 e verifica se a aresta já foi visitada
    def alreadyVisitedEdge(self, v1, v2):
        nPos = self.getEdgePosition(v1, v2)
        return (self.visitedEdges[nPos] == 1)

    # retorna o próximo vértice que pode visitar a partir de um vértice de origem (índice)
    def getNextVertexIndex(self, vIdx):
        v1 = self.vertices[vIdx]
        for v2 in self.adjacent[vIdx]:
            if not self.alreadyVisitedEdge(v1, v2):
                self.markEdgeAsVisited(v1, v2)
                break
        return self.vertices.index(v2)

    # procura o próxima vértice que tem uma aresta (edge) não visitada, dentro de uma lista incremental (tour)
    def getNextVertexWithUnvisitedEdge(self, tour):
        nIndex = -1
        for i in tour:
            if nIndex < 0:
                for j in self.adjacent[self.vertices.index(i)]:
                    if not self.alreadyVisitedEdge(i, j):
                        nIndex = self.getEdgePosition(i, j)
                        break
                if nIndex >= 0:
                    for m in self.edges[nIndex]:
                        if m == i:
                            nIndex = m
                            break
        if nIndex < 0:
            return nIndex
        return self.vertices.index(nIndex)

    def depth_search_subcycle(self, vIndex):
        tour = []  # armazena o tour completo
        subtour = []  # armazena o subciclo

        # inicia com um vértice aleatório, digamos
        vStartIdx = vIndex
        # adiciona o valor do vértice ao circuito de controle
        tour.append(self.vertices[vStartIdx])
        # adiciona o valor do vértice ao circuito final
        self.eulerCycle.append(self.vertices[vStartIdx])

        # percorre o grafo até que todos os vértices tenham sido visitados
        while True:

            # da lista de vértices já percorridos, retorna o que ainda tem alguma aresta a visitar
            vCurrentIdx = self.getNextVertexWithUnvisitedEdge(tour)
            # se não houver, encerra a busca pois o ciclo está pronto
            if vCurrentIdx < 0:
                break

            vStartIdx = vCurrentIdx
            subtour.append(self.vertices[vCurrentIdx])

            while True:
                uidx = self.getNextVertexIndex(vCurrentIdx)
                subtour.append(self.vertices[uidx])
                vCurrentIdx = uidx
                if (vStartIdx == vCurrentIdx):
                    break

            for i in subtour:
                tour.append(i)

            # faz a aglutinação dos subciclos no ciclo de euler
            # troca o vértice isolado pela nova subsequência
            nPos = self.eulerCycle.index(subtour[0])
            self.eulerCycle.pop(nPos)
            for i in subtour:
                self.eulerCycle.insert(nPos, i)
                nPos += 1

            subtour.clear()

    def Hierholzer(self, nStart):  # funcao para identificar circuito euleriano
        self.depth_search_subcycle(nStart)


# Ref:
# http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof
# https://paginas.fe.up.pt/~rossetti/rrwiki/lib/exe/fetch.php?media=teaching:1011:cal:08_2.09_1.grafos6.pdf
