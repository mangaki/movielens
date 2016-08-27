notes = [
    [1, -1, 0, 1, 0, -1],
    [-1, 0, 1, -1, 1, 1],
    [1, 1, 1, 1, -1, -1],
    [1, 1, 0, 0, 1, -1],
    [1, -1, 1, 1, -1, 0]]
nb_gens = 5
nb_films = 6
prenoms = ['Alice', 'Bob', 'Charles', 'Daisy', 'Everett']
films = ['007', 'Batman 1', 'Shrek 2', 'Toy Story 3', 'Star Wars 4', 'Twilight 5']
NB_VOISINS = 3
NB_PREDICTIONS = 2

from big import notes, nb_gens, nb_films, prenoms, films, NB_VOISINS, NB_PREDICTIONS

def calculer_score(i, j):
    score = 0
    for k in range(nb_films):
        score += notes[i][k] * notes[j][k]
    return score

# print(calculer_score(0, 1))  # score(Alice, Bob) = -3
# print(calculer_score(0, 2))  # score(Alice, Charles) = 2

def calculer_tous_scores():
    sim = [[0] * nb_gens for _ in range(nb_gens)]
    for i in range(nb_gens):
        for j in range(nb_gens):
            sim[i][j] = calculer_score(i, j)
    return sim

"""for ligne in calculer_tous_scores():  # À éviter lorsque le dataset est gros
    print(ligne)"""

def plus_proches_voisins(i):
    candidats = []
    for j in range(nb_gens):
        if j != i:
            candidats.append((calculer_score(i, j), prenoms[j], j))
    candidats.sort()
    
    print('Les', NB_VOISINS, 'profils les plus proches de', prenoms[i], 'sont :')
    voisins = []
    for poids, nom, j in candidats[-NB_VOISINS:]:
        print(nom, 'avec poids', poids)
        voisins.append(j)
    return voisins

def calculer_prediction(i, i_film, voisins):
    nb_voisins = 0
    note = 0
    for j in voisins:
        note += notes[j][i_film]
        nb_voisins += 1
    note /= nb_voisins
    return note

def calculer_toutes_predictions(i, voisins):
    candidats = []
    for i_film in range(nb_films):
        if notes[i][i_film] == 0:  # Si i_film n'a pas été vu
            note = calculer_prediction(i, i_film, voisins)
            candidats.append((note, films[i_film]))
    candidats.sort()
    return candidats[-NB_PREDICTIONS:]

"""print('Prédictions pour Alice')
voisins = plus_proches_voisins(0)
for ligne in calculer_toutes_predictions(0, voisins):
    print(ligne)"""

def nouvel_inscrit():
    likes = [0] * nb_films
    dislikes = [0] * nb_films
    candidats = []

    for i_film in range(nb_films):
        for i in range(nb_gens):
            if notes[i][i_film] == 1:
                likes[i_film] += 1
            elif notes[i][i_film] == -1:
                dislikes[i_film] += 1
        candidats.append((likes[i_film] + dislikes[i_film], films[i_film], i_film))
    candidats.sort()

    mon_id = nb_gens
    prenom = input('Prénom ? ')
    prenoms.append(prenom)

    notes.append([0] * nb_films)  # Nouvelle ligne au tableau de notes
    for _, titre, i_film in candidats[-10:]:
        note = int(input('As tu aimé %s ? (%d notes) ' % (titre, _)))
        notes[mon_id][i_film] = note
    return mon_id

mon_id = nouvel_inscrit()
voisins = plus_proches_voisins(mon_id)
for ligne in calculer_toutes_predictions(mon_id, voisins):
    print(ligne)
