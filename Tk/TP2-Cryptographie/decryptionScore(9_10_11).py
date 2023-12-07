import string as st
import importlib

Score_module = importlib.import_module("OccScore(7)")
sc = Score_module.score

def decrypted_text(txt,key) : 
	decrypted = ""
	for letter in txt : 
		if letter in st.ascii_lowercase : 
			#instead of using the cryption alogrithm of the first exercice thissimple alogirhtm is on that is used
			dletter = chr((ord(letter) - ord(key) - ord('a'))%26 + ord('a')) 
			decrypted += dletter
		elif letter in st.ascii_uppercase : 
			dletter = chr((ord(letter) - ord(key) - ord('A'))%26 + ord('A'))
			decrypted += dletter
		else : 
			decrypted += letter
	return decrypted	
def key_score(txt) : 
	max_score = 0
	best_key = ""
	for letter in st.ascii_lowercase : 
		decrypted = decrypted_text(txt,letter)
		score = sc(decrypted)
		if score>max_score:
			best_key = letter
			max_score = score
	return best_key
if __name__ == "__main__" : 
	crypted = "Jxu dbu qdph lv dqg rqh khdowk frxuvh wkh wklqjv zlwk d yhu\ndwwdfn rqh glvsod\ndwlrq ri wkh fubsw"
	best_key = key_score(crypted)
	print(decrypted_text(crypted,best_key))