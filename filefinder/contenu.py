"""Gère la recherche à l'intérieur des fichiers.

Ici, on choisit le lecteur adapté au format du fichier
(texte, PDF, Excel...), puis on appelle sa fonction lire_fragments().

Ensuite, on cherche le texte demandé dans les fragments reçus.
On garde les correspondances avec leur localisation :
ligne, page ou cellule, selon le format.

La lecture du document reste dans lecteurs/.
L'affichage des résultats reste dans cli.py.

Cette partie est encore à développer.
"""