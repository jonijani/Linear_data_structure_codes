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