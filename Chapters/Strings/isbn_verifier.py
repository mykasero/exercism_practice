def is_valid(isbn):
    is_true = False
    numbers_conditional = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    undesirable_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "U", "P", "R",
                           "S", "T", "Z", "Y"]
    numbers = []

    if "-" in isbn:
        isbn = isbn.replace("-", "")
    else:
        pass

    if isbn == "" or len(isbn) < 10 or len(isbn) > 10 or isbn[len(isbn) - 1] in undesirable_letters:
        return False

    for i in range(10):
        if isbn[i] == 'X' and i == 9:
            numbers.append("10")
        elif isbn[i] == "X" and i < 9 or not isbn[i] in numbers_conditional and i < 9:
            return False

        else:
            numbers.append(isbn[i])

    isbn_sum = isbn_sum = int(numbers[0]) * 10 + int(numbers[1]) * 9 + int(numbers[2]) * 8 + int(numbers[3]) * 7 + int(
        numbers[4]) * 6 + int(numbers[5]) * 5 + int(numbers[6]) * 4 + int(numbers[7]) * 3 + int(numbers[8]) * 2 + int(
        numbers[9]) * 1

    if isbn_sum % 11 == 0:
        is_true = True

    return is_true