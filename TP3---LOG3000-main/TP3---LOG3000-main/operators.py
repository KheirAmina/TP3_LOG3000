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
    Multiplie deux nombres.
    
    Args:
        a (float): Premier facteur
        b (float): Deuxième facteur
    
    Returns:
        float: Le produit de a et b
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Effectue une division entre deux nombres.
    
    Args:
        a (float): Numérateur
        b (float): Dénominateur
    
    Returns:
        float: Le quotient de a divisé par b
        
    Raises:
        ZeroDivisionError: Si le dénominateur est zéro
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b
