###############################################################################	
if __name__ == '__main__':
	##########
	choice = 'How to Train Your Dragon'
	##########
	d = None
	print('Réalisateur(s) de "{}" : {}\n'.format(choice, d))

	pass

	##########
	choice = 'Tim Burton'
	##########
	d = None
	print('Film(s) de "{}" : {}\n'.format(choice, d))
	
	##########
	choice = 'Animation'
	##########
	d = None
	print('"Meilleur" film de la catégorie "{}": {}\n'.format(choice,d))

	d = None
	print('10 "meilleurs" films du genre {}: {}\n'.format(choice,d))

	##########
	choice = 1993
	##########
	d = None
	print('"Meilleur" film de l\'année {} au box-office: {}\n'.format(choice,d))

	d = []
	print('Les {} films du box-office sortis en {} : {}\n'.format(len(d),choice,d))

	##########
	choice = 'Tim Burton'
	##########
	d = 0
	print('Revenu total des films de "{}" : {:.2f}\n'.format(choice,d))

	d,v = None,0
	print('Réalisateur générant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(d,v))
	
	d = None
	print('10 "plus gros" réalisateurs: {}\n'.format(d))

	d,v = None,0
	print('Réalisateur ayant le plus de films au box-office : {} ({})\n'.format(d,v))
	
	d,v = None,0
	print('Acteur ayant joué dans le plus de films au box-office : {} ({})\n'.format(d,v))
	
	d,v = None,0
	print('10 acteurs ayant joué dans le plus de films: {}\n'.format(d))

	d,v = None,0
	print('Acteurs ayant joué dans exactement 15 films au box-office : {} \n'.format(d))

	d,v = None,0
	print('Genre réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(d,v))

	d,v = None,0
	print('Studio réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(d,v))

	d,v = None,0
	print('Acteur réalisant le plus gros revenu : {} ({:.2f} millions de $)\n'.format(d,v))

	##########
	choice = 'Harrison Ford'
	##########
	d = None
	print('Genres des films auxquels a participé "{}" : {}\n'.format(choice,d))
	
	d = None
	print('Liste des films de "{}", avec leur genre : {}\n'.format(choice,d))

	d,v = None,0
	print('Studio avec le plus de variété dans les genres produits : {} ({} genres différents)\n'.format(d,v))

	d = None
	print('Acteurs qui ont joué avec "{}": {}\n'.format(choice,d))

	d = None
	print('Acteur qui a joué avec le plus d\'acteurs différents : {} ({})\n'.format(d,v))



