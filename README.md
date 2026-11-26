# FileFinder - L2 Projet Python

Équipe :
- RABIA CHERIF, Iyed, 20265918
- CHERTOUK, Laeticia, 20265871
- MECEDDED, Asma, 20265575
- MEDJBER, Lylia, 20255973

FileFinder est un petit moteur de recherche de fichiers qui s'utilise dans le terminal.
On choisit un dossier, on donne quelques critères, et le programme affiche les fichiers
qui correspondent. À terme, il devra aussi chercher dans le contenu des fichiers et dire
où se trouve le résultat.

## Version 1.0

Le projet est en cours. Pour cette première version, on a surtout mis en place la base :
l'architecture du code, la répartition en modules, et les filtres principaux.

**À noter :** tout ce qui est décrit ici correspond à la version 1.0. Au fil du projet,
certaines choses pourront changer si on en a besoin.

Ce qui est fait :
- parcours d'un dossier et de ses sous-dossiers
- filtre par extension (une ou plusieurs) et par nom (partiel ou exact, sans tenir compte des majuscules)
- filtres par taille et par date de modification : ils sont écrits, mais pas encore branchés dans la ligne de commande
- une classe `Fragment` que tous les lecteurs de fichiers renvoient
- une première version des lecteurs texte et PDF
- des tests automatiques pour les filtres d'extension, de nom et de taille

Ce qui reste à faire :
- les autres options de la ligne de commande
- la recherche dans le contenu des fichiers (`contenu.py`)
- d'autres formats de fichiers que le texte et le PDF
- plus de tests, pour couvrir plus de cas
- la gestion des erreurs (permissions, fichiers illisibles)
- l'index pour accélérer les recherches, et la comparaison avec la recherche directe

## Installation

Il faut Python 3.10 ou plus.

    pip install -e ".[dev]"

## Utilisation

    python scanner.py DOSSIER [--extension .txt] [--nom texte] [--exact]

Quelques exemples :

    python scanner.py exemples --extension .txt
    python scanner.py exemples --nom cours
    python scanner.py exemples --nom notes.txt --exact

Pour lancer les tests :

    python -m pytest

## Organisation du code

    scanner.py            point d'entrée
    filefinder/
      cli.py              arguments du terminal et affichage
      parcours.py         exploration des dossiers
      filtres.py          filtres sur les fichiers
      modeles.py          la classe Fragment
      contenu.py          recherche dans le contenu (à développer)
      lecteurs/           un lecteur par format de fichier
    tests/                tests automatiques
    exemples/             fichiers d'exemple

## Comment on lit le contenu des fichiers

Chaque lecteur fait la même chose : il lit un fichier et renvoie une liste d'objets de la
classe `Fragment`. Un `Fragment` est un petit morceau de texte avec sa position. Par exemple,
une ligne pour un fichier texte, ou une page pour un PDF. Un lecteur ne cherche rien et
n'affiche rien, il lit seulement.

On a choisi cette façon de faire pour que la recherche n'ait pas besoin de connaître les
formats, et pour pouvoir dire exactement où se trouve un résultat.

## Ce qui est choisi, ce qui peut changer

Pour l'instant, on a gardé :
- un programme qui s'utilise dans le terminal ;
- la recherche directe dans les fichiers, avant l'index ;
- des lecteurs qui renvoient tous des `Fragment`.

La classe `Fragment` et les filtres peuvent encore être modifiés si on découvre qu'il
manque quelque chose en avançant.

## À discuter et à décider

Les formats exacts à la fin, la syntaxe de certaines options, la gestion des accents, la
façon de stocker un index, et la recherche d'une phrase répartie sur plusieurs fragments.