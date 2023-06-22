
class Node:
  def __init__(self,value):
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
  
    

  
  def add_new_node_in_end(self,new_node):
    if self.is_empty():
      self.head = new_node
      new_node.next = self.head
      return
    temp = self.head
    while True:
      temp = temp.next
      if temp.next == self.head:
        break
    last_node = temp
    last_node.next = new_node
    new_node.next = self.head
    return
  







    

    
        

    
      
    
    
    
    
    
        
        



    
    
    

  def print_all(self):
    if self.is_empty():
      raise Exception('nothing to print')
    temp = self.head
    while True: 
      print(temp.value)
      temp = temp.next
      if temp == self.head:
        break
    return




if __name__ == "__main__":
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  node4 = Node(4)
  node5 = Node(5)
  node6 = Node('hello')

  csll = CircularSinglyLinkedList()

  csll.add_new_node_in_end(node1)
  csll.add_new_node_in_end(node2)
  csll.add_new_node_in_end(node3)
  csll.add_new_node_in_end(node4)
  csll.add_new_node_in_end(node5)

#   csll.add_new_node_at_start(node1)
#   csll.add_new_node_at_start(node2)
#   csll.add_new_node_at_start(node3)
  csll.add_new_node_at_index(node6,4)


  csll.print_all()
  


  
    
    
      





  