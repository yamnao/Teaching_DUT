import sys

#Etape0: Comprendre ce qu'il y a dans les fichiers
"""
Exemple de box-office:
Avatar#2,788.0#2009 ----- Nom du film = clé, revenu en dollars, annee
Exemple de movie:
Avatar --- nom du film
genre:Sci-Fi Adventure --- genre du film
distributor:Fox --- distribution
directors:James Cameron --- directeur
actors:Sam Worthington#Zoe Saldana#Sigourney Weaver#Michelle Rodriguez#Giovanni Ribisi#Joel David Moore
"""

#Etape 1: Creation d'un dictionnaire global contenant les deux fichiers
# plus creation d'une liste contenant tous les noms de films
def creation_dico_movies(fichier1, fichier2):
    """
    Fonction qui prend les deux fichiers box-office et mmovies-infos et qui
    renvoie un dictionnaire
    Attention de bien ouvrir le fichier en encoding='UTF-8'
    """
    dict_movie = dict()
    list_film = []
    with open(fichier1, 'r', encoding='UTF-8') as f1:
        for line in f1:
            elements = line.strip().split('#')
            list_film.append(elements[0])
            #On modifie le nombre en dollars
            revenu = float(elements[1].replace(',', ''))
            dict_movie[elements[0]] = [revenu, int(elements[2])]

    with open(fichier2, 'r', encoding='UTF-8') as f2:
        # print(f2.read().strip()) -- eneleve les sauts interlignes
        #Donc omm veut maintenant couper entre les sauts a la ligme
        elements = f2.read().strip().split('\n\n')
        for element in elements:
            # print(element)
            lignes = element.splitlines()
            # print(lignes)
            title = lignes[0]
            genre  = lignes[1][7:]
            distributor = lignes[2][13:]
            director = lignes[3][11:].split('#')
            # print(lignes)
            actor = lignes[4][8:].split('#')
            #On les ajoute a la SUITE des premieres informations
            dict_movie[title] += [genre, distributor, director, actor]
    return list_film, dict_movie


def print_all(choice, dict_movie):
    revenue, annee, genre, distr, reali, acteurs = dict_movie[choice]
    print('Mon film prefere est: ', choice, '.')
    print('Il a fait {} dollars'.format(revenue))
    print('Il est paru le {} par la distribution {} et le realisateur {}'.format(annee, distr, reali))
    print("C'est un film de genre {} dont les acteurs sont {}".format(genre, acteurs))

def changement_de_cle(numero_cle, dict_movie):
    assert(0<=numero_cle<=5)
    dico_new = dict()
    for movie, infos in dict_movie.items():
        liste = infos[numero_cle]
        if not (type(liste) is list):
            liste = [liste]
        for element in liste:
            if not element in dico_new:
                dico_new[element]=set()
            dico_new[element].add(movie)
    return dico_new

def find_best_movie(list_film, dict_movie):
    revenue_max = 0
    for film in list_film:
        revenue = dict_movie[film][0]
        if revenue > revenue_max:
            best_film  = film
            revenue_max = revenue
    return best_film, revenue_max

def total_revenu(list_title, dict_movie):
    total = 0
    for film in list_title:
        total += dict_movie[film][0]
    total = round(total, 3)
    return total

def revenu_real(dico_realisateur, dict_movie):
    choices  = list(dico_realisateur.keys())
    revenu_final = 0
    for choice in choices:
        if choice != '':
            list_title_real = list(dico_realisateur[choice])
            revenu_total = total_revenu(list_title_real, dict_movie)
            if revenu_total >= revenu_final:
                real = choice
                revenu_final = revenu_total
    return real, revenu_final

def best_acteur(dico_acteur):
    max_film = 0
    for acteur in dico_acteur.keys():
        if acteur != '':
            if len(dico_acteur[acteur]) > max_film:
                best_ac = acteur
                max_film = len(dico_acteur[acteur])
    return max_film, best_ac

def acteur_15(dico_acteur):
    list_ac = []
    for acteur in dico_acteur.keys():
        if len(dico_acteur[acteur]) == 15:
            list_ac.append(acteur)
    return list_ac

