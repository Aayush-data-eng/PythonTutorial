# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
from collections import deque
class Stack:
  def __init__(self):
      self.container = deque()

  def push(self,val):
      self.container.append(val)

  def pop(self):
      return self.container.pop()

  def peek(self):
      return  self.container[-1]

  def isEmpty(self):
      return len(self.container)==0

  def size(self):
      return len(self.container)

def isMatch (ch1, ch2) :
    matchDict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    return matchDict[ch1] == ch2

def isBalance (s) :
    stack = Stack()
    for ch in s:
        if ch =='(' or ch == '{' or ch == '[' :
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']' :
            if stack.isEmpty() :
                return False
            if isMatch(ch, stack.peek()):
                stack.pop()
            else: return False

    return stack.size() == 0

if __name__ == '__main__':
    print(isBalance("({a+b})"))
    print(isBalance("))((a+b}{"))
    print(isBalance("((a+b))"))
    print(isBalance("((a+g))"))
    print(isBalance("))"))
    print(isBalance("[a+b]*(x+2y)*{gg+kk}"))