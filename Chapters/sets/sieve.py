def primes(limit):
    p=2
    final = []
    marked_list = []
    total_list = []
    for i in range(p,limit+1):
        total_list.append(i)
    if limit >= p:
        final.append(p)
    while len(marked_list) + len(final) < len(total_list):
        for iter1 in range(2*p,limit+1,p):
            marked_list.append(iter1)
        marked_list = list(set(marked_list))

        print(marked_list)

        for iter2 in total_list:
            if iter2 > p and iter2 not in marked_list:
                p = iter2
                final.append(p)
                break
        if p == 997:
            break
        print(p)

    return final
