# Hash Table Collision Detection and how to avoid it




class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False

        # If key already exists then this will run
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found = True
                break
        # if key doesn't exist the  this will run
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
t['march 6'] = 130
t['march 6'] = 250
t['march 21'] = 20
t['dec 12'] = 33

print(t['march 6'])
print(t['dec 12'])
print(t.arr)

del t['march 6']
print(t.arr)
