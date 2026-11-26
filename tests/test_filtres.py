"""Tests des filtres (filefinder/filtres.py).

On vérifie les filtres d'extension, de nom (partiel et exact) et de taille.
On teste aussi les majuscules et le cas où il n'y a aucun résultat.

Pour lancer : python -m pytest tests/test_filtres.py
"""


from pathlib import Path

import pytest

from filefinder.filtres import filtrer_extension, filtrer_nom, filtrer_taille


def test_filtrer_extension():
    fichiers = [
        Path("cours.pdf"),
        Path("notes.txt"),
        Path("rapport.PDF"),
        Path("tableau.xlsx"),
    ]

    resultat = filtrer_extension(fichiers, [".pdf", ".xlsx"])

    attendu = [
        Path("cours.pdf"),
        Path("rapport.PDF"),
        Path("tableau.xlsx"),
    ]

    assert resultat == attendu



def test_filtrer_extension_sans_point():
    fichiers = [Path("cours.pdf"), Path("notes.txt")]

    resultat = filtrer_extension(fichiers, ["pdf"])

    assert resultat == [Path("cours.pdf")]


def test_filtrer_extension_aucun_resultat():
    fichiers = [Path("cours.pdf"), Path("notes.txt")]

    resultat = filtrer_extension(fichiers, [".xlsx"])

    assert resultat == []


def test_filtrer_extension_liste_vide():
    fichiers = [Path("cours.pdf"), Path("notes.txt")]

    resultat = filtrer_extension(fichiers, [])

    assert resultat == []



def test_filtrer_nom_contient():
    fichiers = [Path("cours_python.txt"), Path("notes.txt")]

    resultat = filtrer_nom(fichiers, "python")

    assert resultat == [Path("cours_python.txt")]


def test_filtrer_nom_ignore_la_casse():
    fichiers = [Path("Rapport.PDF"), Path("notes.txt")]

    resultat = filtrer_nom(fichiers, "rapport")

    assert resultat == [Path("Rapport.PDF")]


def test_filtrer_nom_exact():
    fichiers = [Path("notes.txt"), Path("notes.txt.bak"), Path("mes_notes.txt")]

    resultat = filtrer_nom(fichiers, "notes.txt", exact=True)

    assert resultat == [Path("notes.txt")]


# Cette fonction ne commence pas par test_, donc pytest ne l'exécute pas comme un test
def creer_fichier(dossier, nom, taille):
    chemin = dossier / nom
    chemin.write_text("a" * taille)
    return chemin


def test_filtrer_taille_bornes_incluses(tmp_path):
    petit = creer_fichier(tmp_path, "petit.txt", 10)
    moyen = creer_fichier(tmp_path, "moyen.txt", 50)
    grand = creer_fichier(tmp_path, "grand.txt", 100)
    fichiers = [petit, moyen, grand]

    assert filtrer_taille(fichiers, taille_min=50) == [moyen, grand]
    assert filtrer_taille(fichiers, taille_max=50) == [petit, moyen]
    assert filtrer_taille(fichiers, taille_min=10, taille_max=50) == [petit, moyen]


def test_filtrer_taille_exacte(tmp_path):
    petit = creer_fichier(tmp_path, "petit.txt", 10)
    grand = creer_fichier(tmp_path, "grand.txt", 100)

    resultat = filtrer_taille([petit, grand], taille_min=10, taille_max=10)

    assert resultat == [petit]


def test_filtrer_taille_bornes_invalides(tmp_path):
    fichier = creer_fichier(tmp_path, "a.txt", 10)

    with pytest.raises(ValueError):
        filtrer_taille([fichier], taille_min=-1)

    with pytest.raises(ValueError):
        filtrer_taille([fichier], taille_max=-1)

    with pytest.raises(ValueError):
        filtrer_taille([fichier], taille_min=100, taille_max=10)