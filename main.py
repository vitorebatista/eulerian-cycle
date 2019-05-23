from graph import Graph

grafo = Graph()
grafo.importFile('./data/graph.csv')
isConnected = grafo.isConnected()
isPair = grafo.isAllPair()
grafo.Hierholzer()

print("grafo conexo? %r" % isConnected)
print("cada vertice tem numero par de arestas? %r" % isPair)
print("Euler Cycle: %r" % grafo.eulerCycle)
