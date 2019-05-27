"""
Referências:
    https://www-m9.ma.tum.de/graph-algorithms/hierholzer/index_en.html
    http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof
    https://paginas.fe.up.pt/~rossetti/rrwiki/lib/exe/fetch.php?media=teaching:1011:cal:08_2.09_1.grafos6.pdf
    https://www.python-course.eu/graphs_python.php
    https://wiki.python.org/moin/TimeComplexity
"""

from graph import Graph
from image import image

G = Graph()
G.import_file('./data/1.graph')
isConnected = G.is_connected()  # O(|Vˆ2|)
isAllPair = G.is_all_pair()  # O(|A|)
if (isConnected and isAllPair):
    G.euler_cycle(0)  # enviar índice do vértice inicial (deveria ser opcional)

print("\n---------------------------------------------------")
print("Grafo conexo? %r" % isConnected)
print("Cada vertice tem número par de arestas? %r" % isAllPair)
print("Vértices %r" % G.get_vertices())
print("Adjacenes %r" % G.get_adjacent())
print("Arestas %r" % G.get_edges())
print("Euler Cycle: %r" % G.get_euler_cycle())
print("Euler Cycle subtours: %r" % G.get_sub_tours())
print("---------------------------------------------------\n",)

# Abre imagem conforme estrutura da classe Graph
image(G)
