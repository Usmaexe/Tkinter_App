def occ(word):
	seq={}
	i=0
	while i < len(word) : 
		for j in range(i+1,len(word)) : 
			lets = "";distance = 0
			#Check if 2 letter in the word are repeated or not 
			if(word[i]==word[j]):
				lets+=word[i]
				Founded = True
				t=1
				#To verify if a sequence of letter is the same as the other on index j
				while((Founded) and (j+t < len(word))):
					if(word[i+t]==word[j+t]):
						lets+=word[i+t]
						t+=1
					else : 
						Founded = False
				#A sequnce of word of size bigger than 1 is founded
				if(t!=1) :
					Distance = j - i
					#If another sequence of word is founded the distance is added to the dictionnary
					if(lets in seq and len(lets)>=3):
						seq[lets].append(Distance)
					#IF NOT THE DISTANCE IS ADDED WITH A KEY THAT REPRESENT THE SEQUENCE TO THE DICTIONNARY
					elif(len(lets)>=3):
						seq[lets] = [Distance]
		i+=len(lets)+1
	return seq
if __name__ == '__main__' : 
	print(occ('Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvifa ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsve Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdnya tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd hce sxboglavs kvy zm ion tjmmhzd. Sa at Haq 2012 i bfdvsbq azmtmdg widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd.'))