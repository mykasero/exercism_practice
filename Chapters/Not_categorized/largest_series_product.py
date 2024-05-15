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