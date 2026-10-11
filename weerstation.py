import json
from urllib.request import urlopen
from urllib.parse import urlencode


def haal_json_op(url):
    with urlopen(url, timeout=10) as antwoord:
        return json.load(antwoord)


def bekijk_weer(stad):
    try:
        zoek_url = (
            "https://geocoding-api.open-meteo.com/v1/search?"
            + urlencode({"name": stad, "count": 1})
        )

        locatie = haal_json_op(zoek_url)

        if not locatie.get("results"):
            print("Stad niet gevonden.")
            return

        plaats = locatie["results"][0]

        weer_url = (
            "https://api.open-meteo.com/v1/forecast?"
            + urlencode({
                "latitude": plaats["latitude"],
                "longitude": plaats["longitude"],
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
            })
        )

        gegevens = haal_json_op(weer_url)
        weer = gegevens["current"]

        print(f"\n--- WEER IN {plaats['name'].upper()} ---")
        print(f"Temperatuur: {weer['temperature_2m']} °C")
        print(f"Luchtvochtigheid: {weer['relative_humidity_2m']}%")
        print(f"Windsnelheid: {weer['wind_speed_10m']} km/u")

    except (OSError, ValueError, KeyError, TypeError):
        print("Er ging iets mis. Probeer opnieuw.")


def weerstation():
    while True:
        print("\n--- WEERSTATION ---")
        print("1. Weer in Utrecht")
        print("2. Andere stad")
        print("3. Terug naar hoofdmenu")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            bekijk_weer("Utrecht")

        elif keuze == "2":
            stad = input("Welke stad? ").strip()

            if stad:
                bekijk_weer(stad)
            else:
                print("Vul een stad in.")

        elif keuze == "3":
            break

        else:
            print("Ongeldige keuze.")