if __name__ == '__main__':

    list_film, dict_movie = creation_dico_movies('box-office.txt', 'movies-info.txt')
    # print(list_film)
    # print(dict_movie)
    #DOnc notre dico a pour value: revenue, annee, genre, distributor, director, actor
    value_dico = {'revenue':0, 'annee':1, 'genre':2, 'distributeur':3, 'realisateur':4, 'acteurs':5}

    ######Question 1
    choice = 'How to Train Your Dragon'
    d = dict_movie[choice][value_dico['realisateur']]
    print('Réalisateur(s) de "{}" : {}\n'.format(choice, d))
    ######

    ######Question2
    print_all(choice, dict_movie)
    ######


    ##########Question3
    choice = 'Tim Burton'
    dico_realisateur = changement_de_cle(value_dico['realisateur'], dict_movie)
    print('Film(s) de "{}" : {}\n'.format(choice, dico_realisateur[choice]))
    ##########


    ##########Question4
    choice = 'Animation'
    dico_genre = changement_de_cle(value_dico['genre'], dict_movie)
    list_title_genre_pref = list(dico_genre[choice])
    best_film, best_revenu = find_best_movie(list_title_genre_pref, dict_movie)
    print('"Meilleur" film de la catégorie "{}": {}\n'.format(choice,best_film))
    ##########

    ##########Question5
    choice = 'Animation'
    dico_genre = changement_de_cle(value_dico['genre'], dict_movie)
    list_title_genre_pref = list(dico_genre[choice])
    list_best_film = []
    for indice in range(10):
        best_film, best_revenu  = find_best_movie(list_title_genre_pref, dict_movie)
        list_best_film.append(best_film)
        list_title_genre_pref.remove(best_film)

    print('"Meilleur" film de la catégorie "{}": {}\n'.format(choice,list_best_film))
    ##########


    #########Question6
    choice = 1997
    dico_annee = changement_de_cle(value_dico['annee'], dict_movie)
    list_title_annee_pref = list(dico_annee[choice])
    best_film, best_revenu = find_best_movie(list_title_annee_pref, dict_movie)
    print('"Meilleur" film de l\'année {} au box-office: {}\n'.format(choice,best_film))
    print('Les {} films du box-office sortis en {} : {}\n'.format(len(list_title_annee_pref),choice,list_title_annee_pref))
    #########

    #########Question9
    choice = 'Tim Burton'
    dico_realisateur = changement_de_cle(value_dico['realisateur'], dict_movie)
    list_title_real_pref = list(dico_realisateur[choice])
    revenu_total = total_revenu(list_title_real_pref, dict_movie)
    print('Revenu total des films de "{}" : {:.2f}\n'.format(choice,revenu_total))
    ########

    ########Question10
    best_realisateur, best_revenu = revenu_real(dico_realisateur, dict_movie)
    print('Réalisateur ayant le plus de films au box-office : {} ({})\n'.format(best_realisateur, best_revenu))
    ########

    ########Question11
    dico_real = changement_de_cle(value_dico['realisateur'], dict_movie)
    list_real, list_revenu = [], []
    for nb in range(10):
        best_realisateur, best_revenu = revenu_real(dico_real, dict_movie)
        list_real.append(best_realisateur)
        list_revenu.append(best_revenu)
        del dico_real[best_realisateur]
    print('10 "plus gros" réalisateurs: {}\n'.format(list_real))
    ########



    #######Question12
    dico_acteur = changement_de_cle(value_dico['acteurs'], dict_movie)
    nb_film, best_ac = best_acteur(dico_acteur)
    print('Acteur ayant joué dans le plus de films au box-office : {} ({})\n'.format(best_ac,nb_film))
    #######

    ###### Question13
    dico_ac = changement_de_cle(value_dico['acteurs'], dict_movie)
    list_nb_film, list_ac= [], []
    for nb in range(10):
        nb_film, best_ac = best_acteur(dico_ac)
        list_nb_film.append(nb_film)
        list_ac.append(best_ac)
        del dico_ac[best_ac]
    print('10 acteurs ayant joué dans le plus de films: {}\n'.format(list_ac))
    #########

    #######Question14
    dico_acteur = changement_de_cle(value_dico['acteurs'], dict_movie)
    list_ac = acteur_15(dico_acteur)
    print('Acteurs ayant joué dans exactement 15 films au box-office : {} \n'.format(list_ac))
    ########


    ######Question15
    dico_genre = changement_de_cle(value_dico['genre'], dict_movie)
    dico_studio = changement_de_cle(value_dico['distributeur'], dict_movie)
    dico_acteur = changement_de_cle(value_dico['acteurs'], dict_movie)
    best_genre, max_genre = revenu_real(dico_genre, dict_movie)
    best_studio, max_studio = revenu_real(dico_studio, dict_movie)
    best_acteur, max_acteur = revenu_real(dico_acteur, dict_movie)

    print('Genre réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(best_genre,max_genre))
    print('Studio réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(best_studio,max_studio))
    print('Acteur réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(best_acteur,max_acteur))
    ######


    ########Question16
    choice = 'Harrison Ford'
    list_film_acteur_pref = list(dico_acteur[choice])
    list_genre = []
    for film in list_film_acteur_pref:
        genre_ = dict_movie[film][value_dico['genre']]
        if not genre_ in list_genre:
            list_genre.append(genre_)
    print('Genres des films auxquels a participé "{}" : {}\n'.format(choice,list_genre))
    #########

    #####Question17

    ######

    #######Question18
    max_len = 0
    for studio in dico_studio.keys():
        list_genre = []
        for film in list(dico_studio[studio]):
            genre_ = dict_movie[film][value_dico['genre']]
            if not genre_ in list_genre:
                list_genre.append(genre_)
        if len(list_genre) > max_len:
            max_len = len(list_genre)
            best_studio = studio
    print('Studio avec le plus de variété dans les genres produits : {} ({} genres différents)\n'.format(best_studio,max_len))
    ######
