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

    
    def add_new_node_at_end(self, new_node):
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def add_new_node_at_index(self, new_node, position):  #  value=7  position 18 
        if self.is_empty():
            if position == 0:
                self.head = new_node
            else:
                #print('index out of range ')
                raise Exception('index out of range ')
            return
            

        index = 0
        previous = None
        temp = self.head
        
        while index != position:
            if temp.next == None:
                #print('index out of range')
                raise Exception('index out of range ')
            previous = temp
            temp = temp.next
            index += 1
        previous.next = new_node
        new_node.next = temp.next

    def update_first_node(self,new_value):
        if self.is_empty():
            print('No node in linked list to update') 
            return
        self.head.value = new_value
        return
    
    def update_last_node(self,new_value):
        if self.is_empty():
            print('No node in linked list to update')
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.value = new_value
        return
    
    def update_node_value_at_index(self,new_value,position):
        if self.is_empty():
            print('linked list is empty')
            return
        
        if position == 0:
            self.head.value = new_value
            return

        index = 0
        previous = None
        temp = self.head
        while index != position:
            previous = temp
            temp = temp.next
            index += 1
        previous.next.value = new_value
        return
    
        # Remove first node ,last node, and specific index of node
    def remove_first_node(self):
        if self.head == None:
            print('Linked is empty ')
            return
        self.head = self.head.next
        return
    
    def remove_last_node(self):
        if self.is_empty():
            print('Linked list is empty')
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return
    
    def remove_node_at_index(self,position):
        if self.is_empty():
            print('Linked list is empty ')

        if position == 0:
            temp = self.head
            temp = temp.next
            self.head = temp
            return
        
        index = 0
        previous = None
        temp = self.head
        while index != position:
            previous = temp
            temp = temp.next
            index += 1
        previous.next = temp.next
        return
    
    
        


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

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node("node7")

    # ll.Add_new_node_at_start(node1)
    # ll.Add_new_node_at_start(node2)
    # ll.Add_new_node_at_start(node3)

    ll.add_new_node_at_end(node1)
    ll.add_new_node_at_end(node2)
    ll.add_new_node_at_end(node3)
    ll.add_new_node_at_end(node4)
    ll.add_new_node_at_end(node5)

    #ll.add_new_node_at_index(node7,3)

    #ll.update_first_node('1_first_node_updated')

    #ll.update_last_node('5_last_node_updated')

    ll.update_node_value_at_index('New_value_on_this_index ',1)


    ll.print_ll()
        

