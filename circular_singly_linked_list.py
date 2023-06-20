class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class CircularSinglyLinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    if self.head == None:
      return True
    else:
      return False
    
  def add_new_node_at_start(self,new_node):
    if self.is_empty():
      self.head = new_node
      new_node.next = self.head
      return
    temp = self.head
    while temp.next != self.head:
      temp = temp.next
    temp.next = new_node
    new_node.next = self.head
    self.head = new_node
    return