from flask import Flask, request, jsonify

app = Flask(__name__)

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
        conseils.append("Ajouter un caractère spécial")

    if score <= 2:
        niveau = "FAIBLE"
    elif score <= 3:
        niveau = "MOYEN"
    else:
        niveau = "FORT"

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
