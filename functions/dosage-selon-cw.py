from calc_functions import *


def masse_volumique_S_liant_fonction():
    if fraction_ciment_3 > 0:
        masse_volumique_S_liant_valeur = 1 / (
                    (0.01 * fraction_ciment_1) / masse_volumique_specifique_du_ciment_1 + 0.01 *
                    fraction_ciment_2 / masse_volumique_specifique_du_ciment_2 + 0.01 * fraction_ciment_3 / masse_volumique_specifique_du_ciment_3)
    else:
        masse_volumique_S_liant_valeur = 1 / (
                    (0.01 * fraction_ciment_1) / masse_volumique_specifique_du_ciment_1 + 0.01 *
                    fraction_ciment_2 / masse_volumique_specifique_du_ciment_2)


def poids_specific_liant_fonction():
    poids_specific_liant_valeur = masse_volumique_S_liant_valeur / masse_volumique_eau
