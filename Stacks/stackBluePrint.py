from typing import Deque
from collections import deque
class Stack:
  def  __init__ (self):
    # self.container : Deque[int] = deque() #This will let only integers value to get inserted, nut alone this dosen't stop string at runtime so we will modify t he push function
    self.container = deque()

  def push (self, val) :
    # if not isinstance (val, int):
    #   raise TypeError ("Only integers are allowed.")
    self.container.append(val)

  def pop (self) :
    return self.container.pop()

  def peek (self) :
    return self.container[-1]

  def isEmpty (self) :
    return self.size() == 0
    # return len(self.container) == 0
  
  def size (self) :
    return len(self.container)
# print(dir(Deque))

stk = Stack() 
stk.push(5)
stk.push('Jaolly')
print(stk.size())
print(stk.peek())