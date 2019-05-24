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
        self.visitedArestas = []
        self.adjacent = []
        self.arestas = []
        self.eulerCycle = []

    def newVertice(self, ident):
        self.vertices.append( ident )
        self.visitedVertices.append(0)
        self.adjacent.append( [] )

    def newAresta(self, v1, v2):
        self.arestas.append( [v1, v2] )
        self.visitedArestas.append(0)

    def montaAdjacentes(self):
        for i in self.arestas:
            nPos1 = self.vertices.index(i[0])
            nPos2 = self.vertices.index(i[1])
            self.adjacent[nPos1].append( i[1] )
            self.adjacent[nPos2].append( i[0] )

    def importFile(self, fileDir):
        nLine = 0
        with open(fileDir, newline='') as inputfile:
            for row in csv.reader(inputfile):
                nLine += 1
                if (nLine == 1): # na primeira linha encontra todos os vertices
                    for i in row:
                        self.newVertice( int(i) )
                else: # nas demais linhas encontra as arestas
                    self.newAresta( int(row[0]), int(row[1]) )
        self.montaAdjacentes()

    def depth_search(self,vIndex): # recebe o index do vertice a fazer a busca em profundidade
        self.visitedVertices[ vIndex ] = 1 # marca vertice como visitado (pelo seu indice)
        for adj in self.adjacent[ vIndex ]: # para cada vértice adjacente (busca pelo índice)
            if (self.visitedVertices[ self.vertices.index(adj) ] == 0): # verifica se ainda não foi visitado
                self.depth_search( self.vertices.index(adj) ) # busca nos vertices ligados, passando o index

    def isConnected(self): # verifica se grafo é conexo
        self.depth_search(0)  #busca nos vertices ligados, passando o index de um elemento qualquer
        return (self.visitedVertices.count(0) == 0) #verifica se algum vertice nao foi visitado após a busca

    def isAllPair(self): #verifica se todos os vertices tem grau par
        for i in self.adjacent:
            if (len(i) % 2) > 0:
                return False
        return True





    def getArestaPosition(self,v1,v2):
        nPos = self.arestas.count([v1,v2])
        if nPos == 0:
            nPos = self.arestas.index([v2,v1])
        else:
            nPos = self.arestas.index([v1,v2])
        return nPos

    def markArestaAsVisited(self,v1,v2):
        nPos = self.getArestaPosition(v1,v2)
        self.visitedArestas[nPos] = 1
        return nPos

    def alreadyVisitedAresta(self,v1,v2):
        nPos = self.getArestaPosition(v1,v2)
        return (self.visitedArestas[nPos] == 1)

    def getNextVertexIndex(self,u):
        v1 = self.vertices[u]
        for v2 in self.adjacent[u]:
            if not self.alreadyVisitedAresta(v1,v2):
                self.markArestaAsVisited(v1,v2)
                break
        return self.vertices.index(v2)
    
    def getNextVertexWithUnvisitedEdge(self,tour):
        nIndex = -1
        for i in tour:
            if nIndex < 0:
                for j in self.adjacent[self.vertices.index(i)]:
                    if not self.alreadyVisitedAresta(i,j):
                        nIndex = self.getArestaPosition(i,j)
                        break
                if nIndex >= 0:
                    for m in self.arestas[nIndex]:
                        if m == i:
                            nIndex = m
                            break
        if nIndex < 0:
            return nIndex
        return self.vertices.index(nIndex)



    def depth_search_subcycle(self,vIndex): # recebe o index do vertice a fazer a busca em profundidade
        
        tour = []
        subtour = []

        startidx = vIndex
        tour.append(self.vertices[startidx])
        self.eulerCycle.append(self.vertices[startidx])

        while True:

            #if nLoop == 0:
            currentidx = startidx
            #else:
            currentidx = self.getNextVertexWithUnvisitedEdge(tour)
            if currentidx < 0:
                    break
            startidx = currentidx
           # nLoop += 1

            subtour.append( self.vertices[currentidx] )

            while True:
                uidx = self.getNextVertexIndex( currentidx )
                subtour.append( self.vertices[uidx] )
                currentidx = uidx
                if (startidx == currentidx):
                    break
            for i in subtour:
                tour.append(i)

            nPos = self.eulerCycle.index( subtour[0] )
            self.eulerCycle.pop( nPos )
            for i in subtour:
                self.eulerCycle.insert(nPos,i)
                nPos += 1

            subtour.clear()

        a = 10
        




    def Hierholzer(self): #funcao para identificar circuito euleriano
        self.depth_search_subcycle(5)




#Ref:
#http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof
#https://paginas.fe.up.pt/~rossetti/rrwiki/lib/exe/fetch.php?media=teaching:1011:cal:08_2.09_1.grafos6.pdf