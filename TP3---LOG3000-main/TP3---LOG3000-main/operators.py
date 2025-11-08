"""
Module contenant les opérations arithmétiques de base pour la calculatrice.
Chaque fonction prend deux nombres en entrée et retourne le résultat de l'opération.
"""

def add(a: float, b: float) -> float:
    """
    Additionne deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Soustrait deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Deuxième opérande
    
    Returns:
        float: La différence entre b et a (b - a)
    """
    return b - a

def multiply(a: float, b: float) -> float:
    """
    Calcule la puissance d'un nombre par un autre.
    
    Args:
        a (float): La base
        b (float): L'exposant
    
    Returns:
        float: Le résultat de a élevé à la puissance b (a ** b)
    """
    return a ** b

def divide(a: float, b: float) -> float:
    """
    Effectue une division entière entre deux nombres.
    
    Args:
        a (float): Numérateur
        b (float): Dénominateur
    
    Returns:
        float: Le quotient entier de a divisé par b (a // b)
    """
    return a // b
