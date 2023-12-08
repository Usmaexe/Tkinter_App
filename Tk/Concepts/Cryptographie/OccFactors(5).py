import importlib
Occurence_module = importlib.import_module("Occurence(4)")
occ = Occurence_module.occ

def keyLen(occs,length) : 
	#length is used to verify that we divise each number on the max of spacing
	factors = []
	for key,value in occs.items() :
		factor=[]
		if(len(value)==1) :
			for i in range(2,length) :
				if value[0] % i ==0 and len(factor) != 2:
					factor.append(i)
		else : 
			for item in value :  
				for i in range(2,length) : 
					if item%i == 0 : 
						factor.append(i)
			numbers = {nb:0 for nb in factor}
			max1 = 0
			max2 = 0
			for number in numbers : 
				if number in factor : 
					numbers[number] += 1
				if numbers[number]> max1 : 
					max1 = number	
			numbers.pop(max1)
			for number in numbers : 
				if numbers[number]>max2 : 
					max2 = number
			factor=[max1,max2] 
				
		if len(factor) >= 2 : 
			factors.append(factor)
	dict_factors = {tuple(factor) : 0 for factor in factors}
	for factor in factors : 
		if tuple(factor) in dict_factors.keys() : 
			dict_factors[tuple(factor)] += 1
	keylengths = []
	for key,value in dict_factors.items():
		if(value>2):
			keylengths.append(key)

	return keylengths
					
if __name__ == '__main__' : 
	txt = 'Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvifa ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsve Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdnya tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd hce sxboglavs kvy zm ion tjmmhzd. Sa at Haq 2012 i bfdvsbq azmtmdg widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd.'
	nbOfOccurences = occ(txt)
	print(keyLen(nbOfOccurences,len(txt)))