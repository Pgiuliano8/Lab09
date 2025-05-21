import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._airports = DAO.getAllAirports()
        self._grafo = nx.Graph()

    def buildGraph(self):
        self._grafo.clear()