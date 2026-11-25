"""Vérifie les filtres développés dans filefinder/filtres.py.

On peut déjà essayer les filtres manuellement avec scanner.py.
Ici, le but est d'automatiser ces vérifications pour ne pas
avoir à les refaire à la main après chaque modification.

Pour chaque test :
- préparer une liste de chemins ;
- appeler le filtre ;
- vérifier le résultat attendu avec assert.

Cas à vérifier : extension, nom partiel, nom exact,
majuscules et absence de résultat.
Vous pouvez ajouter d'autres cas utiles.
Ces tests n'ont pas besoin de vrais fichiers : des chemins suffisent.

Pour lancer ce fichier depuis la racine du projet :
    python -m pytest tests/test_filtres.py

Pour l'instant, ce fichier décrit les tests à écrire.
"""