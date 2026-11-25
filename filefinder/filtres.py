"""Filtre les fichiers par extension et par nom."""


def filtrer_extension(fichiers, extension):
    return [
        fichier
        for fichier in fichiers
        if fichier.suffix.lower() == extension.lower()
    ]


def filtrer_nom(fichiers, nom, exact=False):
    nom = nom.casefold()
    resultats = []

    for fichier in fichiers:
        nom_fichier = fichier.name.casefold()

        if exact:
            correspond = nom_fichier == nom
        else:
            correspond = nom in nom_fichier

        if correspond:
            resultats.append(fichier)

    return resultats