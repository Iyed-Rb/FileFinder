"""Structures de données communes aux lecteurs et au moteur."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Fragment:
    """Un morceau de texte lu dans un fichier, avec sa position.

    Tous les lecteurs renvoient une liste de Fragment.
    Les numéros de ligne et de page commencent à 1.
    Ce qui ne s'applique pas au format reste à None.
    """

    texte: str
    ligne: int | None = None
    page: int | None = None
    feuille: str | None = None
    cellule: str | None = None