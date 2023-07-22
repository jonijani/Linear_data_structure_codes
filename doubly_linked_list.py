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
  
  
  def replace_new_node_at_index(self, new_node, position):
    if self.is_empty():
      raise Exception('Linked list empty cant replace node')
    temp = self.head
    # if position == 0:
    #   # first point new_node next and pre
    #   new_node.next = temp.next
    #   new_node.pre = None

    #   temp.next.pre = new_node
    #   self.head = new_node
    #   return
      
    index = 0
    temp = self.head
    while index != position: #index0123    | position 3
      temp = temp.next
      index += 1
    if temp == self.head:
      first_node = temp
      second_node = temp.next
      
      new_node.next = second_node
      second_node.pre = new_node
      self.head = new_node
      first_node.next = None
      return

    if temp.next == None:
      last_node = temp
      sec_last_node = temp.pre

      #new_node.next = None
      new_node.pre = sec_last_node
      sec_last_node.next = new_node
      last_node.pre = None
      return
     
    next_node = temp.next
    prev_node = temp.pre  # error
    # here we point new nodes to next node and previouse node 
    new_node.next = next_node
    new_node.pre = prev_node # error as no previous node
    # here we assign previous node to new_node and next_node to new_node
    next_node.pre = new_node
    prev_node.next = new_node # error as no previous node

    temp.next,temp.pre = None,None
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