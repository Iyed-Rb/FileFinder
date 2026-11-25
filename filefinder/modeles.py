"""Structures de données communes aux lecteurs et au moteur."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Fragment:
    """cette classe représente un fragment de texte extrait d'un fichier.
    quand vous travaillez sur un lecteur, vous devez produire une liste de Fragment pour chaque fichier.
    comme ca on obtient un modele commun pour tous les lecteurs, et on peut ensuite faire des recherches sur ces fragments.

    Les numéros de ligne et de page commencent à 1.
    Les informations absentes ou non applicables restent à None.
    texte est obligatoire , si ya pas texte donc un retour vide, les autres attributs sont None
    """

    texte: str
    ligne: int | None = None
    page: int | None = None
    feuille: str | None = None
    cellule: str | None = None