def spiral_matrix(size):
    final = []
    i = size
    loops = 0
    group = []
    tmp_group = []
    numbers = [i for i in range(1,(size*size)+1)]
    if size == 0 :
        return []
    else:
        while len(numbers) > 0:
            for item in range(i):
                tmp_group.append(numbers[item])

            group.append(tmp_group)
            tmp_group = []
            for item in range(i):
                numbers.pop(0)

            if loops in [0,2]:
                i -= 1
                if loops == 0:
                    loops += 1
                elif loops == 2:
                    loops -= 1
            else:
                loops += 1
    test1="STOP"
    return final