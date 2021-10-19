# Puissance4

LU3IN005_Statistique

Members:

- **Kai YANG**  
  Student number : _21107392_
- **Youheng GUO**  
  Student number : _28711440_

Ce répertoire contient deux sous-dossiers:

- combinatorics  
  Pour tous concernant le jeu **_Puissance 4_**
- bandits-manchots  
  Pour tous concernant la machine à sous (Partie 3)

## combinatorics

Dans ce dossier, on a une classe `Game` qui contient la plateau et les méthodes pour manipuler et contrôler la plateau et le jeu.

Et puis, il y a une classe père `Player` pour être hérité par puisieurs type de joueurs.
Par la conséquence, on a quatre types de joueur, avec trois classes fils :

- `HumanPlayer`  
   Elle lit une entrée d'utilisateur dans console, et lancer le jeu
- `RandomPlayer`  
   Elle joue au hazard
- `MonteCarloPlayer`  
   Elle joue selon l'algo Monte Carlo (Partie 2)
- `UCTPlayer`  
   Elle joue selon l'algo UCB (Partie 4)

Et à la fin, il y a un fichier `main` pour lancer tous les simulations de jeu

## bandits-manchots

Dans ce dossier, on a tout d'abord un fichier `action` pour exécuter une fois la machine à sous (Exo 1 dans la partie 3). Afin de simuler les machines, on a réaliser un script sous langage `R`, et créer du fichier `csv`, pour avoir une série de donnée de probabilité. La fonction `action` est donc capable de lire le fichier `csv` et simuler les machines à sous.

En suite, on a réaliser les quatre algorithmes dans l'énoncé. Ils prennent les paramètres comme indiqué dans l'énoncé, et retournent le résultat d'une action.

Enfin, le fichier `main` applique les 4 algorithmes, et calcule les fonction du regret pour chaque algorithmem, etc.
