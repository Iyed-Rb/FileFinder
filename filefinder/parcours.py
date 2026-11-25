"""Récupère les fichiers d'un dossier et de ses sous-dossiers."""


def scanner_dossier(dossier):
    fichiers = []

    for element in dossier.rglob("*"):
        if element.is_file():
            fichiers.append(element)

    return fichiers