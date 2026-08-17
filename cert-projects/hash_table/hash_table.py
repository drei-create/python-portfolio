class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        total = 0
        for character in key:
            total = total + ord(character)
        return total

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
        return None

table = HashTable()
table.add("name", "Aldrei")
table.add("role", "Computer Engineer")
print(table.lookup("name"))
print(table.lookup("role"))
print(table.lookup("missing"))
