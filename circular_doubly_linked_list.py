class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class CircularDoubly:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add_new_node_at_start(self, new_node):
        if self.is_empty():
            new_node.next = new_node
            new_node.pre = new_node
            self.head = new_node
            return

        temp = self.head
        first_node = temp
        last_node = temp.pre

        new_node.next = first_node
        new_node.pre = last_node
        last_node.next = new_node
        first_node.pre = new_node
        self.head = new_node
        return
    
    def add_new_node_at_end(self, new_node):
        if self.is_empty():
            new_node.next = new_node
            new_node.pre = new_node
            self.head = new_node
            return

        temp = self.head
        first_node = temp
        last_node = temp.pre

        last_node.next = new_node
        new_node.next = first_node
        new_node.pre = last_node
        first_node.pre = new_node
        return



        
    def print_all(self):
        if self.is_empty():
            raise Exception('Doubly linked list is empty')
        temp = self.head
        while True:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    c_d_l_l = CircularDoubly()
    # c_d_l_l.add_new_node_at_start(node1)
    # c_d_l_l.add_new_node_at_start(node2)
    # c_d_l_l.add_new_node_at_start(node3)
    # c_d_l_l.add_new_node_at_start(node4)
    # c_d_l_l.add_new_node_at_start(node5)

    c_d_l_l.add_new_node_at_end(node1)
    c_d_l_l.add_new_node_at_end(node2)
    c_d_l_l.add_new_node_at_end(node3)
    c_d_l_l.add_new_node_at_end(node4)
    c_d_l_l.add_new_node_at_end(node5)







    c_d_l_l.print_all()
