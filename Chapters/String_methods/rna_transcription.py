def to_rna(dna_strand):
    rna_strand = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_conv = ""

    if dna_strand == "":
        pass
    else:
        for gene in dna_strand:
            rna_conv += rna_strand[gene]

    return rna_conv
