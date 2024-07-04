from itertools import permutations

def can_chain(dominoes):
    if not dominoes:
        return []

    if len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None

    for chain in permutations(dominoes):
        if working(chain):
            return working(chain)

    return None

def working(chain):
    links = [chain[0]]

    for domino in chain[1:]:
        if links[-1][1] == domino[0]:
            links.append(domino)

        elif links[-1][1] == domino[1]:
            links.append((domino[1], domino[0]))

    if (len(links) == len(chain) and links[0][0] == links[-1][1]):
        return links
