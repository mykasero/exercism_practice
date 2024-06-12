#STATUS 5/7 PASSED

from itertools import combinations as cwr
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


        totals_list = values

        if max(weights) == maximum_weight:
            totals_list.append(values[weights.index(max(weights))])

        test1 = tuple()
        test2 = tuple()
        total_wt = 0

        indexes = [i for i in range(len(items))]

        r = 2
        while r < len(values):
            ind_test = cwr(indexes,r)

            for i in ind_test:
                test1 = (weights[i[0]],weights[i[1]])
                test2 = (values[i[0]],values[i[1]])

                total_wt += sum(test1)

                if total_wt <= maximum_weight:
                    total += sum(test2)
                else:
                    totals_list.append(total)
                    total_wt = 0
                    total = 0


                    total_wt += sum(test1)
                    if total_wt <= maximum_weight:
                        total += sum(test2)

            r += 1




        TEST_MAX = max(totals_list)
        STOP = "TEST"

        return max(totals_list)


