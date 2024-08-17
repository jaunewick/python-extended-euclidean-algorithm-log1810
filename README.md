# python-extended-euclidean-algorithm-log1810

Un script Python `epgcd.py` qui implémente l'algorithme d'Euclide étendu pour calculer le plus grand commun diviseur (PGCD) de deux nombres.

Le script affiche également toutes les étapes du processus, ce qui le rend particulièrement utile pour les étudiants du cours LOG1810.

## Prérequis
- Python 3.x
- `pip` ou `pipenv` pour la gestion des packages
- `numpy` pour les opérations sur les vecteurs

## Installation

1. **Créer un environnement virtuel** :
```bash
python3 -m venv .venv
```
2. **Activer l'environnement virtuel** :
- Sur macOS/Linux :
```bash
source ./venv/bin/activate
```
- Sur Windows :
```bash
.\venv\Scripts\activate
```
- Ou utilisez pipenv :
```bash
pipenv
```

3. **Installer les dépendances** :
- Avec pip:
```bash
pip install numpy
```
- Avec pipenv :
```bash
pipenv install numpy
```

## Utilisation
1. **Modifier les vecteurs A et B dans le script selon les besoins** :
```python
A, B = [1110, 1, 0], [99999, 0, 1]
```
2. **Exécuter le script** :
```bash
python3 epgcd.py
```
3. **Enjoy! :)**