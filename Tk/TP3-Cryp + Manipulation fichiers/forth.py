def Delete(word) :
	words = []
	for letter in word : 
		if(letter != ' '): 
			result = word.replace(letter,"")
			words.append(result)
	return words


def Swap(word) :
	words = []
	if len(word) == 1:
		return [word]
	
	for i in range(len(word)) :
		for letter in Swap(word[:i] + word[i+1:]) : 	
			words.append(word[i]+letter)	
	return words			


def Replace(word) : 
	words = []
	for i in range(len(word)) :
		for j in range(97,123) : 
			w = word[:i] + chr(j) + word[i+1:]
			words.append(w)
	words = [w for w in words if w!= word]
	return words

def Add(word):
	words = []
	for i in range(len(word)+1):
		for j in range(97,123) : 
			w = word[:i] + chr(j) + word[i:]
			if not(w in words) : 
				words.append(w)
	words = [w for w in words if w!= word]
	return words

if __name__ == "__main__" : 

	##EACH OF THESE FUNCTIONS UTILIZES VARIOUS TECHNIQUES TO GENERATE 
	##WORDS THAT HAVE LETTERS SIMILAR TO THOSE IN A SPECIFIED WORD.
	
	#FUNCTION THAT DELETE A LETTER: 
	#print(Delete('nice game'))

	##FUNCTION THAT SWAP LETTERS USING RECURSIVITY:
	finalList = Swap('eat')
	finalList.remove('eat')
	#print(finalList)

	##FUNCTION THAT REMPLACE EACH LETTER 
	#print(Replace('can'))

	##FUNCTION THAT ADD A LETTER :
	#print(Add('at')) 

	##FUNCTION 
	swaping = Swap('at')
	swaping.remove('at')
	listGrp = Delete('dys') + swaping + Replace('dys') + Add('dys')
	print(sorted(listGrp))