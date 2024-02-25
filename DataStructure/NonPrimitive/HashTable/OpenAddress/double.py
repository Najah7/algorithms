class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def hash(self, key):
        return key % self.size

    def hash2(self, key):
        return 7 - (key % 7)

    def insert(self, key):
        index = self.hash(key)
        if self.table[index] is None or self.table[index] is self.deleted:
            self.table[index] = key
        else:
            index2 = self.hash2(key)
            i = 1
            while True:
                new_index = (index + i * index2) % self.size
                if (
                    self.table[new_index] is None
                    or self.table[new_index] is self.deleted
                ):
                    self.table[new_index] = key
                    break
                i += 1

    def search(self, key):
        index = self.hash(key)
        if self.table[index] == key:
            return index
        index2 = self.hash2(key)
        i = 1
        while self.table[(index + i * index2) % self.size] != key:
            i += 1
        return (index + i * index2) % self.size

    def delete(self, key):
        index = self.search(key)
        self.table[index] = self.deleted

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None and self.table[i] is not self.deleted:
                print(i, ":", self.table[i])
            else:
                print(i, ":", "None")


table = DoubleHashingHashTable(10)
table.insert(12)
table.insert(25)
table.insert(35)
table.display()
print()
table.delete(25)
table.display()
