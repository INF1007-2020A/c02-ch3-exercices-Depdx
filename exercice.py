#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return (voltage**2) / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	return  0 == v1[0] * v2[0] + v1[1] * v2[1]

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	for v in values:
		pass # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
			pass
		elif value >= 10:
			pass
		elif value >= 5:
			pass
		elif value >= 1:
			pass

	return (twenties, tens, fives, twos, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
