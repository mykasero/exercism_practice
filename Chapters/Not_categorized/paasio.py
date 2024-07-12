import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model.

    SUBCLASSING means you start the parent class,
    which has it's own methods and attributes.
    At '__init__', you have call the parent __init__ method:
        # python3 only, with self automatically supplied
        super().__init__(*args)

        # python2 compliant, NEVER user self.__class__ inside it!
        super(MeteredFile, self).__init__(*args)

        # Use the name of parent class directly
        # Note the (self)
        io.BufferedRandom.__init__(self, *args)

    If dealing with multiple inheritance, for example:
    class A(B, C):
        def __init__(self):
            B.__init__(self)
            C.__init__(self)

    Then you can wrap their methods, customizing them.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._read_calls = 0
        self._write_calls = 0

        self._bytes_written = 0
        self._bytes_read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        line = super().readline()
        if not line:
            raise StopIteration

        self._read_calls += 1
        self._bytes_read += len(line)
        return line

    def read(self, size=-1):
        total = super().read(size)
        self._read_calls += 1
        self._bytes_read += len(total)
        return total

    @property
    def read_bytes(self):
        return self._bytes_read

    @property
    def read_ops(self):
        return self._read_calls

    def write(self, b):
        size = super().write(b)
        self._write_calls += 1
        self._bytes_written += size
        return size

    @property
    def write_bytes(self):
        return self._bytes_written

    @property
    def write_ops(self):
        return self._write_calls


class MeteredSocket:
    """Implement using a delegation model.

    DELEGATION means that an attribute of self,
    in this example self._socket,
    will receive some methods passed to self.
    """

    def __init__(self, socket):
        self._socket = socket

        self._send_calls = 0
        self._bytes_sent = 0
        self._receive_calls = 0
        self._bytes_received = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        total = self._socket.recv(bufsize, flags)

        self._receive_calls += 1
        self._bytes_received += len(total)
        return total

    @property
    def recv_bytes(self):
        return self._bytes_received

    @property
    def recv_ops(self):
        return self._receive_calls

    def send(self, data, flags=0):
        size = self._socket.send(data, flags)

        self._send_calls += 1
        self._bytes_sent += size
        return size

    @property
    def send_bytes(self):
        return self._bytes_sent

    @property
    def send_ops(self):
        return self._send_calls