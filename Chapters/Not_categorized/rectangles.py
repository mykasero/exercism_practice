def rectangles(s):
    rects = 0
    for y in range(len(s)):
        for x in range(len(s[0])):
            if s[y][x] == '+':
                for yi in range(y+1, len(s)):
                    if s[yi][x] == "+":
                        for xi in range(x+1, len(s[0])):
                            if s[yi][xi] == '+':
                                if s[y][xi] == '+' and \
                                    len(s[y][x+1:xi+1].replace('-', '').replace('+', '')) == 0 and \
                                        all((s[l][xi] in '+|') for l in range(y+1, yi+1)):
                                    rects += 1
                            elif s[yi][xi] != '-':
                                break
                    elif s[yi][x] != "|":
                        break
    return rects

'''
Instructions
Count the rectangles in an ASCII diagram like the one below.

   +--+
  ++  |
+-++--+
|  |  |
+--+--+
The above diagram contains 6 rectangles
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rectangles/canonical-data.json
