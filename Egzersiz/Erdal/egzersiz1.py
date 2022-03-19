class Cokgen:
    
    def __init__(self,cokgenadi,kenarsayisi,acılistesi):  
        self.cokgenadi = cokgenadi
        self.kenarsayisi = kenarsayisi
        self.acılistesi = acılistesi
        
    def cokgenAdiSoyle(self):
       print("Çokgenin Adı",self.cokgenadi,"Kenar Sayısı",self.kenarsayisi,"Açıları",self.acılistesi,"olan bir çokgendir.")

cokgen1 = Cokgen("Üçgen","3",[30,60,90])
cokgen2 = Cokgen("KareÜçgen","4",[90,90,90,90])
cokgen1.cokgenAdiSoyle()
cokgen2.cokgenAdiSoyle()

