def calculer_imc(poids, taille):
    imc = poids / (taille * taille)
    return imc

mon_imc = calculer_imc(88, 1.85)
print("Mon IMC est : " + str(round(mon_imc, 1)))
