"""
Tests unitaires pour les opérations arithmétiques de base.
"""

import pytest
from operators import add, subtract, multiply, divide

def test_add():
    """
    Teste la fonction d'addition avec différents types de nombres.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == 0.3
    assert add(-2.5, 1.5) == -1.0

def test_subtract():
    """
    Teste la fonction de soustraction et vérifie l'ordre des opérandes.
    La fonction doit calculer b - a.
    """
    assert subtract(2, 3) == 1  # 3 - 2
    assert subtract(5, 3) == -2  # 3 - 5
    assert subtract(1, 1) == 0
    assert subtract(-1, 2) == 3  # 2 - (-1)

def test_multiply():
    """
    Teste la fonction de multiplication.
    Vérifie que l'opération effectue bien une multiplication et non une puissance.
    """
    assert multiply(2, 3) == 6  # 2 * 3 = 6 (pas 2³ = 8)
    assert multiply(3, 2) == 6  # 3 * 2 = 6 (pas 3² = 9)
    assert multiply(5, 0) == 0  # 5 * 0 = 0 (pas 5⁰ = 1)
    assert multiply(1, 5) == 5  # 1 * 5 = 5 (pas 1⁵ = 1)
    assert multiply(2, -1) == -2  # 2 * (-1) = -2 (pas 2⁻¹ = 0.5)

def test_divide():
    """
    Teste la division.
    Vérifie que l'opération effectue bien une division décimale et non une division entière.
    """
    assert divide(6, 2) == 3.0  # 6 / 2 = 3.0
    assert divide(7, 2) == 3.5  # 7 / 2 = 3.5 (pas 7 // 2 = 3)
    assert divide(1, 2) == 0.5  # 1 / 2 = 0.5 (pas 1 // 2 = 0)
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)