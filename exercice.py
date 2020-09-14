#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return (voltage**2) / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	return  0 == v1[0] * v2[0] + v1[1] * v2[1]

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	resultat = 0
	total =0
	for v in values:
		resultat += v*(v>=0)
		total+=1*(v>=0)
	return resultat/total

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, ones = 0 , 0 , 0 , 0
	while value != 0:
		if value >= 20:
			twenties += 1
			value -= 20
		elif value >= 10:
			tens += 1
			value -= 10
		elif value >= 5:
			fives += 1
			value -= 5
		elif value >= 1:
			ones += 1
			value -= 1
	return twenties, tens, fives, ones

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
