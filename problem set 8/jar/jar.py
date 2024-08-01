class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Something wrong")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("out of capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("No cookie left")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value > 12:
            raise ValueError("Only 12 cookies fix")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value > self._capacity or value < 0:
            raise ValueError("no cookies or out ot capacity")