"""
TP 1 — Calculatrice en Python (Première séance)

Objectifs pédagogiques:
- Entrées/sorties avec input() et print()
- Variables, types (int, float), conversions
- Fonctions et réutilisation de code
- Conditions (if/elif/else) et boucles (while)
- Gestion d'erreurs simples (division par zéro, saisie invalide)
- Formatage de chaînes (f-strings)
"""

import math

# Fonctions de clcul de base

def addition(a: float, b: float) -> float:
    return a + b

def soustraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible.")
    return a / b

def puissance(a: float, b: float) -> float:
    return a ** b

def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Modulo par zéro impossible.")
    return a % b

def racine_carree(a: float) -> float:
    if a < 0:
        raise ValueError("Impossible de calculer la racine carrée d’un nombre négatif.")
    return math.sqrt(a)

# Utilitaire: lecture robuste d'un nombre

def lire_nombre(message: str) -> float:
    """Demande un nombre à l'utilisateur jusqu'à obtenir une saisie valide."""
    while True:
        texte = input(message).strip().replace(",", ".")
        try:
            return float(texte)
        except ValueError:
            print("Saisie invalide. Entrez un nombre (ex: 3, 4.2, -7).")

#le nombre de décimales à afficher
def lire_entier(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Affichage du menu
def afficher_menu() -> None:
    print("\n=== Calculatrice - TP Python (Séance 1) ===")
    print("Choisissez une opération :")
    print("  1) Addition        (+)")
    print("  2) Soustraction    (-)")
    print("  3) Multiplication  (*)")
    print("  4) Division        (/)")
    print("  5) Puissance       (^)")
    print("  6) Modulo          (%)")
    print("  7) Racine carree   (sqrt)")
    print("  h) Historique")
    print("  q) Quitter")

def obtenir_operation() -> str:
    choix = input("Votre choix: ").strip().lower()
    if choix in ("1", "+"): 
        return "+"
    if choix in ("2", "-"):
        return "-"
    if choix in ("3", "*"):
        return "*"
    if choix in ("4", "/"): 
        return "/"
    if choix in ("5", "^"): 
        return "^"
    if choix in ("6", "%"): 
        return "%"
    if choix in ("7", "sqrt", "r", "√"): 
        return "sqrt"
    if choix in ("h", "hist", "historique"):
        return "h"
    if choix in ("q", "quit", "exit"):
        return "q"
    print("Choix invalide. Réessayez.")
    return ""

#  un dictionnaire d'opérations
operations = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division,
    "^": puissance,
    "%": modulo,
    "sqrt": racine_carree,
}

def calculer(op:str, a:float, b:float) -> float:
    if op not in operations:
        raise ValueError(f"Opération inconnue: {op}")
    fonction = operations[op]
    return fonction(a) if op == "sqrt" else fonction(a, b)


def main() -> None:
    historique = []
    nb_decimales = lire_entier("choisir le nombre de décimales à afficher:")

    while True:
        afficher_menu()
        op = obtenir_operation()
        if op == "":
            continue
        if op == "q":
            print("Au revoir.")
            break

        if op == "h":
            if not historique:
                print("Aucune opération effectuée.")
            else:
                print("Historique des opérations")
                for ligne in historique:
                    print(ligne)
            continue

        # Détection de la racine carrée
        if op == "sqrt":
            a = lire_nombre("Entrez un nombre : ")
            try:
                resultat = calculer(op, a , 0)
                print(f"Résultat : sqrt{a} = {resultat:.{nb_decimales}f}")
                historique.append(f"sqrt{a} = {resultat:.{nb_decimales}f}")
            except Exception as e:
                print(f"Erreur : {e}")
            continue

        # Lecture des deux opérandes
        a = lire_nombre("Entrez le premier nombre : ")
        b = lire_nombre("Entrez le deuxieme nombre : ")

        try:
            resultat = calculer(op, a, b)
            print(f"Résultat : {a} {op} {b} = {resultat:.{nb_decimales}f}")
            historique.append(f"{a} {op} {b} = {resultat:.{nb_decimales}f}")
        except ZeroDivisionError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Erreur : {e}")

        # Option: demander si l'utilisateur veut continuer
        continuer = input("Continuer ? (o/n): ").strip().lower()
        if continuer not in ("o", "oui", "y", "yes", ""):
            print("Au revoir.")
            break


def tests_rapides():
    assert addition(2, 3) == 5
    assert soustraction(6, 2) == 4
    assert multiplication(7, 3) == 21
    assert division(9, 3) == 3
    assert puissance(4, 2) == 16
    assert modulo(5, 3) == 2
    assert math.isclose(racine_carree(16), 4)
    print("Tous les tests unitaires sont passés avec succès !")


if __name__ == "__main__":
     tests_rapides()
main()


