class LinearAddressHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            index = index + 1
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = index + 1
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


table = LinearAddressHashTable(10)
table.insert(12)
table.insert(25)
table.insert(35)
table.display()
