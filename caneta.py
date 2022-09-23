class Caneta:
    
    def __init__(self, cor, tipo_ponta, marca):
        
        self.cor = cor
        self.tipo_ponta = tipo_ponta
        self.marca = marca
    
    def risca(self):
        joaozinho = self.cor
        juquinha = self.tipo_ponta
        mariazinha = self.marca       
        return f"Minha caneta risca com a cor {joaozinho}, é do tipo {juquinha} e da marca {mariazinha}"


caneta_azul = Caneta("azul","esferográfica","bic")
caneta_de_rico = Caneta("preta","tinteira","montblanc")
caneta_de_pena = Caneta("vermelha","pena","sem marca")

print(caneta_azul.risca())
print(caneta_de_rico.risca())
print(caneta_de_pena.risca())