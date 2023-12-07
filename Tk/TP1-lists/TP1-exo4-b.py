from load_dictionary import load

wdss = load("2of4brif.txt")

					
def palingrames(mots):
	pali_list=[]
	for mot in mots : 
		end = len(mot)
		rev_word = mot[::-1]
		if end > 1 :
			for i in range(end):	
				if mot[i:]==rev_word[:end - i] and rev_word[end - i:] in mots:
					pali_list.append((mot,rev_word[end-i:]))
				if mot[:i]==rev_word[end - i:] and rev_word[:end - i] in mots:
					pali_list.append((rev_word[:end - i],mot))
	return pali_list

print(palingrames(wdss))
