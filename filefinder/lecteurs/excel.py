"""Lecture des classeurs XLSX.

Produire un fragment par cellule non vide, sur toutes les feuilles.
Renseigner le nom de feuille et l'adresse de cellule.
Les valeurs sont converties en texte.
La gestion des formules devra être précisée dans la documentation.
Ne pas rechercher de mot, afficher de résultat ou modifier le fichier.
Auteur(s) : à compléter.
"""

from pathlib import Path

from filefinder.modeles import Fragment


def lire_fragments(chemin: Path) -> list[Fragment]:
    """Extraire le contenu des cellules avec leur localisation.

    Renvoyer [] si aucune cellule exploitable n'est présente.
    Signaler les échecs de lecture par une exception.
    """
    raise NotImplementedError("Lecteur Excel à développer")