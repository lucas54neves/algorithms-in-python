class BinarySearchTree():
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def add_node(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
        else:
            old_node = self.root

            current_node = old_node.left if node.value <= old_node.value else old_node.right

            while current_node is not None:
                old_node = current_node

                current_node = current_node.left if node.value <= current_node.value else current_node.right
            
            if node.value <= old_node.value:
                old_node.left = node
            else:
                old_node.right = node
        
        return True

    @property
    def height(self):
        return self.root.height()
    
    def search_value(self, value):
        return self.root.search_value(value)
    
    def in_order(self):
        return self.root.in_order()

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.value)
    
    def search_value(self, value):
        if value == self.value:
            return True
        
        if value <= self.value:
            return self.left.search_value(value) if self.left is not None else False
        
        return self.right.search_value(value) if self.right is not None else False
    
    def height(self):
        height_left = self.left.height() if self.left is not None else 0

        height_right = self.right.height() if self.right is not None else 0

        return max(height_left, height_right) + 1
    
    def in_order(self):
        list_in_order = []

        if self.left is not None:
            list_in_order.extend(self.left.in_order())
        
        list_in_order.append(self.value)
        
        if self.right is not None:
            list_in_order.extend(self.right.in_order())
        
        return list_in_order