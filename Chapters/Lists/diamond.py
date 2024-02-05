def rows(letter):

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = letters.index(letter)
    rows = list(range(n)) + list(range(n, -1, -1))
    print(rows)
    def get_row(i):
        chars = [' '] * len(rows)
        chars[n + i] = chars[n - i] = letters[i]
        print(chars)
        return ''.join(chars)

    return list(map(get_row, rows))