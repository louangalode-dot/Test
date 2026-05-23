from flask import Flask, request, jsonify
import re

app = Flask(__name__)

MOTS_DE_PASSE_COURANTS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "admin", "welcome",
    "monkey", "dragon", "master", "sunshine", "princess",
    "azerty", "motdepasse", "soleil", "bonjour", "football",
    "loulou", "thomas", "nicolas", "jordan", "batman"
]

SEQUENCES = ["abcdef", "qwerty", "azerty", "123456", "654321", "abcabc"]

def analyser_mdp(mdp):
    if mdp.lower() in MOTS_DE_PASSE_COURANTS:
        return {"niveau": "DANGEREUX", "conseils": [
            "Ce mot de passe figure dans les listes de hackers.",
            "Choisis quelque chose d unique et personnel."
        ]}

    score = 0
    conseils = []

    # Longueur
    if len(mdp) >= 12:
        score += 2
    elif len(mdp) >= 10:
        score += 1
    else:
        conseils.append("Au moins 12 caractères recommandés (tu en as " + str(len(mdp)) + ")")

    # Majuscule
    if any(c.isupper() for c in mdp):
        score += 1
    else:
        conseils.append("Ajouter une majuscule")

    # Minuscule
    if any(c.islower() for c in mdp):
        score += 1
    else:
        conseils.append("Ajouter une minuscule")

    # Chiffre
    if any(c.isdigit() for c in mdp):
        score += 1
    else:
        conseils.append("Ajouter un chiffre")

    # Caractère spécial
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mdp):
        score += 2
    else:
        conseils.append("Ajouter un caractère spécial (!@#$%...)")

    # Répétitions (aaa, 111)
    if re.search(r"(..)\1{2,}", mdp) or re.search(r"(.)\1{2,}", mdp):
        score -= 1
        conseils.append("Éviter les répétitions (aaa, 111...)")

    # Séquences connues
    for seq in SEQUENCES:
        if seq in mdp.lower():
            score -= 1
            conseils.append("Éviter les séquences connues (azerty, 123456...)")
            break

    # Mot + chiffres basiques (loulou02, thomas123)
    if re.match(r"^[a-zA-Z]+\d{1,4}$", mdp):
        score -= 1
        conseils.append("Mot + chiffres = trop prévisible (ex: loulou02)")

    # Que des chiffres
    if mdp.isdigit():
        score = 0
        conseils = ["Un mot de passe ne peut pas être que des chiffres"]

    # Niveau final
    if score <= 2:
        niveau = "FAIBLE"
    elif score <= 4:
        niveau = "MOYEN"
    elif score <= 6:
        niveau = "FORT"
    else:
        niveau = "EXCELLENT"

    return {"niveau": niveau, "conseils": conseils}

@app.route("/")
def home():
    return open("app/index.html").read()

@app.route("/analyser", methods=["POST"])
def analyser():
    mdp = request.json["mdp"]
    return jsonify(analyser_mdp(mdp))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
