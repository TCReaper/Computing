class myHashTable():
    def __init__(self, length):
        self._array = [None] * length

    def insert(self, data):
        current_index = hash(data)
        while current_index < len(self._array) and self._array[current_index] != None:
            current_index += 1
        if self._array[current_index] == None:
            self._array[current_index] = data
        else:
            print("Insertion failed - Hash Table is full.")

    def find(self, data):
        current_index = hash(data)
        iterations = 0
        while self._array[current_index] != data and iterations <= len(self._array):
            if current_index == len(self._array) - 1:
                current_index = 0
            else:
                current_index += 1
            iterations += 1
        if self._array[current_index] == data:
            return current_index
        else:
            return -1
        
    def delete(self, data):
        index = self.find(data)
        if index < 0:
            return False
        else:
            self._array[index] = None
            return True



x = myHashTable(10)
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)
print(str(x.find(3)))
print(str(x.find(6)))
if x.delete(2):
    print("Deleted 2")
else:
    print("Failed to delete 2")
print(str(x.find(2)))
print(str(x.find(5)))


