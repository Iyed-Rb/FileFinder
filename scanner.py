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



def main():
    parser = argparse.ArgumentParser(description="Rechercher des fichiers")
    parser.add_argument("dossier", type=Path, help="Dossier à parcourir")
    parser.add_argument("--extension", help="Extension à rechercher, exemple : .txt")

    args = parser.parse_args()

    if not args.dossier.is_dir():
        parser.error(f"Le dossier n'existe pas : {args.dossier}")

    fichiers = scanner_dossier(args.dossier)

    if args.extension:
        fichiers = filtrer_extension(fichiers, args.extension)

    for fichier in fichiers:
        print(fichier)


if __name__ == "__main__":
    main()
