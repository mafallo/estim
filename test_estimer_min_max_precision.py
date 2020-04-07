#dichotomie
#L'algorithme est le suivant :
#Trouver la position la plus centrale du tableau (si le tableau est vide, sortir).
#Comparer la valeur de cette case à l'élément recherché.
#Si la valeur est égale à l'élément, alors retourner la position, 
#sinon reprendre la procédure dans la moitié de tableau pertinente.
#On peut toujours se ramener à une moitié de tableau sur un tableau trié en ordre croissant. 
#Si la valeur de la case est plus petite que l'élément, on continuera sur la moitié droite, 
#c'est-à-dire sur la partie du tableau qui contient des nombres plus grands que la valeur de la case. 
#Sinon, on continuera sur la moitié gauche.

#Le but de cet exercice est d'estimer la valeur du plus petit flottant qui peut être représenté comme un flottant. 
#Pour #vous aider, voici deux valeurs :
#Comme on le voit,  10−320  est correctement imprimé, alors que  10−330  est, de manière erronée, rapporté comme étant nul.

import unittest
import estimer_min_max_precision

class TestEstimation(unittest.TestCase) :
	
	def test_shouldreturn5ifMinEq0andMaxEq10(self):
		(centre, liste, longueur, recherche) = estimer_min_max_precision.estim_min(0,10)
		self.assertEqual(centre, 5)

	def test_raiseErrorIfTabDimIslowerthan3(self):
		with self.assertRaises(ValueError):
			estimer_min_max_precision.estim_min(1,2)

	def test_raiseErrorIfTabIsNull(self):
		with self.assertRaises(ValueError):
			estimer_min_max_precision.estim_min("","")

	def test_shouldReturnASortedList(self):
			(centre, list_triee, longeur, recherche) = estimer_min_max_precision.estim_min(0,6)
			self.assertEqual(list_triee, [0, 1, 2, 3, 4, 5])

	def test_shouldReturnLongeur2LalisteEq3ifMaxEq3(self):
			(centre, list_triee, longueur, recherche) = estimer_min_max_precision.estim_min(0,6)
			self.assertEqual(longueur, 6)

	def test_souldReturnAnIntegerIfMaxIsOdd(self):
			(centre, list_triee, longueur, recherche) = estimer_min_max_precision.estim_min(0,7)
			self.assertEqual(type(centre), int)

	def test_shouldRetun2IfMyFirstAttempsIsCenter(self):
			(centre, list_triee, longueur, recherche) = estimer_min_max_precision.estim_min(0,7)
			self.assertEqual(centre, list_triee[7//2])

if __name__ == '__main__':
	unittest.main()
