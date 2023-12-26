class Node:
  def __init__(self,value):
      self.value = value
      self.next = None


class linkedList:
  def __init__(self):
      self.head = None
      self.tail = None

class CircularQueue:
  def __init__(self):
      self.ll = linkedList()