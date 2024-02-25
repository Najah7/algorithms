class QuadraticAddressHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def quadratic_probing(self, key, i):
        return (self.hash(key) + i * i) % self.size

    def insert(self, key):
        index = self.hash(key)
        i = 1
        while self.table[index] is not None:
            index = self.quadratic_probing(key, i)
            i += 1
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        i = 1
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = self.quadratic_probing(key, i)
            i += 1
        return None

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = None

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(i, ":", self.table[i])
            else:
                print(i, ":", "None")


table = QuadraticAddressHashTable(10)
table.insert(12)
table.insert(25)
table.insert(35)
table.display()
print()
table.delete(25)
table.display()
