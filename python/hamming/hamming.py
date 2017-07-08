def distance(A, B):
	"""Calculate the Hamming difference between two DNA strands."""

	def chunks(s, n):
		"""Produce `n`-character chunks from `s`."""
		for start in range(0, len(s), n):
		    yield s[start:start+n]

	a = []
	for chunk in chunks(A, 1):
		a.append(chunk)				

	b = []
	for chunk in chunks(B, 1):
		b.append(chunk)				
	
	n=0
	
	if len(a) != len(b):
		raise ValueError
	else:
		for i in range(len(a)):
			if a[i] != b[i]:
				n += 1

	return n

print(distance("A", "A"))