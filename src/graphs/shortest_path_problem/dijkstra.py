class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

class Node:
    def __init__(self, index):
        self.index = index
        self._distance = float('inf')
        self._parent = None
        self._neighbors = []
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, new_distance):
        self._distance = new_distance
    
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, node):
        self._parent = node
    
    @property
    def neighbors(self):
        return self._neighbors
    
    @neighbors.setter
    def neighbors(self, data):
        node, weight = data

        self._neighbors.append(Edge(node, weight))

class Graph:
    def __init__(self):
        self._nodes = {}
    
    @property
    def nodes(self):
        return self._nodes
    
    @nodes.setter
    def nodes(self, index):
        self.nodes[index] = Node(index)
    
    def get_node_by_index(self, index):
        return self.nodes.get(index)

    def add_edge(self, index1, index2, weight):
        node1 = self.get_node_by_index(index1)

        node2 = self.get_node_by_index(index2)

        if node1 and node2:
            node1.neighbors = node2, weight
            node2.neighbors = node1, weight

    @staticmethod
    def extract_shortest_distance_node(node_list):
        node_list.sort(key=lambda node: node.distance)

        shortest_distance_node = node_list[0]

        node_list = node_list[1:]

        return shortest_distance_node, node_list
    
    @staticmethod
    def relax(node, neighbor, weight):
        if neighbor.distance > node.distance + weight:
            neighbor.distance = node.distance + weight

            neighbor.parent = node

    def dijkstra(self, source):
        source_node = self.get_node_by_index(source)

        source_node.distance = 0

        distances = []

        queue = list(self.nodes.values())

        while queue:
            node, queue = self.extract_shortest_distance_node(queue)

            distances.append(node)

            for neighbor in node.neighbors:
                self.relax(node, neighbor.node, neighbor.weight)

        for node in distances:
            print(f'Node: {node.index} | Distance: {node.distance}')