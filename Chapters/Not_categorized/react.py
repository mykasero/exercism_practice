class InputCell:
    def __init__(self, initial_value):
        self._callbacks = []
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for c in self._callbacks:
            c(self._value)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.input = inputs
        self.function = compute_function
        self.value = 0


    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
    