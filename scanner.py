from pathlib import Path
import argparse

def scanner_dossier(dossier):
    fichiers = []

    for element in dossier.rglob("*"):
    # on ajoute cette condition pour ne récupérer que les fichiers, car  
    #rglob ne fait pas la différence entre un fichier et un dossier
        if element.is_file():
            fichiers.append(element)

    return fichiers


def filtrer_extension(fichiers, extension):
  ext = extension.lower()
  resultat = []
  for fichier in fichiers:
    if fichier.suffix.lower() == ext:
      resultat.append(fichier)
  return resultat


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


def main():
    parser = argparse.ArgumentParser(description="Rechercher des fichiers")
    parser.add_argument("dossier", type=Path, help="Dossier à parcourir")
    parser.add_argument("--extension", help="Extension à rechercher, exemple : .txt")
    parser.add_argument("--nom", help="Texte à rechercher dans le nom du fichier")
    parser.add_argument("--exact",action="store_true",help="Rechercher le nom complet, extension comprise",
    )

    args = parser.parse_args()

    if not args.dossier.is_dir():
        parser.error(f"Le dossier n'existe pas : {args.dossier}")

    if args.exact and not args.nom:
    parser.error("--exact nécessite --nom")

    fichiers = scanner_dossier(args.dossier)

    if args.extension:
        fichiers = filtrer_extension(fichiers, args.extension)

    if args.nom:
        fichiers = filtrer_nom(fichiers, args.nom, exact=args.exact)

    

    for fichier in fichiers:
        print(fichier)


if __name__ == "__main__":
    main()
