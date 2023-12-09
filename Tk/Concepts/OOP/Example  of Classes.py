class voiture:
    @classmethod
    def listev(cls):
        return ["audi","bmw"]
    def __init__(self,m="abc",p=1000):
        self.matricule=m
        self.prix=p
    def infosv(self):
        print("prix : " ,self.prix)
    def __eq__(self, other):
        return self.matricule==other.matricule
    def __repr__(self):
        return "voiture " + self.matricule
    def __str__(self):
        return "voiture " + self.matricule
    def augmenterprix(self,a):
        self.prix=self.prix+a
v1= voiture(m="abc",p=3000)
v2=voiture(m="abc",p=2000); v2.prix=3000; print(v1==v2)
print(voiture.listev())
print(v2)
class QuatreQuatre(voiture):
    def __init__(self,m="abc",p=3000,cm=1000):
        self.matricule=m
        self.prix=p
        self.chargemax=1000
    def infosvq(self):
        return super().infosv() + "chargemax :"
vq= QuatreQuatre()
vq.augmenterprix(300)
vq.infosv()

