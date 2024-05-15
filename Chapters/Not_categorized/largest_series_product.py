def largest_product(series, size):
    final = 0
    parts = []
    products = []
    sum_val = 1

    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    else:
        for item in series:
            if item not in ["0","1","2","3","4","5","6","7","8","9"]:
                raise ValueError("digits input must only contain digits")

        for i in range(len(series)):
            if i + size-1 >= len(series):
                break
            parts.append(series[i:i+size])

        for item in parts:
            for i in range(len(item)):
                sum_val *= int(item[i])

            products.append(sum_val)
            sum_val = 1

    final = max(products)

    return final

'''
Introduction
You work for a government agency that has intercepted a series of encrypted communication signals from a group of bank robbers. 
The signals contain a long sequence of digits. Your team needs to use various digital signal processing techniques to analyze the signals and 
identify any patterns that may indicate the planning of a heist.

Instructions
Your task is to look for patterns in the long sequence of digits in the encrypted signal.

The technique you're going to use here is called the largest series product.

Let's define a few terms, first.

input: the sequence of digits that you need to analyze
series: a sequence of adjacent digits (those that are next to each other) that is contained within the input
span: how many digits long each series is
product: what you get when you multiply numbers together
Let's work through an example, with the input "63915".

To form a series, take adjacent digits in the original input.
If you are working with a span of 3, there will be three possible series:
"639"
"391"
"915"
Then we need to calculate the product of each series:
The product of the series "639" is 162 (6 × 3 × 9 = 162)
The product of the series "391" is 27 (3 × 9 × 1 = 27)
The product of the series "915" is 45 (9 × 1 × 5 = 45)
162 is bigger than both 27 and 45, so the largest series product of "63915" is from the series "639". So the answer is 162.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/largest-series-product/canonical-data.json
