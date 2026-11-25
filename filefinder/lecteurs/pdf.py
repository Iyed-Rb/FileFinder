"""Lecteur PDF.

Complétez lire_fragments() pour récupérer le texte page par page.
Chaque fragment doit garder son numéro de page.
Vous pouvez ajouter d'autres fonctions pour organiser votre code.
"""

from pathlib import Path

from filefinder.modeles import Fragment


def lire_fragments(chemin: Path) -> list[Fragment]:
    """Extraire le texte des pages avec leur localisation.

    Renvoyer [] si aucun texte n'est extractible.
    Signaler les échecs de lecture par une exception.
    """
    raise NotImplementedError("Lecteur PDF à développer")