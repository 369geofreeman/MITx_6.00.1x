# Basic Hash table


# A hash table (hash map) is a data structure that implements an associative array abstract data type, 
# a structure that can map keys to values. A hash table uses a hash function to compute an index, 
# also called a hash code, into an array of buckets or slots, from which the desired value can be found. 
# During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t['march 6'] = 130
t['march 21'] = 20
t['dec 12'] = 33

print(t['march 6'])
print(t['dec 12'])
del t['march 21']
print(t.arr)

