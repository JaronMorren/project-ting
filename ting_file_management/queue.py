from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    # Initializes the Queue object
    def __init__(self):
        # Creates an empty list to store the data
        self._data = []

    def __len__(self):
        # Returns the length of the data list
        return len(self._data)

    def enqueue(self, value):
        # Appends the value to the data list
        self._data.append(value)

    def dequeue(self):
        # Checks if the queue is empty
        if len(self._data) == 0:
            # Returns None if the queue is empty
            return None
        # Removes and returns the first element
        #  from the data list (FIFO behavior)
        return self._data.pop(0)

    def search(self, index):
        # Checks if the index is out of bounds
        if index < 0 or index >= len(self._data):
            # Raises an IndexError if the index is invalid or nonexistent
            raise IndexError("Índice Inválido ou Inexistente")
        # Returns the element at the specified index in the data list
        return self._data[index]


# https://github.com/tryber/sd-025-b-live-lectures
# /blob/lecture/cs/3.4/my_queue.py
