def distance(tab,w1,w2) : 
	if len(w1) == 0 and len(w2) ==0 : 
		return 0
	elif len(w1) == 0 or len(w2) == 0 : 
		return abs(len(w1)-len(w2))
	else : 
		return remplire_tab(tab,w1,w2,len(w1),len(w2))
def remplir_tab(tab,w1,w2,l1,l2) : 
	if(w1[:l1]!=w2[:l2] and l1==1 and l2==1):
		return 2
	elif(l1<l2 or l1>l2):
		return abs(l1-l2) + remplir_tab(tab,w1,w2,abs(l1-l2),abs(l1-l2))
	else : 
		for i in range(l1) : 
			for j in range(l2):
				tab[i][j] = remplire_tab(w1,w2,i,j)

if __name__ == "__main__"  : 
	word1 = "stay"
	word2 = "play"
	distances[0][] = [for i in range(len(word1))]
	ditstances[][0] = [for i in range(len(word2))]
	print(distance(tab,word1,word2))