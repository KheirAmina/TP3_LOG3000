"""
Tests unitaires pour l'application web Flask.
"""

import pytest
from app import app, calculate

@pytest.fixture
def client():
    """
    Fixture pour créer un client de test Flask.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """
    Teste l'accès à la page d'accueil avec GET.
    """
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'form' in rv.data

def test_calculate_valid_expressions():
    """
    Teste le parsing et le calcul d'expressions valides.
    """
    assert calculate("2 + 3") == 5
    assert calculate("5 - 2") == -3  # car b - a
    assert calculate("2 * 3") == 6  # multiplication normale
    assert calculate("6 / 2") == 3.0  # division décimale

def test_calculate_invalid_expressions():
    """
    Teste la gestion des expressions invalides.
    """
    with pytest.raises(ValueError, match="Expression vide"):
        calculate("")
    
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+23")
    
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("2+3+4")
    
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a+b")