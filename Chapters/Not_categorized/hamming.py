def distance(strand_a, strand_b):
    diffs = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for letter_pos in range(len(strand_a)):
            if strand_a[letter_pos] != strand_b[letter_pos]:
                diffs += 1

    return diffs
