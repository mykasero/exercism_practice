def saddle_points(matrix):
    res = []
    if len(matrix) != 0:
        try:
            matrix_trans = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
            print(matrix_trans)
        except IndexError:
            raise ValueError("irregular matrix")
        for num, i in enumerate(matrix):
            for enum, k in enumerate(matrix_trans,1):
                print("NUM = ", num, " i = ", i, " enum = ", enum, " k = ", k)
                if k[num] == max(i) and k[num] == min(k):
                    res.append({"row": num+1,"column":enum })

    return(res)