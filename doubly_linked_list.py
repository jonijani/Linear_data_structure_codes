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
    





  def print_all(self):
    if self.is_empty():
      #print('doubly linked list is empty')
      raise Exception('Doubly linked list is empty')
    temp = self.head
    while temp != None:
      print(temp.value)
      temp = temp.next
    return