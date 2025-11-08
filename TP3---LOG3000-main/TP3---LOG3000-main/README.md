## Équipe
- Amina Djemah (2178325)
- Rayane Ighil (2076794)

# Calculatrice Web Flask

Une application web de calculatrice simple et intuitive développée avec Flask.

## Description du Projet

Cette application web permet d'effectuer les opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface utilisateur claire et responsive. Le projet est développé dans le cadre du cours LOG3000 et met l'accent sur les bonnes pratiques de développement logiciel.

### Fonctionnalités
- Calculs arithmétiques de base
- Interface utilisateur intuitive
- Gestion des erreurs (division par zéro, format invalide)
- Design responsive

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- **Python 3.8+**
- **pip** (le gestionnaire de paquets Python)
- **Git**
- Un navigateur web moderne

## Guide d'Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/KheirAmina/TP3_LOG3000.git
   cd TP3_LOG3000
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer l'application**
   ```bash
   python app.py
   ```

2. **Accéder à l'application**
   - Ouvrez votre navigateur
   - Accédez à `http://localhost:5000`

3. **Utiliser la calculatrice**
   - Entrez un premier nombre
   - Cliquez sur l'opérateur souhaité
   - Entrez le deuxième nombre
   - Appuyez sur '=' pour voir le résultat

## Tests

Les tests unitaires sont écrits avec pytest. Pour les exécuter :

1. **Installation des dépendances de test**
   ```bash
   pip install pytest
   ```

2. **Exécution des tests**
   ```bash
   pytest tests/
   ```

## Structure du Projet

```
TP3_LOG3000/
├── app.py              # Point d'entrée de l'application
├── operators.py        # Fonctions des opérations arithmétiques
├── static/            
│   └── style.css      # Styles CSS
├── templates/
│   └── index.html     # Template principal
└── tests/             # Tests unitaires
```

## Contribution

1. **Branches**
   - `main` : code de production
   - `develop` : développement actif
   - `feature/*` : nouvelles fonctionnalités
   - `bugfix/*` : corrections de bugs

2. **Pull Requests**
   - Créez une branche depuis `develop`
   - Développez votre fonctionnalité
   - Soumettez une PR vers `develop`
   - Attendez la revue de code

3. **Issues**
   - Utilisez les templates fournis
   - Étiquetez correctement (bug, enhancement, etc.)
   - Soyez précis dans la description
