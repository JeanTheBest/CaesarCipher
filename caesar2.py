

def codage(caractere, decalage):
    caractere= ord(caractere)
    if caractere>64 and caractere<91:
        caractere_code = chr(caractere+decalage)
        # *Attention ! Test et modification
        # pour les valeurs de caratere_code supérieures à 91
    return caractere_code

question = input("Voulez-vous coder un message ? (o/n)")
if question == "o":
    caractereUtilisateur = input("Rentrez le message à coder :")
    print (codage(caractereUtilisateur, 3))
elif question == "n":
    print("A bientôt")
else:
    print("rentrez 'o' ou 'n'")

