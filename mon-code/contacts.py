# Gestionnaire de contacts

contacts = [
    {"nom": "Alice", "tel": "0470123456", "email": "alice@gmail.com"},
    {"nom": "Bob", "tel": "0481234567", "email": "bob@gmail.com"},
    {"nom": "Louan", "tel": "0492345678", "email": "louan@easi.net"}
]

def afficher_contacts():
    print("=== MES CONTACTS ===")
    for contact in contacts:
        print(contact["nom"] + " | " + contact["tel"] + " | " + contact["email"])

def chercher_contact(nom):
    for contact in contacts:
        if contact["nom"] == nom:
            print("Trouvé : " + contact["nom"] + " - " + contact["tel"])
            return
    print("Contact introuvable.")

afficher_contacts()
print("")
chercher_contact("Louan")
chercher_contact("Marc")
