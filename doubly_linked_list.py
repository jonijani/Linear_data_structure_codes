class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.pre = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    #return self.head == None
    if self.head == None:
      return True
    else:
      return False
    
  def add_new_node_at_start(self, new_node):
    if self.is_empty():
      self.head = new_node
      return
    first_node = self.head  # temp pointing first node
    new_node.next = first_node
    first_node.pre = new_node
    self.head = new_node

  def add_new_node_at_end(self, new_node):
    if self.is_empty():
      self.head = new_node
      return
    temp = self.head
    while temp.next != None:
      temp = temp.next
    temp.next = new_node
    new_node.pre = temp
    return
    





  def print_all(self):
    if self.is_empty():
      #print('doubly linked list is empty')
      raise Exception('Doubly linked list is empty')
    temp = self.head
    while temp != None:
      print(temp.value)
      temp = temp.next
    return
  




if __name__ == "__main__":
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  node4 = Node(4)
  node5 = Node(5)
  node6 = Node('hello')
  doubly_l_l = DoublyLinkedList()

  doubly_l_l.add_new_node_at_start(node1)
  doubly_l_l.add_new_node_at_start(node2)
  doubly_l_l.add_new_node_at_start(node3)

  doubly_l_l.add_new_node_at_end(node1)
  doubly_l_l.add_new_node_at_end(node2)
  doubly_l_l.add_new_node_at_end(node3)
  doubly_l_l.add_new_node_at_end(node4)
  doubly_l_l.add_new_node_at_end(node5)