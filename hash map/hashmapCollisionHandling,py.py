class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.getHash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        hsh = self.getHash(key)
        for element in self.arr[hsh] :
            if element[0] == key:
                return element [1]

    def print(self):
        for i in self.arr:
            print(i)

    def __delitem__(self, key):
        hsh = self.getHash(key)
        for index , element in enumerate (self.arr[hsh]) :
            if element [0] == key :
                del self.arr[hsh][index]


t = HashTable()
t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
t.print()
print ()
print(t["march 6"])
print(t["march 17"])
del t['march 17']
print()
t.print()