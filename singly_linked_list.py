class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        

    def Add_new_node_at_start(self, new_node):
        if self.is_empty():
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        


    def print_ll(self):
        if self.is_empty():
            print("list is Empty")
            return
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
        
if __name__ == "__main__":
    ll = SinglyLL()

    node1 = Node(2)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(2)
    node6 = Node(4)
    node7 = Node("node7")

    ll.Add_new_node_at_start(node1)
    ll.Add_new_node_at_start(node2)
    ll.Add_new_node_at_start(node3)

    ll.print_ll()
        

