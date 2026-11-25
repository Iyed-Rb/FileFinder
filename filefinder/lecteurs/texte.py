"""Lecture des fichiers texte : TXT, Markdown, code source, etc.

Produire un fragment par ligne, avec son numéro.
Ne pas rechercher de mot, afficher de résultat ou modifier le fichier.
Auteur(s) : à compléter.
"""

from pathlib import Path

from filefinder.modeles import Fragment


def lire_fragments(chemin: Path) -> list[Fragment]:
    """Extraire les lignes du fichier avec leur localisation.

    Renvoyer [] pour un fichier vide.
    Signaler les échecs de lecture par une exception.
    """
    raise NotImplementedError("Lecteur texte à développer")