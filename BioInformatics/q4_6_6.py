def non_consistent(peptide, spectrum):
    return

def mass(peptide):
    return

def expand(peptides):
    return

def parent_mass(spectrum):
    return spectrum[-1]

def cyclopeptide_sequencing(spectrum):
    peptides = set('')
    while peptides not None:
        peptides = expand(peptides)
        for pep_idx, peptide in enumerate(peptides):
            if mass(peptide) == parent_mass(spectrum):
                if cyclospectrum(peptide) == spectrum:
                    print(peptide)
                del peptides[pep_idx]
            else if non_consistent(peptide, spectrum):
                del peptides[pep_idx]

