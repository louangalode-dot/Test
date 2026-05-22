def analyser_mdp(mdp):
   score = 0
   conseils = []

   if len(mdp) >= 8:
       score += 1
   else:
       conseils.append("Au moins 8 caractères")

   if any(c.isupper() for c in mdp):
       score += 1
   else:
       conseils.append("Ajouter une majuscule")

   if any(c.islower() for c in mdp):
       score += 1
   else:
       conseils.append("Ajouter une minuscule")

   if any(c.isdigit() for c in mdp):
       score += 1
   else:
       conseils.append("Ajouter un chiffre")

   if any(c in "!@#$%^&*" for c in mdp):
       score += 1
   else:
       conseils.append("Ajouter un caractère spécial (!@#$%)")

   if score <= 2:
       niveau = "FAIBLE 🔴"
   elif score <= 3:
       niveau = "MOYEN 🟡"
   else:
       niveau = "FORT 🟢"

   print("Niveau : " + niveau)
   if conseils:
       print("Conseils :")
       for conseil in conseils:
           print("  → " + conseil)

print("=== Vérificateur de mot de passe ===")
mdp = input("Entre ton mot de passe : ")
analyser_mdp(mdp)
