
######################################################
############# BIBLIOTHEQUE - FONCTIONS ###############
######################################################

def codage(caractere, decalage):
    caractere = ord(caractere)

    if 65 <= caractere <= 90:  # Majuscules (A-Z)
        caractere_code = caractere + decalage
        if caractere_code > 90:
            caractere_code -= 26 # Si caractère dépasse z ( code asci 122), on fait revenir la lettre au début de l'alphabet
        return chr(caractere_code)

    elif 97 <= caractere <= 122:  # Minuscules (a-z)
        caractere_code = caractere + decalage
        if caractere_code > 122:
            caractere_code -= 26
        return chr(caractere_code)

    else:
        return chr(caractere)  # Autres caractères inchangés



###########################################
############# CODE PRINCIPAL ##############
###########################################

question = input("Voulez-vous coder un message ? o/n : ")
if question == "o":
    message = input("Entrez le message : ")
    decalage = 3
    message_code = ""

    # Parcours chaque lettre du message pour la coder
    for lettre in message:
        message_code += codage(lettre, decalage)

    print("Message codé : ", message_code)
    
elif question == "n":
    print("A bientôt")
