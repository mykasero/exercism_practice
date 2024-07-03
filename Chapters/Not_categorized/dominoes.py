# STATUS 10/13 PASSED

def can_chain(dominoes):
    #sort reversed for easier pop

    dominoes = sorted(dominoes,key=lambda x: x[0])[::-1]

    if dominoes == []:
        return []
    else:
        new_dominoes = [dominoes.pop()]


    tmp_domino = []
    i= 1


    while dominoes != []: # THE CHAIN SHOULD BE CONTINUOUS, THERE ARE NO GROUPS OF CHAINS!!!
        tmp_domino = dominoes[-1]

        if i > len(dominoes):
            # new_dominoes = None
            break

        if new_dominoes[-1][1] == tmp_domino[0]:
            new_dominoes.append(tmp_domino)
            dominoes.pop()
            tmp_domino = []
            i=1

        else:
            tmp_domino = tmp_domino[::-1]

            if new_dominoes[-1][1] == tmp_domino[0]:
                new_dominoes.append(tmp_domino)
                dominoes.pop()
                tmp_domino = []
                i = 1
            else:
                new_dominoes[-1] = new_dominoes[-1][::-1]

                if new_dominoes[-1][1] == tmp_domino[0]:
                    new_dominoes.append(tmp_domino)
                    dominoes.pop()
                    tmp_domino = []
                    i = 1

                else:
                    tmp_domino = tmp_domino[::-1]

                    if new_dominoes[-1][1] == tmp_domino[0]:
                        new_dominoes.append(tmp_domino)
                        dominoes.pop()
                        tmp_domino = []
                        i = 1

                    else:
                        i += 1


    if dominoes == []:
        if (len(new_dominoes) == 1 and new_dominoes[0][0] != new_dominoes[0][1]) or len(new_dominoes) > 1 and new_dominoes[0][0] != new_dominoes[-1][1]:
            return None

        return new_dominoes

    else:
        return None


