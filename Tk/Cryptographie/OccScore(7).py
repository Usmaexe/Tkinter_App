import importlib

Occurence_module = importlib.import_module("LettreOcc(6)")
occ = Occurence_module.lettreOcc

def score(word) : 
	#letters REPRESENTS THE OCCURENCE OF EACH LETTER BY ORDER IN ANY TYPE OF TEXT
	letters = list('ETAOINSHRDLCUMWFGYPBVKJXQZ')
	target = letters[:6] + letters[len(letters)-6:]
	
	#Frequency REPRESENTS THE OCCURENCE OF EACH LETTER IN THE STRING WORD
	frequency = occ(word)
	frequency = frequency[:6] + frequency[len(frequency)-6:]
	score = 0
	for letter in target : 
		if(letter in frequency):
			score+=1
	return score
if __name__ == '__main__' : 
	print(score('rc ascwuiluhnviwuetnh,osgaa ice tipeeeee slnatsfietgi tittynecenisl. e fo f fnc isltn sn o a yrs sd onisli ,l erglei trhfmwfrogotn,l stcofiit. aea wesn,lnc ee w,l eIh eeehoer ros iol er snh nl oahsts ilasvih tvfeh rtira id thatnie.im ei-dlmf i thszonsisehroe, aiehcdsanahiec gv gyedsB affcahiecesd d lee onsdihsoc nin cethiTitx eRneahgin r e teom fbiotd n ntacscwevhtdhnhpiwru'))
