try:
    x = int(input("Entrez un nombre : "))
    print(f"Vous avez entré {x}")
except ValueError:
    print("Erreur : ce n'est pas un nombre valide !")