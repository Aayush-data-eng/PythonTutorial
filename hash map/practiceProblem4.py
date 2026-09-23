class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]


    def getHash(self, key):
        asciiCharAsum = 0
        for char in key:
            asciiCharAsum += ord(char)
        return asciiCharAsum % self.MAX

    def __setitem__(self, key, val):
        hsh = self.getHash(key)
        for i in range(self.MAX):
            index = (hsh + i) % self.MAX
            if self.arr[index] != None:
                if self.arr[index][0] == key:
                    self.arr[index][1] = val
                    return
            if self.arr[index] == None or self.arr[index][1] == None:
                self.arr[index] = [key, val]
                return
        print("HashTable is full.")

    def print(self):
        for i in self.arr:
            print(i)

    def __getitem__(self, key):
        hsh = self.getHash(key)
        for i in range(self.MAX):
            index = (hsh + i) % self.MAX
            if self.arr[index] == None:
                print(
                    "Presently no such item exist in our records, hence can be accessed through your given key."
                )
                return

            if self.arr[index][0] == key:
                if self.arr[index][1] == None:
                    print("The item is already deleted from our records.")
                    return
                return self.arr[index][1]

    def __delitem__(self, key):
        hsh = self.getHash(key)
        for i in range(self.MAX):
            index = (hsh + 1) % self.MAX

            if self.arr[index] == None:
                print(
                    "The item is yet to get inserted, ie) Presently no such item exist in our records."
                )
                return
            if self.arr[index][0] == key:
                if self.arr[index][1] == None:
                    print("Item already deleted from our records.")
                    return
                self.arr[index][1] = None
                return


t = HashTable()
t["march 6"] = 20
t.print()
t["march 17"] = 88
print()
t.print()
del t["march 17"]
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
t["march 33"] = 999
t["april 1"] = 87
t["april 2"] = 123
t["april 3"] = 234234
t["april 4"] = 91
t["May 22"] = 4
t["May 7"] = 47
print()
t.print()
t["Jan 1"] = 0
del t["april 2"]
t["Jan 1"] = 0
print()
t.print()