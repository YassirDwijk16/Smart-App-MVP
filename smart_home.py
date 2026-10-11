import json

BESTAND = "lamp_status.json"


def laad_status():
    try:
        with open(BESTAND, "r") as bestand:
            gegevens = json.load(bestand)
            return gegevens["lamp_aan"]
    except (FileNotFoundError, ValueError, KeyError, TypeError):
        return False


def sla_status_op(lamp_aan):
    with open(BESTAND, "w") as bestand:
        json.dump({"lamp_aan": lamp_aan}, bestand)


def smart_home():
    lamp_aan = laad_status()

    while True:
        print("\n--- Smart Home Controller ---")
        print("1. Lamp aanzetten")
        print("2. Lamp uitzetten")
        print("3. Status bekijken")
        print("4. Terug naar hoofdmenu")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            lamp_aan = True
            sla_status_op(lamp_aan)
            print("De lamp staat nu aan.")

        elif keuze == "2":
            lamp_aan = False
            sla_status_op(lamp_aan)
            print("De lamp staat nu uit.")

        elif keuze == "3":
            if lamp_aan:
                print("Status: lamp staat aan.")
            else:
                print("Status: lamp staat uit.")

        elif keuze == "4":
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")