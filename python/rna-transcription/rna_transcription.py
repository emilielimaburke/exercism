
def to_rna(dna_strand):
	"""Given a DNA strand, return its RNA complement (per RNA transcription)."""
	rna_strand = ""
	for letter in dna_strand:
		if letter == "G":
			rna_strand += "C"
		elif letter == "C":
			rna_strand += "G"
		elif letter == "T":
			rna_strand += "A"
		elif letter == "A":
			rna_strand += "U"
		else:
			return ""
	return rna_strand