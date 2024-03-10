def distance(strand_a, strand_b):
    diffs = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for letter_pos in range(len(strand_a)):
            if strand_a[letter_pos] != strand_b[letter_pos]:
                diffs += 1

    return diffs

'''
Instructions
Calculate the Hamming Distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information. 
If we compare two strands of DNA and count the differences between them we can see how many mistakes occurred. This is known as the "Hamming Distance".

We read DNA using the letters C,A,G and T. Two strands might look like this:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
They have 7 differences, and therefore the Hamming Distance is 7.

The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to be familiar with :)

Implementation notes
The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work.

This particular exercise requires that you use the raise statement to "throw" a ValueError when the strands being checked are not the same length. The tests will only pass if you both raise the exception and include a message with it.

# When the sequences being passed are not the same length.
raise ValueError("Strands must be of equal length.")

'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/hamming/canonical-data.json
