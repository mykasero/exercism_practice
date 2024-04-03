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
'''
nstructions
Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:

9 8 7
5 3 2
6 6 7
representing this matrix:

    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
your code should be able to spit out:

A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.
The rows for our example matrix:

9, 8, 7
5, 3, 2
6, 6, 7
And its columns:

9, 5, 6
8, 3, 6
7, 2, 7
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/matrix/canonical-data.json
