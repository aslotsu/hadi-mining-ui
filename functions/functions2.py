import math

from calc_functions import *


def masse_de_residu_sec_total_dans_le_remblai_ajustement_fonction(masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1,
                  masse_de_residu_sec_dans_le_remblai_valeur, ajout_agregat_sec_additionnel_co_mixing,
                ajout_rejet_humide_additionnel, teneur_en_eau_massique_du_residu):
    masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 = masse_de_residu_sec_dans_le_remblai_valeur +\
    ajout_agregat_sec_additionnel_co_mixing + ajout_rejet_humide_additionnel / (+ 0.01 * teneur_en_eau_massique_du_residu)
    return masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1

def volume_de_residu_sec_total_dans_le_remblai_ajustement_fonction(volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1, 
ajout_rejet_humide_additionnel, 
teneur_en_eau_massique_du_residu, 
masse_de_residu_sec_dans_le_remblai_valeur, 
masse_volumique_specifique_du_residu, 
ajout_agregat_sec_additionnel_co_mixing, 
masse_volumique_specific_agregat_co_mixing):
    A = ajout_agregat_sec_additionnel_co_mixing / masse_volumique_specific_agregat_co_mixing
    
    B = ajout_rejet_humide_additionnel / (1 + 0.01 * teneur_en_eau_massique_du_residu)
    
    c = masse_de_residu_sec_dans_le_remblai_valeur
    
    d = 1 / masse_volumique_specifique_du_residu
    
    e = A + (B + c) * d
    if ajout_agregat_sec_additionnel_co_mixing == 0:
        volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 = (B + c) * d
    else:
        volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 = A + (B + c) * d
        volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 = ((((ajout_rejet_humide_additionnel) / (
                1 + (0.01 * teneur_en_eau_massique_du_residu))) + masse_de_residu_sec_dans_le_remblai_valeur) / (
                                                                              masse_volumique_specifique_du_residu)) + (
                                                                                     ajout_agregat_sec_additionnel_co_mixing / masse_volumique_specific_agregat_co_mixing)
    return volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1

def nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_fonction(nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1,
              masse_de_liant_total_dans_le_remblai_valeur_Mb, masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1):
    nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1 = masse_de_liant_total_dans_le_remblai_valeur_Mb / masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1
    return nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1





def nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_fonction(
nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1, 
pourcentage_massique_de_liant_recette_1, 
masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1):
    nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1 = 0.01 * pourcentage_massique_de_liant_recette_1 * masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1

    return nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1



def nouveau_volume_total_de_liant_dans_le_remblai_fonction(
nouveau_volume_total_de_liant_dans_le_remblai_recette_1, nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1, masse_volumique_S_liant_valeur):
    nouveau_volume_total_de_liant_dans_le_remblai_recette_1 = nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1 / masse_volumique_S_liant_valeur
    return nouveau_volume_total_de_liant_dans_le_remblai_recette_1

def nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_fonction(
nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1, 
nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1, 
masse_de_liant_total_dans_le_remblai_valeur_Mb):
    nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1 = nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1 - masse_de_liant_total_dans_le_remblai_valeur_Mb
    
    return nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1

def masse_ciment_1_a_ajouter_dans_le_remblai_ajustement_fonction(masse_ciment_1_a_ajouter_dans_le_remblai_recette_1_ajustement, fraction_ciment_1, nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1):
    masse_ciment_1_a_ajouter_dans_le_remblai_recette_1_ajustement = fraction_ciment_1 * nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1
    return masse_ciment_1_a_ajouter_dans_le_remblai_recette_1_ajustement




def masse_ciment_2_a_ajouter_dans_le_remblai_ajustement_fonction( masse_ciment_2_a_ajouter_dans_le_remblai_recette_1_ajustement, fraction_ciment_2, nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1):
    masse_ciment_2_a_ajouter_dans_le_remblai_recette_1_ajustement = fraction_ciment_2 * nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1
    return masse_ciment_2_a_ajouter_dans_le_remblai_recette_1_ajustement




