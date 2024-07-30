import sys

def dico_films(fichier1, fichier2):
    dico = dict()
    compteur = 0
    with open(fichier1, 'r', encoding='UTF-8') as f1:
        for line in f1:
            compteur += 1
            elements = line.strip().split('#')
            # print(elements)
            #2,187.0 -- 2187.0
            revenu = float(elements[1].replace(',', ''))
            dico[elements[0]] = [compteur, revenu, int(elements[2])]
    with open(fichier2, 'r', encoding='UTF-8') as f2:
        elements = f2.read().strip().split('\n\n')
        for element in elements:
            lignes = element.splitlines()
            # print(lignes)
            title = lignes[0]
            genre = lignes[1][7:].split('/')
            studio = lignes[2][13:].split('/')
            realisateur = lignes[3][11:].split('#')
            acteurs = lignes[4][8:].split('#')
            dico[title] += [genre, studio, realisateur, acteurs]
    return dico

def print_all(dico, film_pref):
    compteur, revenue, annee, genre, studio, real, acteurs = dico[film_pref]
    print('Mon film prefere est: ', choice, '.')
    print('Il a fait {} dollars'.format(revenue))
    print('Il est paru le {} par la distribution {} et le realisateur {}'.format(annee, studio, real))
    print("C'est un film de genre {} dont les acteurs sont {}".format(genre, acteurs))

def changement_cle(dico, new_cle):
    ##dico[new_cle]= title
    dico_new = dict()
    for movie, infos in dico.items():
        elements = infos[new_cle]
        for element in elements:
            if not element in dico_new:
                dico_new[element] = set()
            dico_new[element].add(movie)
    return dico_new


if __name__ == '__main__':

    #'Avatar\n\tgenre:Sci-Fi Adventure\n\tdistributor:Fox\n\tdirectors:James Cameron\n\tactors:Sam Worthington#Zoe Saldana#Sigourney Weaver#Michelle Rodriguez#Giovanni Ribisi#Joel David Moore',
    # ['Valkyrie', '\tgenre:Thriller', '\tdistributor:United Artists', '\tdirectors:Bryan Singer', '\tactors:Tom Cruise#Kenneth Branagh#Tom Wilkinson#Bill Nighy#Carice van Houten']

    #dictionnaire  --- cle: titre des films -- valeurs: revenu, date de sortie, genre, studio, real, acteurs
    dico_film = dico_films('box-office.txt', 'movies-info.txt')
    valeur_nombre = {'compteur':0, 'revenu':1, 'annee':2, 'genre':3, 'studio':4, 'realisateur':5, 'acteurs':6}

    #Question1
    ##########
    choice = 'How to Train Your Dragon'
    d = dico_film[choice][valeur_nombre['realisateur']]
	print('Réalisateur(s) de "{}" : {}\n'.format(choice, d))
    ##########

    #### Question2
    print_all(dico_film, choice)
    #####

    #### Question3
    #cle: relisateur, valeur: liste_film
    choice = 'Tim Burton'
    dico_realisateur = changement_cle(dico_film, valeur_nombre['realisateur'])
    print('Film(s) de "{}" : {}\n'.format(choice, dico_realisateur[choice]))
    ####

    ### Question4
    choice = 'Animation'
    dico_genre = changement_cle(dico_film, value_dico['genre'])
    list_title_genre_pref = list(dico_genre[choice])
    best_film, best_revenu = find_best_movie(list_title_genre_pref, dict_movie)
    print('"Meilleur" film de la catégorie "{}": {}\n'.format(choice,best_film))
    #########
