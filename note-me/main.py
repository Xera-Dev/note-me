import json
import datetime

def create_note():
    print("-------------------")
    contenu = input("Note: ")
    titre = input("Titre: ")
    print("-------------------")
    
    # Créer un dictionnaire représentant la note
    note = {
        "titre": titre,
        "contenu": contenu,
        "date_creation": datetime.datetime.now().isoformat()
    }
    
    # Charger les notes existantes depuis le fichier JSON s'il existe
    try:
        with open("data.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    
    # Ajouter la nouvelle note à la liste des notes
    notes.append(note)
    
    # Enregistrer la liste mise à jour dans le fichier JSON
    with open("data.json", "w") as f:
        json.dump(notes, f, indent=4)

def view_notes():
    try:
        with open("data.json", "r") as f:
            notes = json.load(f)
            if not notes:
                print("Aucune note trouvée.")
            else:
                print("---- Liste des notes ----")
                for idx, note in enumerate(notes, 1):
                    print(f"Note {idx}:")
                    print(f"Titre: {note['titre']}")
                    print(f"Contenu: {note['contenu']}")
                    print(f"Date de création: {note['date_creation']}")
                    print("-------------------------")
    except FileNotFoundError:
        print("Aucune note trouvée.")
    



def main():
    while True:
        print("\n----- Menu: -----")
        print("| 1. Faire une note")
        print("| 2. Lire une note")
        print("| 0. Quitter")
        print("-------------------")
        choice = input("Entrez votre choix: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
