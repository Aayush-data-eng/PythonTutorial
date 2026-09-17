class HashTable :
  def __init__ (self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]

  def getHash (self, key) :
    asciiSum = 0
    for char in key:
      asciiSum += ord(char)
      return asciiSum % self.MAX
  
  def __setitem__ (self, key, val) :
    hsh = self.getHash(key)
    self.arr[hsh] = val

  def __getitem__ (self, key) :
    hsh = self.getHash(key)
    return self.arr[hsh]

  def print(self):
    for i in self.arr:
        print(i)

  def __delitem__ (self, key):
    hsh = self.getHash(key)
    self.arr[hsh] = None

t = HashTable()
t['march 6'] = 130
t["march 1"] = 20
t['dec 17'] = 27
t.print()
del t['march 6'] 