from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Retourne la somme de a et b.
    Supporte int et float.
    """
    return a + b

def is_palindrome(s: str) -> bool:
    """
    Vérifie si la chaîne s est un palindrome.
    Ignore la casse et les caractères non alphanumériques.
    Exemple: "A man, a plan, a canal: Panama" -> True
    """
    # Normalisation : garder uniquement les lettres/chiffres en minuscule
    normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]

