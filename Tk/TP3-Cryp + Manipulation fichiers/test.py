import string
def suggerer_corrections(mot, vocabulaire, corpus):
    if mot in vocabulaire:
        return [mot]  # Le mot est présent dans le vocabulaire, donc on le suggère tel quel
    else:
        suggestions = []
        # Correction en modifiant une seule lettre
        for i in range(len(mot)):
            for lettre in string.ascii_lowercase:
                nouveau_mot = mot[:i] + lettre + mot[i+1:]
                if nouveau_mot in corpus:
                    suggestions.append(nouveau_mot)
        
        if suggestions:
            return suggestions  # Des suggestions valides ont été trouvées en modifiant une seule lettre
        
        # Correction en modifiant deux lettres
        for i in range(len(mot)):
            for j in range(i+1, len(mot)):
                for lettre1 in string.ascii_lowercase:
                    for lettre2 in string.ascii_lowercase:
                        nouveau_mot = mot[:i] + lettre1 + mot[i+1:j] + lettre2 + mot[j+1:]
                        if nouveau_mot in corpus:
                            suggestions.append(nouveau_mot)
        
        if suggestions:
            return suggestions  # Des suggestions valides ont été trouvées en modifiant deux lettres
        
        return [mot]  # Aucune suggestion valide trouvée, on renvoie le mot saisi tel quel

vocabulaire = ["chat", "chien", "maison", "ordinateur", "voiture"]
corpus = ["chat", "chien", "maison", "ordinateur", "voiture", "chaise", "table"]

mot_saisi = "dys"

suggestions = suggerer_corrections(mot_saisi, vocabulaire, corpus)

print("Suggestions de corrections pour le mot", mot_saisi)
print(suggestions)