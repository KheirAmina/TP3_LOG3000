# Templates

Ce répertoire contient les templates HTML utilisés par l'application Flask.

## Fichiers

### index.html
Template principal de l'application qui affiche l'interface de la calculatrice.

- **Rôle**: Fournit l'interface utilisateur de la calculatrice
- **Fonctionnalités**:
  - Affichage des boutons numériques et opérateurs
  - Zone d'affichage des expressions et résultats
  - Gestion des entrées utilisateur
  - Affichage des messages d'erreur

## Dépendances
- Les templates utilisent le moteur de template Jinja2 (inclus avec Flask)
- Les styles sont définis dans `/static/style.css`

## Notes pour les développeurs
- Les templates suivent la syntaxe Jinja2 pour l'intégration avec Flask
- Les modifications de l'interface doivent maintenir la compatibilité avec les fonctions de `app.py`
- Assurez-vous de tester le rendu sur différents navigateurs