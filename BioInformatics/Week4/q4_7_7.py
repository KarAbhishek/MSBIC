from BioInformatics.Week4.scoring import score
from BioInformatics.Week4.q4_6_6 import mass, parent_mass, expand

def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leaderboard = set([''])
    leader_peptide = ''
    while leaderboard is not None:
        leaderboard = expand(leaderboard)
        for pep_idx, peptide in enumerate(leaderboard):
            if mass(peptide) == parent_mass(spectrum):
                if score(peptide, spectrum) > score(leader_peptide, spectrum):
                    leader_peptide = peptide
                elif mass(peptide) > parent_mass(spectrum):
                    del leaderboard[pep_idx]
            leaderboard = trim(leaderboard, spectrum, n)
        print(leader_peptide)

def trim(leaderboard, spectrum, n, amino_acid, amino_acid_mass):
    linear_scores = [0 for i in range(1, leaderboard)]
    for j in range(1, leaderboard):
        peptide = leaderboard[j]
        linear_scores[j] = score(peptide, spectrum)
    leaderboard.sort(reversed)
    linear_scores.sort(reversed)
    for j in range(n+1, len(leaderboard)):
        if linear_scores(j) < linear_scores(n):
            del leaderboard[j:]
        return leaderboard
    return leaderboard