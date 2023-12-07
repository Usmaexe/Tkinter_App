def cryptedSeq(txt,length) : 
	sequences = ['']*length
	for i in range(len(txt)): 
		sequences[i%length] += txt[i]
	for i in range(len(sequences)) : 
		print(i+1,' ',sequences[i])
if __name__ == '__main__' :
	txt = str(input('Enter a crypted message : '))
	keyLen = int(input('Enter the length of the key :'))
	cryptedSeq(txt,keyLen)
