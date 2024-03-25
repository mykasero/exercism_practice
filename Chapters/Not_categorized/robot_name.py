import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "U", "P", "R", "S",
           "T", "Q", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Robot:
    def __init__(self):
        self.name = ""
        self.name_list = []

        for i in range(5):
            if i < 2:
                self.name += letters[random.randint(0, len(letters) - 1)]
            else:
                self.name += numbers[random.randint(0, len(numbers) - 1)]

        self.name_list.append(self.name)

    def reset(self):
        self.name = ""
        for i in range(5):
            if i < 2:
                self.name += letters[random.randint(0, len(letters) - 1)]
            else:
                self.name += numbers[random.randint(0, len(numbers) - 1)]

        if self.name in self.name_list:
            self.name = ""
            random.seed(random.randint(0, 999))
            for i in range(5):
                if i < 2:
                    self.name += letters[random.randint(0, len(letters) - 1)]
                else:
                    self.name += numbers[random.randint(0, len(numbers) - 1)]
