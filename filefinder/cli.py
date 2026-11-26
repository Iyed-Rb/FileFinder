"""Lit les arguments du terminal et affiche les fichiers trouvés."""

import argparse
from pathlib import Path

from filefinder.filtres import filtrer_extension, filtrer_nom
from filefinder.parcours import scanner_dossier


def main():
    parser = argparse.ArgumentParser(
        description="Rechercher des fichiers"
    )

    parser.add_argument(
        "dossier",
        type=Path,
        help="Dossier à parcourir",
    )
    parser.add_argument(
        "--extension",
        help="Extension à rechercher, exemple : .txt",
    )
    parser.add_argument(
        "--nom",
        help="Texte à rechercher dans le nom du fichier",
    )
    parser.add_argument(
        "--exact",
        action="store_true",
        help="Rechercher le nom complet, extension comprise",
    )

    args = parser.parse_args()

    if args.exact and not args.nom:
        parser.error("--exact nécessite --nom")

    if not args.dossier.is_dir():
        parser.error(f"Dossier introuvable ou invalide : {args.dossier}")

    fichiers = scanner_dossier(args.dossier)

    if args.extension:
        fichiers = filtrer_extension(fichiers, [args.extension])

    if args.nom:
        fichiers = filtrer_nom(
            fichiers,
            args.nom,
            exact=args.exact,
        )

    for fichier in fichiers:
        print(fichier)