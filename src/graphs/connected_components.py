class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self._neighbors = []
    
    def __repr__(self):
        return str(self.index)

    @property
    def neighbors(self):
        return self._neighbors
    
    @neighbors.setter
    def neighbors(self, neighbor):
        self._neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self._nodes = {}
        self.connected_components = {}
    
    @property
    def nodes(self):
        return self._nodes
    
    @nodes.setter
    def nodes(self, index):
        self._nodes[index] = Node(index)
    
    def add_edge(self, index_1, index_2, directional=False):
        if directional:
            self.nodes[index_1].neighbors = self.nodes[index_2]
        else:
            self.nodes[index_1].neighbors = self.nodes[index_2]
            self.nodes[index_2].neighbors = self.nodes[index_1]
    
    def return_nodes_unvisited(self):
        return [node for node in list(self.nodes.values()) if not node.visited]
    
    def calculate_connected_components(self):
        nodes_unvisited = self.return_nodes_unvisited()

        while nodes_unvisited:
            node = nodes_unvisited[0]

            index = len(self.connected_components)

            self.connected_components[index] = [node]

            node.visited = True

            for neighbor in node.neighbors:
                self.connected_components[index].append(neighbor)

                neighbor.visited = True
            
            nodes_unvisited = self.return_nodes_unvisited()
        
        for index, connected_components in self.connected_components.items():
            print(f'Componente {index + 1}: {str(connected_components)}')
        
        print(f'{len(self.connected_components)} componentes conectados')