def masse_ciment_3_a_ajouter_dans_le_remblai_ajustement_fonction(masse_ciment_3_a_ajouter_dans_le_remblai_recette_1_ajustement, fraction_ciment_3, nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1):
    masse_ciment_3_a_ajouter_dans_le_remblai_recette_1_ajustement = fraction_ciment_3 * nouvelle_masse_de_liant_a_ajouter_dans_le_remblai_recette_1
    return masse_ciment_3_a_ajouter_dans_le_remblai_recette_1_ajustement

def masse_eau_contenu_residu_humide_humide_ajoute_ajustement_fonction(masse_eau_contenu_residu_humide_humide_ajoute_ajustement_recette_1, ajout_rejet_humide_additionnel, teneur_en_eau_massique_du_residu):
    masse_eau_contenu_residu_humide_humide_ajoute_ajustement_recette_1 = ajout_rejet_humide_additionnel * (0.01 * teneur_en_eau_massique_du_residu/ (1 + 0.01 * teneur_en_eau_massique_du_residu))
    return masse_eau_contenu_residu_humide_humide_ajoute_ajustement_recette_1




def masse_eau_total_ajustement_fonction(masse_eau_total_ajustement_recette_1, masse_eau_total_dans_le_remblai_valeur, ajout_eau_additionnelle, masse_eau_contenu_residu_humide_humide_ajoute_ajustement_recette_1):
    masse_eau_total_ajustement_recette_1 = masse_eau_total_dans_le_remblai_valeur + ajout_eau_additionnelle + masse_eau_contenu_residu_humide_humide_ajoute_ajustement_recette_1
    return masse_eau_total_ajustement_recette_1




def volume_eau_total_ajustement_fonction(volume_eau_total_ajustement_recette_1, masse_eau_total_ajustement_recette_1, masse_volumique_eau):
    volume_eau_total_ajustement_recette_1 = masse_eau_total_ajustement_recette_1 / masse_volumique_eau
    
    return volume_eau_total_ajustement_recette_1





def nouveau_rapport_eau_ciment_ajustement_fonction(nouveau_rapport_eau_ciment_ajustement_recette_1, masse_eau_total_ajustement_recette_1, nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1):
    nouveau_rapport_eau_ciment_ajustement_recette_1 = masse_eau_total_ajustement_recette_1 / nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1
    
    return nouveau_rapport_eau_ciment_ajustement_recette_1




def nouveau_pourcentage_solide_ajustement_fonction(
nouveau_pourcentage_solide_ajustement_recette_1, 
masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1, 
nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1, 
masse_eau_total_ajustement_recette_1):

    nouveau_pourcentage_solide_ajustement_recette_1 = (
      masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 + nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1) / (
      masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 + nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1 + masse_eau_total_ajustement_recette_1)
    
    return nouveau_pourcentage_solide_ajustement_recette_1




def nouvelle_teneur_en_eau_massique_ajustement_fonction(
nouvelle_teneur_en_eau_massique_ajustement_recette_1, 
masse_eau_total_ajustement_recette_1, 
masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1, 
nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1):

    nouvelle_teneur_en_eau_massique_ajustement_recette_1 = masse_eau_total_ajustement_recette_1 / (
            masse_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 + nouvelle_masse_totale_de_liant_dans_le_remblai_ajustement_recette_1)

    return nouvelle_teneur_en_eau_massique_ajustement_recette_1






def nouveau_volume_des_solides_ajustement_fonction(
nouveau_volume_des_solides_ajustement_recette_1, 
volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1, 
nouveau_volume_total_de_liant_dans_le_remblai_recette_1):

    nouveau_volume_des_solides_ajustement_recette_1 = volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 + nouveau_volume_total_de_liant_dans_le_remblai_recette_1
    
    return nouveau_volume_des_solides_ajustement_recette_1




