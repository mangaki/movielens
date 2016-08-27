import csv

nb_gens = 668
nb_films = 9800
notes = [[0] * nb_films for _ in range(nb_gens)]
prenoms = list(range(nb_gens))
films = [''] * nb_films
NB_VOISINS = 50
NB_PREDICTIONS = 20

with open('ratings-ml.csv', newline='') as csvfile:
    f = csv.reader(csvfile)
    nb_gens = 0
    nb_films = 0
    nb_notes = 0
    for ligne in f:
        i, i_film, note = ligne
        i = int(i)
        i_film = int(i_film)
        note = int(note)
        notes[i][i_film] = note
        nb_gens = max(i + 1, nb_gens)
        nb_films = max(i_film + 1, nb_films)
        nb_notes += 1
    print(nb_notes, 'notes chargées de', nb_gens, 'personnes sur', nb_films, 'films')

with open('works-ml.csv', newline='') as csvfile:
    f = csv.reader(csvfile)
    for ligne in f:
        i_film, titre = ligne
        films[int(i_film)] = titre
