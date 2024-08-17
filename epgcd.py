import numpy as np

def epgcd(A, B, prev_op=None):
    if A[0] == B[0]:
        output_format(A, B)
        return A
    elif A[0] > B[0]:
        if prev_op != "A-B":
            output_format(A, B)
        return epgcd(A-B, B, "A-B")
    else:
        if prev_op != "B-A":
            output_format(A, B)
        return epgcd(A, B-A, "B-A")

def output_format(A, B):
    return print(f"[{A[0]}, {A[1]}, {A[2]}] [{B[0]}, {B[1]}, {B[2]}]")

if __name__ == '__main__':
    # Entrez les paramètres de PGCD(a,b) ici, sous forme [a, 1, 0], [b, 0, 1]
    A, B = [1110, 1, 0], [99999, 0, 1]

    # Affichage
    print("\nSolution:\n")
    print("On utilise les vecteurs de l'algorithme d'Euclide étendu, soit :\n")
    vctrA, vctrB = np.array(A), np.array(B)
    result = epgcd(vctrA, vctrB)
    print(f"\nD'où le PGCD de {A[0]} et {B[0]} est {result[0]}.\n")