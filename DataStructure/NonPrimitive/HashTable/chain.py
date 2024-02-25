import typing as t


class ChainedHashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # for chaining


class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.table: t.List[t.Optional[ChainedHashTableEntry]] = [None] * size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:  # when bucket is empty
            self.table[index] = ChainedHashTableEntry(key, value)
        else:  # bucket already exists
            current = self.table[index]
            if current.key == key:  # key already exists
                current.value = value
                return

            while current.next:
                current = current.next
            current.next = ChainedHashTableEntry(key, value)

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # key not found

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return
            previous = current
            current = current.next

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            print(f"{i}:", end=" ")
            while current:
                print(f"{current.key}:{current.value}", end=" -> ")
                current = current.next
            print("None")

    def _hash(self, key):
        return hash(key) % self.size


hash_table = ChainedHashTable(size=10)
hash_table.insert("test", 42)
hash_table.insert("make", 17)
hash_table.insert("test", 99)  # overwrite

# search
result_test = hash_table.search("test")
result_make = hash_table.search("make")
result_unknown = hash_table.search("unknown")

print(result_test, result_make, result_unknown)
hash_table.display()
