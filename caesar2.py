def codage(caractere, decalage):
    caractere = ord(caractere) 
    if 65 <= caractere <= 90:
        caractere_code = caractere + decalage
        if caractere_code > 90:
            caractere_code -= 26
        return chr(caractere_code)
    else:
        return caractere

question = input("Voulez-vous coder un message ? (o/n) : ")

if question == "o":
    message = input("Rentrez le message à coder : ")
    decalage = 3
    message_code = ""

    for lettre in message:
        message_code += codage(lettre, decalage) 

    print("Message codé : ", message_code)
elif question == "n":
    print("A bientôt")
else:
    print("Veuillez entrer 'o' ou 'n'")