def nouveau_volume_total_ajustement_fonction(
nouveau_volume_total_ajustement_recette_1, 
volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1, 
nouveau_volume_total_de_liant_dans_le_remblai_recette_1, 
volume_eau_total_ajustement_recette_1):

    
    nouveau_volume_total_ajustement_recette_1 = volume_de_residu_sec_total_dans_le_remblai_ajustement_recette_1 + nouveau_volume_total_de_liant_dans_le_remblai_recette_1 + volume_eau_total_ajustement_recette_1
    
    return nouveau_volume_total_ajustement_recette_1





def nouveau_volume_des_vides_ajustement_fonction(
nouveau_volume_des_vides_ajustement_recette_1, 
nouveau_volume_total_ajustement_recette_1, 
nouveau_volume_des_solides_ajustement_recette_1):

    nouveau_volume_des_vides_ajustement_recette_1 = nouveau_volume_total_ajustement_recette_1 - nouveau_volume_des_solides_ajustement_recette_1
    return nouveau_volume_des_vides_ajustement_recette_1







def nouvel_indice_des_vides_ajustement_fonction(
nouvel_indice_des_vides_ajustement_recette_1, 
nouveau_volume_des_vides_ajustement_recette_1, 
nouveau_volume_des_solides_ajustement_recette_1):

    nouvel_indice_des_vides_ajustement_recette_1 = nouveau_volume_des_vides_ajustement_recette_1 / nouveau_volume_des_solides_ajustement_recette_1

    return nouvel_indice_des_vides_ajustement_recette_1





def compacite_ajustement_fonction(
compacite_ajustement_recette_1, 
nouveau_volume_des_solides_ajustement_recette_1, 
nouveau_volume_total_ajustement_recette_1):

    compacite_ajustement_recette_1 = nouveau_volume_des_solides_ajustement_recette_1 / nouveau_volume_total_ajustement_recette_1

    return compacite_ajustement_recette_1




def porosite_ajustement_fonction(
porosite_ajustement_recette_1, 
compacite_ajustement_recette_1):

    porosite_ajustement_recette_1 = 1 - compacite_ajustement_recette_1

    return porosite_ajustement_recette_1




def nouveau_degre_de_saturation_ajustement_fonction(
nouveau_degre_de_saturation_ajustement_recette_1, 
volume_eau_total_ajustement_recette_1, 
nouveau_volume_des_vides_ajustement_recette_1):

    nouveau_degre_de_saturation_ajustement_recette_1 = volume_eau_total_ajustement_recette_1 / nouveau_volume_des_vides_ajustement_recette_1

    return nouveau_degre_de_saturation_ajustement_recette_1



def teneur_en_eau_volumique_ajustement_fonction(teneur_en_eau_volumique_ajustement_recette_1, porosite_ajustement_recette_1, nouveau_degre_de_saturation_ajustement_recette_1):
    teneur_en_eau_volumique_ajustement_recette_1 = porosite_ajustement_recette_1 * (0.01 * degre_de_saturation)
    return teneur_en_eau_volumique_ajustement_recette_1






def nouvelle_masse_volumique_totale_remblai_fonction(nouvelle_masse_volumique_totale_valeur_recette_1, masse_volumique_seche_remblai_valeur, teneur_en_eau_massique_remblai_valeur):
    nouvelle_masse_volumique_totale_valeur_recette_1 = masse_volumique_seche_remblai_valeur * (1 + teneur_en_eau_massique_remblai_valeur)
    return nouvelle_masse_volumique_totale_valeur_recette_1



