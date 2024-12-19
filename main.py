"""
Classe qui permet de déterminer si une chaîne est un palindrome.
"""

def ispalindrome(text):
    """
    Teste si une chaîne est un palindrome.
    Ignore les accents, la casse, les espaces et les caractères non alphanumériques.
    """

    # Dictionnaire pour remplacer les caractères accentués par leurs équivalents non accentués
    accents = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ç': 'c',
        'É': 'e', 'È': 'e', 'Ê': 'e', 'Ë': 'e',
        'À': 'a', 'Â': 'a', 'Ä': 'a',
        'Ù': 'u', 'Û': 'u', 'Ü': 'u',
        'Î': 'i', 'Ï': 'i',
        'Ô': 'o', 'Ö': 'o',
        'Ç': 'c'
    }

    # Convertir la chaîne en minuscules
    text = text.lower()
    cleaned_text = ""

    # Nettoyer la chaîne
    for char in text:
        # Remplacer les caractères accentués par leurs équivalents non accentués
        char = accents.get(char, char)
        # Conserver uniquement les caractères alphanumériques
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            cleaned_text += char

    # Comparer la chaîne nettoyée avec son inverse
    return cleaned_text == cleaned_text[::-1]


#### Fonction principale




def main():

    """
    permet clear'appeler la fonction ispalyndrome et de la tester
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()