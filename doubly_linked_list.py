class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.pre = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None