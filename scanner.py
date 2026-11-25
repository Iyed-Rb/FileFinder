from pathlib import Path

dossier = Path("exemples")

for element in dossier.rglob("*"):
    if element.is_file():
        print(element)


