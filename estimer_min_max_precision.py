#La même limitation s'applique sur les grands nombres. Toutefois, cela est un peu moins évident, 
#car comme toujours il faut faire attention aux types : 10**450 et 10**450.0

def rechercher_centre(le_milieu, la_liste, ma_recherche, mon_debut, ma_fin):
	if (la_liste[le_milieu] == ma_recherche):
		print('Votre recherche est en position '+ str(le_milieu) )  
		return ma_recherche

	if (la_liste[le_milieu] > ma_recherche):
		print('Votre recherche est entre '+ str(mon_debut) +' et '+ str(la_liste[le_milieu])) 
		(longueur, list_triee, centre) = set_my_search_parameters(mon_debut, la_liste[le_milieu])
		ma_recherche = rechercher_centre(centre, list_triee, ma_recherche, mon_debut, ma_fin)
		return ma_recherche

	if (la_liste[le_milieu] < ma_recherche) :
		print('Votre recherche est entre '+ str(la_liste[le_milieu]) +' et '+ str(ma_recherche) )
		(longueur, list_triee, centre) = set_my_search_parameters(la_liste[le_milieu], ma_fin)
		recherche = rechercher_centre(centre, list_triee, ma_recherche, mon_debut, ma_fin)
		return ma_recherche

def estim_min(my_min,my_max):
	my_min = int(my_min)
	my_max = int(my_max)

	
	if ((my_max - my_min) <= 1):
		raise ValueError('Impossible de trouver un milieu')

	if(my_min < my_max):
		ma_recherche = 4
		(longueur, list_triee, centre) = set_my_search_parameters(my_min, my_max)
		recherche = rechercher_centre(centre, list_triee, ma_recherche, my_min, my_max)
		return centre, list_triee, longueur, recherche

	else :
		raise ValueError('Le tableau est vide, sortir')

def set_my_search_parameters(p_min, p_max):
	param_list = list(range(p_max))
	param_len = len(list(range(p_max)))
	param_centre = (p_max - p_min) // 2
	return param_len, param_list, param_centre

