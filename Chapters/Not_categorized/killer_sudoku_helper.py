from itertools import combinations_with_replacement

def combinations(target, size, exclude):
    numbers = [1,2,3,4,5,6,7,8,9]
    final = []

    if exclude is not None:
        for item in exclude:
            numbers.pop(numbers.index(item))

    for i in range(size+1):
        combos = combinations_with_replacement(numbers, i)
        for combo in combos:
            if sum(combo) == target and len(list(set(combo))) == size:
                final.append(sorted(combo))
                # return final

    return final



