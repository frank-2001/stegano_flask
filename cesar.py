def cesar(text, shift, mode="encrypt"):
    """
    Chiffre ou déchiffre le texte donné en utilisant l'algorithme de César.

    Args:
        text (str): Le texte d'entrée à chiffrer ou déchiffrer.
        shift (int): La valeur de décalage (clé) pour le chiffrement.
        mode (str, facultatif): Le mode ("encrypt" ou "decrypt"). Par défaut, c'est "encrypt".

    Returns:
        str: Le texte chiffré ou déchiffré.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Détermine la direction du décalage en fonction du mode
            if mode == "encrypt":
                shift_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            elif mode == "decrypt":
                shift_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            else:
                raise ValueError("Mode invalide. Utilisez 'encrypt' ou 'decrypt'.")
            # Conserve la casse d'origine
            if char.isupper():
                shift_char = shift_char.upper()
            result += shift_char
        else:
            # Garde les caractères non alphabétiques inchangés
            result += char
    return result

def test():
    print("Clear : Test | Crypted : ",cesar("Test",4))

test()