def prediction_cw_slump_fonction(
pourcentage_massique_de_liant_recette_1,
slump, 
poids_specific_remblai_valeur):

    prediction_cw_slump_valeur = (1 + 0.01 * pourcentage_massique_de_liant_recette_1) * 4.95 * 1000000


    denominateur = slump * (1 + 0.01 * pourcentage_massique_de_liant_recette_1) / poids_specific_remblai_valeur
    denominateur = denominateur + 235.5122

    denominateur = math.pow(denominateur, 2)

    prediction_cw_slump_valeur = prediction_cw_slump_valeur / denominateur


    return prediction_cw_slump_valeur

def prediction_cw_rapport_eau_ciment_fonction(refprediction_cw_rapport_eau_ciment_valeur, rapport_eau_sur_ciment_valeur,
pourcentage_massique_de_liant_recette_1, 
rapport_eau_ciment_dosage_selon_rapport_recette_1, 
pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1):

    A = math.pow(100 / pourcentage_massique_de_liant_recette_1 + 1, -1)
    A = A * 4
    A = A + 1

    denominateurAs= 1 + (rapport_eau_sur_ciment_valeur * (A))

    prediction_cw_rapport_eau_ciment_valeur = 100 / A

# MsgBox(prediction_cw_rapport_eau_ciment_valeur)

# pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1 = prediction_cw_rapport_eau_ciment_valeur

# MsgBox(pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1)

    return prediction_cw_rapport_eau_ciment_valeur



def masse_volumique_grain_solid_Paf_fonction(ref_masse_volumique_specific_agregat_co_mixing, ref,
 masse_volumique_specifique_du_residu, ref_masse_volumique_S_liant_valeur,
ref_nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1,
masse_volumique_grain_solid_PAF_valeur ,masse_volumique_Paf):

    masse_volumique_grain_solid_PAF_valeur = A_m / ref_masse_volumique_specific_agregat_co_mixing + (1 - A_m) / masse_volumique_specifique_du_residu + nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1 / 100 / masse_volumique_S_liant_valeur

    masse_volumique_grain_solid_PAF_valeur = 1 / masse_volumique_grain_solid_PAF_valeur

    masse_volumique_grain_solid_PAF_valeur = masse_volumique_grain_solid_PAF_valeur * (1 + nouveau_pourcentage_massique_de_liant_dans_le_remblai_ajustement_recette_1/ 100)

    return masse_volumique_grain_solid_PAF_valeur





def masse_volumique_bulk_total_PAF_fonction(
masse_volumique_bulk_total_PAF_valeur, 
pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1, 
masse_volumique_grain_solid_PAF_valeur, 
masse_volumique_eau):

    pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1 = pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1 / 100


    masse_volumique_bulk_total_PAF_valeur = pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1 / masse_volumique_grain_solid_PAF_valeur

    masse_volumique_bulk_total_PAF_valeur = masse_volumique_bulk_total_PAF_valeur + (1 - pourcentage_solide_cw_massique_fixe_dosage_selon_rapport_recette_1) / masse_volumique_eau

    masse_volumique_bulk_total_PAF_valeur = 1/ masse_volumique_bulk_total_PAF_valeur

    return masse_volumique_bulk_total_PAF_valeur








# public
# object
# masse_de_residu_sec_dans_le_remblai_PAF_fonction(object
# masse_de_residu_sec_dans_le_remblai_PAF_valeur_recette_2, object
# masse_total_MT_PAF_recette_2, object
# A_m, object
# pourcentage_solide_massique_fixe, object
# pourcentage_massique_de_liant_recette_2)
# :
#
# masse_de_residu_sec_dans_le_remblai_PAF_valeur_recette_2 = Operators.MultiplyObject(masse_total_MT_PAF_recette_2,
#                                                                                     Operators.SubtractObject(1, A_m))
#
# masse_de_residu_sec_dans_le_remblai_PAF_valeur_recette_2 = Operators.MultiplyObject(
#     masse_de_residu_sec_dans_le_remblai_PAF_valeur_recette_2,
#     Operators.DivideObject(Operators.DivideObject(pourcentage_solide_massique_fixe, 100), Operators.AddObject(1,
#                                                                                                               Operators.DivideObject(
#                                                                                                                   pourcentage_massique_de_liant_recette_2,
#                                                                                                                   100))))
#
# return masse_de_residu_sec_dans_le_remblai_PAF_valeur_recette_2



