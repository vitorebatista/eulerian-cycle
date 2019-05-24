from graph import Graph

grafo = Graph()
grafo.importFile('./data/graph2.csv')
isConnected = grafo.isConnected()
isPair = grafo.isAllPair()
grafo.Hierholzer()

print("grafo conexo? %r" % isConnected)
print("cada vertice tem numero par de arestas? %r" % isPair)
print("Euler Cycle: %r" % grafo.eulerCycle)
print("fim")

# melhor exemplo https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html
# na aba "more" tem o pseudocodigo