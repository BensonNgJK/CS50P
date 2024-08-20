class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{'🍪'*self.size}"

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Exceeded Jar capacity")
        if size < 0:
            raise ValueError("Not enough cookies")
        self._size = size

