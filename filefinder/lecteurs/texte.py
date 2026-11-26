"""ici le code du Lecteur de fichiers texte (.txt).

-Lit le fichier ligne par ligne  et retourne un Fragment par ligne,
avec son numéro de ligne à partir de 1.

-Si le fichier est vide, la liste retournée est [].
"""


from pathlib import Path

from filefinder.modeles import Fragment


def lire_fragments(chemin: Path) -> list[Fragment]:
    fragments = []
    with open(chemin, encoding="utf-8") as fichier:
        for numero, ligne in enumerate(fichier, start=1): # A chaque tour de boucle, Python lit une seule ligne à la fois.
            fragments.append(Fragment(texte=ligne.rstrip("\n"), ligne=numero))
    return fragments