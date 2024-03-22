def slices(series, length):
    final = []
    ctr = 0
    digit = ""
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    elif length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif len(series) == 0:
        raise ValueError("series cannot be empty")
    else:
        while len(series)>= length:
            if ctr < length:
                digit += series[ctr]
                ctr += 1
            elif ctr == length:
                final.append(digit)
                digit = ""
                series = series.replace(series[0],"",1)
                ctr = 0


    return final

