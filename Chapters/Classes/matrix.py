class Matrix:
    def __init__(self, matrix_string):
        self.string = matrix_string
        self.string_split = ""
        self.sub_list = []
        self.matrix = []
        self.temp_list = []
        self.column_list = []
        self.iter_list = 0
        self.iter_item = 0

    def row(self, index):
        self.string_split = self.string.split("\n")

        for item in self.string_split:
            self.sub_list.append(item.split())

        for numbers in self.sub_list:
            self.matrix.append(list(map(int, numbers)))

        return self.matrix[index - 1]

    def column(self, index):
        if len(self.string) == 1:
            return [int(self.string[0])]
        else:
            self.string_split = self.string.split("\n")

            for item in self.string_split:
                self.sub_list.append(item.split())

            for numbers in self.sub_list:
                self.matrix.append(list(map(int, numbers)))

            while len(self.column_list) < len(self.matrix[0]):
                if len(self.temp_list) < 3:
                    self.temp_list.append(self.matrix[self.iter_list][self.iter_item])
                    self.iter_list += 1
                else:
                    self.column_list.append(self.temp_list)
                    self.temp_list = []
                    self.iter_item += 1
                    self.iter_list = 0

            return self.column_list[index - 1]