def masse_de_residu_humide_dans_le_remblai_PAF_fonction(
masse_de_residu_humide_dans_le_remblai_valeur_recette_2_PAF, 
masse_de_residu_sec_dans_le_remblai_PAF_valeur, 
pourcentage_solide_residu_humide_PAF):

    masse_de_residu_humide_dans_le_remblai_valeur_recette_2_PAF = masse_de_residu_sec_dans_le_remblai_PAF_valeur / (
            pourcentage_solide_residu_humide_PAF / 100)

    return masse_de_residu_humide_dans_le_remblai_valeur_recette_2_PAF




def masse_de_aggrega_sec_dans_le_remblai_fonction(
masse_de_aggrega_sec_dans_le_remblai_valeur_recette_2, 
masse_total_MT_PAF_recette_2, 
A_m, 
pourcentage_solide_massique_fixe, 
pourcentage_massique_de_liant_recette_2):

    masse_de_aggrega_sec_dans_le_remblai_valeur_recette_2 = masse_total_MT_PAF_recette_2 * A_m

    masse_de_aggrega_sec_dans_le_remblai_valeur_recette_2 = masse_de_aggrega_sec_dans_le_remblai_valeur_recette_2 * (
            pourcentage_solide_massique_fixe / 100/ (1 + pourcentage_massique_de_liant_recette_2/ 100))

    return masse_de_aggrega_sec_dans_le_remblai_valeur_recette_2




def masse_de_liant_total_dans_le_remblai_PAF_function(
masse_de_liant_total_dans_le_remblai_valeur_Mb_PAF_recette_2, 
masse_total_MT_PAF_recette_2, 
volume_du_liant_dans_le_remblai_valeur_recette_2, 
pourcentage_solide_massique_fixe, 
pourcentage_massique_de_liant_recette_2):

    masse_de_liant_total_dans_le_remblai_valeur_Mb_PAF_recette_2 = masse_total_MT_PAF_recette_2 * (pourcentage_solide_massique_fixe / 100) * (pourcentage_massique_de_liant_recette_2 / 100/ (1 + pourcentage_massique_de_liant_recette_2/ 100))

    return masse_de_liant_total_dans_le_remblai_valeur_Mb_PAF_recette_2





def masse_eau_total_dans_le_remblai_PAF_fonction(
masse_eau_total_dans_le_remblai_valeur_recette_2_PAF, 
masse_total_MT_PAF_recette_2, 
pourcentage_solide_massique_fixe):
    masse_eau_total_dans_le_remblai_valeur_recette_2_PAF = masse_total_MT_PAF_recette_2

    masse_eau_total_dans_le_remblai_valeur_recette_2_PAF = masse_eau_total_dans_le_remblai_valeur_recette_2_PAF * (1 - pourcentage_solide_massique_fixe/ 100)

    return masse_eau_total_dans_le_remblai_valeur_recette_2_PAF






def masse_eau_a_rajouter_PAF_fonction(
masse_eau_a_rajouter_valeur_recette_2_PAF, 
masse_eau_total_dans_le_remblai_valeur_recette_2_PAF, 
masse_de_residu_sec_dans_le_remblai_PAF_valeur, 
masse_de_residu_humide_dans_le_remblai_valeur_recette_2_PAF):

    masse_eau_a_rajouter_valeur_recette_2_PAF = masse_eau_total_dans_le_remblai_valeur_recette_2_PAF - (masse_de_residu_humide_dans_le_remblai_valeur_recette_2_PAF - masse_de_residu_sec_dans_le_remblai_PAF_valeur)

    return masse_eau_a_rajouter_valeur_recette_2_PAF




