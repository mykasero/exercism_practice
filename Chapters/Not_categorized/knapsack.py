import itertools
def maximum_value(maximum_weight, items):
    max_val = 0
    total = 0

    if items == []:
        return max_val

    else:

        weights = [item["weight"] if item["weight"] <= maximum_weight else "X" for item in items]

        if len(weights) == 1 and weights[0] == "X":
            return max_val

        values = [item["value"] for item in items]


        totals_list = values.copy()

        if max(weights) == maximum_weight:
            totals_list.append(values[weights.index(max(weights))])

        test1 = tuple()
        test2 = tuple()
        total_wt = 0

        indexes = [i for i in range(len(items))]

        r = 1
        while r < len(weights):
            x = itertools.combinations(weights, r)
            y = itertools.combinations(values, r)
            for i_x, i_y in zip(x, y):
                total_wt = sum(i_x)

                if total_wt <= maximum_weight:
                    total_val = sum(i_y)
                    totals_list.append(total_val)
                else:
                    total_wt = 0
                    total_val = 0

            r += 1


        return max(totals_list)


