"""
Application web de calculatrice utilisant Flask.
Ce module fournit une interface web simple pour effectuer des opérations arithmétiques de base.
Il utilise les fonctions définies dans le module operators pour les calculs.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant les opérateurs à leurs fonctions correspondantes
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str) -> float:
    """
    Analyse et évalue une expression arithmétique simple.
    
    Args:
        expr (str): L'expression à évaluer (ex: "2 + 3", "10 - 5")
    
    Returns:
        float: Le résultat de l'opération
        
    Raises:
        ValueError: Si l'expression est invalide, vide, ou contient plusieurs opérateurs
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("Expression vide")

    s = expr.replace(" ", "")  # Supprime les espaces pour faciliter le parsing

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Les opérandes sont manquantes ou l'opérateur est à une position invalide
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)