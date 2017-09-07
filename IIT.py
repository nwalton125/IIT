from math import log

def entropy(dist):
	total = 0
	for i in dist:
		total += dist[i] * log(dist[i], 2)
	return -1 * total

#Returns the string consisting of the elements of pos, in the order given by pos.
def str_slice(s, pos):
	new_s = "a"*len(pos)
	for i in range(len(pos)):
		new_s[pos[i]] = s[i]
	return new_s

print(str_slice("HMMOORSU", (3,0,7,5,6,4,2,1)) == "MUSHROOM")

print(str_slice("HOMMOUS", (4,2,3,1)) == "MOMH")

#Finds all strings of length n formable from the given alphabet.
def n_strings(n, alphabet):
	if n == 0:
		return [""]
	else:
		smaller_strings = n_strings(n-1, alphabet)
		all_strings = []
		for char in alphabet:
			for s in smaller_strings:
				all_strings.append(char + s)
		return all_strings

print(n_strings(3, ["a", "k"]) == ["aaa", "aak", "aka", "akk", "kaa", "kak", "kka", "kkk"])

#Variables: seta is the set of positions of the set A, setb is the set of positions of the set B, bstring is the set of fixed characters in bstring, f is the state transition function, and alphabet is the character set.

#Finds EI(A -> B) = H(z_B | A random, y_B = x_B). i.e. the set of characters in B is fixed and we vary A to see what happens when we update the whole string based on an update function.
def ei(seta, setb, bstring, f, alphabet):
	str_probs = {}
	prob_scale_factor = len(alphabet) ** len(seta)
	for astring in n_strings(len(seta), alphabet):
		full_string = reorder_string(astring + bstring, seta + setb)
		if full_string not in str_probs:
			str_probs[full_string] = 0
		str_probs[full_string] += 1
	for s in str_probs:
		str_probs[s] /= prob_scale_factor
	return entropy(str_probs)

#Finds the phi value for the specific partition a, b of our string x
def phiab(seta, setb, x, f, alphabet):
	return ei(seta, setb, )


