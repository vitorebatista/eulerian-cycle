from graph import Graph

grafo = Graph()
grafo.importFile('./data/graph6.csv')
isConnected = grafo.isConnected()
isPair = grafo.isAllPair()
grafo.Hierholzer(0) #enviar índice do vértice inicial (deveria ser opcional)

print("grafo conexo? %r" % isConnected)
print("cada vertice tem numero par de arestas? %r" % isPair)
print("Euler Cycle: %r" % grafo.eulerCycle)
print("fim")

# melhor exemplo https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html
# na aba "more" tem o pseudocodigo


# na real acho que ta faltando uma coisa:
# calcular a distancia do vértice, pra garantir que ele vai percorrer o melhor caminho e 
# não vai ficar reentrando em alguns vértices que já passou.
# https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html