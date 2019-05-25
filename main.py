"""
Referências:
    Hierholzer:
        https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html # na aba "more" tem o pseudocodigo

    http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof
    https://paginas.fe.up.pt/~rossetti/rrwiki/lib/exe/fetch.php?media=teaching:1011:cal:08_2.09_1.grafos6.pdf
"""

from graph import Graph
from image import image

G = Graph()
G.importFile('./data/6.graph')
G.Hierholzer(0)  # enviar índice do vértice inicial (deveria ser opcional)

print("\n---------------------------------------------------")
print("Grafo conexo? %r" % G.isConnected())
print("Cada vertice tem número par de arestas? %r" % G.isAllPair())
print("Vértices %r" % G.getVertices())
print("Adjacenes %r" % G.getAdjacent())
print("Arestas %r" % G.getEdges())
print("Euler Cycle: %r" % G.getEulerCycle())
print("---------------------------------------------------\n",)

# Abre imagem conforme estrutura da classe Graph
image(G)


# na real acho que ta faltando uma coisa:
# calcular a distancia do vértice, pra garantir que ele vai percorrer o melhor caminho e
# não vai ficar reentrando em alguns vértices que já passou.
# https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html
