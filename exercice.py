#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, r"C:\Users\Benoit\Desktop\école\Automne2020\INF1007\GitHub\c04-ch6-exercices-Benoit323\exercice6.py")
import exercice6
import turtle



# TODO: Définissez vos fonction ici
def volume_masse(demi_axe1 = 1, demi_axe2 = 2, demi_axe3 = 5, masse_volumique = 10):
    volume= (4/3) * math.pi * demi_axe1 * demi_axe2 * demi_axe3
    masse = masse_volumique * volume
    return (masse, volume)






if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volume_masse())
    print((lambda sentence: sorted(exercice6.frequence(sentence), key=exercice6.frequence(sentence).__getitem__)[-1])("lol"))



