def proteins(strand):
    cod_2_protein = {"AUG" : "Methionine", "UUU" : "Phenylalanine","UUC" : "Phenylalanine",
                    "UUA" : "Leucine", "UUG" : "Leucine", "UCU" : "Serine","UCC" : "Serine","UCA" : "Serine","UCG" : "Serine",
                    "UAU" : "Tyrosine","UAC" : "Tyrosine", "UGU" : "Cysteine","UGC" : "Cysteine",
                    "UGG" : "Tryptophan", "UAA" : 0,"UAG" : 0,"UGA" : 0}
    sample = ""
    final = []


    for words in range(int(len(strand)/3)):
        for letter in range(0 + (words * 3),3 + (words*3)):
            sample+= strand[letter]
        if sample in cod_2_protein.keys() and cod_2_protein[sample] != 0:
            final.append(cod_2_protein[sample])
            sample = ""
        elif cod_2_protein[sample] == 0:
            break

    return final
