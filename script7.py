from smart_home import smart_home
from weerstation import weerstation
def toon_menu():
    opties = [
        "Weerstation",
        "Smart Home Controller",
        "Afsluiten"
    ]

    print("\nWelkom bij Smart App Store!")

    for nummer, optie in enumerate(opties, start=1):
        print(f"{nummer}. {optie}")


while True:
    toon_menu()
    keuze = input("Maak een keuze: ")

    if keuze == "1":
        weerstation()

    elif keuze == "2":
        smart_home()
    elif keuze == "3":
        print("Programma afgesloten.")
        break

    else:
        print("Ongeldige keuze, probeer opnieuw.")