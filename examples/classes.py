# Sınıflar ve Nesne Tabanlı Programlama

class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgi(self):
        print(f'Araba: {self.marka} {self.model}')

araba1 = Araba('Toyota', 'Corolla')
araba1.bilgi()
