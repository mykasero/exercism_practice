def flatten(iterable):
    final = []

    for item in iterable:
        if isinstance(item,list):
            final.extend(flatten(item))
        elif item is not None:
            final.append(item)

    return final