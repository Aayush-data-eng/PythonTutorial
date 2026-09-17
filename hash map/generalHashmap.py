class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for idx in range(self.MAX)]

  
    def getHash(self, key):
        asciiSum = 0
        for char in key:
            asciiSum += ord(char)
        return asciiSum % self.MAX

  
    def add(self, key, value):
        hsh = self.getHash(key)
        self.arr[hsh] = value

      
    def get (self, key) :
      # if key not in self.arr:
      #   raise Exception ("This data is not yet fed in our records.")
      #   return
      hsh = self.getHash(key)
      return self.arr[hsh]

  
    def print(self):
        for i in range(self.MAX):
            print(self.arr[i])

    # def modifiedAdd (self, key, value) :
    #   hsh = self.getHash(key)
    #   self.arr[key] = {key,value}

    # def modifiedPrint (self):
      # for key, val in (self.arr).items():
      #   print(key , " " , val)

ht = HashTable()
# print(ht.getHash("march 6"))
# ht.print()
ht.add("march 6", 130)
ht.add("march 28", 300)
# print()
ht.print()
# print(f"This is when we are accessing the element that is not in our list:-{ht.get('march 7')}")
# print(f"This is how to access elements in a hash table or map:-{ht.get('march 6')}")