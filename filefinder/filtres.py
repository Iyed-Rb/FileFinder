from datetime import date



def filtrer_extension(fichiers, extensions):
    """Filtre les fichiers selon une ou plusieurs extensions."""
    extensions = {
        "." + extension.lower().lstrip(".")
        for extension in extensions
    }

    return [
        fichier
        for fichier in fichiers
        if fichier.suffix.lower() in extensions
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



def filtrer_taille(fichiers, taille_min=None, taille_max=None):
    """Filtre les fichiers par taille en octets, bornes incluses."""
    if taille_min is not None and taille_min < 0:
        raise ValueError("La taille minimale doit être positive ou nulle.")

    if taille_max is not None and taille_max < 0:
        raise ValueError("La taille maximale doit être positive ou nulle.")

    if (
        taille_min is not None
        and taille_max is not None
        and taille_min > taille_max
    ):
        raise ValueError("La taille minimale dépasse la taille maximale.")

    resultats = []

    for fichier in fichiers:
        taille = fichier.stat().st_size

        if taille_min is not None and taille < taille_min:
            continue

        if taille_max is not None and taille > taille_max:
            continue

        resultats.append(fichier)

    return resultats



def filtrer_date_modification(fichiers, date_min=None, date_max=None):
    """Filtre par date de modification, bornes incluses."""
    if (
        date_min is not None
        and date_max is not None
        and date_min > date_max
    ):
        raise ValueError("La date minimale dépasse la date maximale.")

    resultats = []

    for fichier in fichiers:
        date_modification = date.fromtimestamp(fichier.stat().st_mtime)

        if date_min is not None and date_modification < date_min:
            continue

        if date_max is not None and date_modification > date_max:
            continue

        resultats.append(fichier)

    return resultats