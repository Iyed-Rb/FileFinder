"""Lecteur de fichiers PDF via PyMuPDF.

Parcourt le document page par page et retourne un Fragment par page non vide,
avec le numéro de page à partir de 1.

- Si Un PDF est sans texte donc on retourne [], veut dire que le PDF est vide.

"""



from pathlib import Path

import pymupdf

from filefinder.modeles import Fragment


def lire_fragments(chemin: Path) -> list[Fragment]:
    fragments = []
    with pymupdf.open(chemin) as document:
        for numero, page in enumerate(document, start=1):
            texte = page.get_text().strip() # recupe re le texte de la page, pas ligne par ligne.
            if texte:
                fragments.append(Fragment(texte=texte, page=numero))
    return fragments