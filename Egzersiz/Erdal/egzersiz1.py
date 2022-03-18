class cokgen:
    def __init__(self,cokgenadi,kenarsayisi,acılistesi):
        self.cokgenadi = cokgenadi
        self.kenarsayisi = kenarsayisi
        self.acılistesi = acılistesi
    def cokgenadisoyle(self):
        print("Çokgen Adi",self.cokgenadi,"Kenar Sayısı", self.kenarsayisi, "Açı Listesi",self.acılistesi)
cokgen1 = cokgen("Üçgen","3",[30,60,90])
cokgen2 = cokgen("Kare","4",[90,90,90,90])
cokgen1.cokgenadisoyle()
cokgen2.cokgenadisoyle()
