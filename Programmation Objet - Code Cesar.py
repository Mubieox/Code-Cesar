class CodeCesar:
    def __init__(self,cle):
        self.cle=cle
        self.alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def decale(self,lettre):
        num1=self.alphabet.find(lettre)
        num2=num1+self.cle
        if num2>=26:
            num2-=26
        if num2<0:
            num2+=26
        nouvelle_lettre=self.alphabet[num2]
        return nouvelle_lettre
    
    def cryptage(self,texte):
        nouveaux_texte=""
        for lettre in texte:
            nouveaux_texte+=self.decale(lettre)
        return nouveaux_texte
    
    def transforme(self,texte):
        self.cle=-self.cle
        message=self.cryptage(texte)
        self.cle=-self.cle
        return message

cle_de_chiffrement=int(input("Veuillez rentrer la clé de chiffrement : "))
code=CodeCesar(cle_de_chiffrement)
texte=input("Veuillez rentrer un texte à chiffrer : ")
print(code.cryptage(texte))