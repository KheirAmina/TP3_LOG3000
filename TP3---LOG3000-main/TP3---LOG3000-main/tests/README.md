# Tests

Ce répertoire contient les tests unitaires pour la calculatrice web Flask.

## Structure

- `test_operators.py` : Tests des opérations arithmétiques de base
- `test_app.py` : Tests des fonctionnalités web et du parsing d'expressions

## Exécution des tests

1. Assurez-vous d'être dans l'environnement virtuel :
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/MacOS
   ```

2. Installez pytest :
   ```bash
   pip install pytest
   ```

3. Exécutez les tests :
   ```bash
   pytest tests/
   ```

## Couverture des tests

### Opérations arithmétiques (`test_operators.py`)
- Addition : test des nombres positifs, négatifs et décimaux (avec gestion de la précision)
- Soustraction : vérification de l'ordre des opérandes (b - a)
- Multiplication : test de la multiplication standard (a * b)
- Division : test de la division décimale avec gestion de la division par zéro

### Application Web (`test_app.py`)
- Parsing d'expressions : formats valides et invalides
- Gestion des erreurs : expressions malformées, valeurs non numériques
- Routes HTTP : GET et POST sur la route principale

## Rapports de bugs

Les tests permettent d'identifier les problèmes potentiels dans :
- L'ordre des opérandes pour certaines opérations
- Le traitement des expressions malformées
- La gestion des cas limites (division par zéro, etc.)