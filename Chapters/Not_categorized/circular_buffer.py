class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity

    def read(self):
        items = {}
        if any(self.buffer) == False:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            for item in self.buffer:
                if item != None:
                    self.buffer[self.buffer.index(item)] = None
                    return item
                    break

    def write(self, data):
        if all(self.buffer) == True:
            raise BufferFullException("Circular buffer is full")
        else:

            for spot in range(len(self.buffer)):
                if self.buffer[spot] == None:
                    self.buffer[spot] = data
                    break

    def overwrite(self, data):

        if all(self.buffer) == False:
            for spot in range(len(self.buffer)):
                if self.buffer[spot] == None:
                    self.buffer[spot] = data
                    break
        elif all(self.buffer) == True:

            self.buffer[self.buffer.index(min(self.buffer))] = data

    def clear(self):
        for item in self.buffer:
            if item != None:
                self.buffer[self.buffer.index(item)] = None
