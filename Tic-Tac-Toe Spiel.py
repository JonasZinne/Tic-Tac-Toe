# Titel
print("Tic-Tac-Toe Spiel")

# Variablen
spiel_aktiv = True
spieler_aktuell = "X"

# Spielfeld definieren
spielfeld = [''] + [str(i) for i in range(1, 10)]

# Spielfeld ausgeben
def spielfeld_ausgeben():
    for i in range(1, 10, 3):
        print(f"{spielfeld[i]}|{spielfeld[i+1]}|{spielfeld[i+2]}")
    print()

# Spielereingabe 
def spieler_eingabe():
    while True:
        spielzug = input("Eingabe Feld: ")

        if spielzug.lower() == 'exit':
            print("Das Spiel wurde beendet.")
            return None

        try:
            spielzug = int(spielzug)
            if spielzug < 1 or spielzug > 9:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")
                continue

            if spielfeld[spielzug] in ['X', 'O']:
                print("Dieses Feld ist bereits belegt! Bitte ein anderes Feld eingeben.")
            else:
                return spielzug

        except ValueError:
            print("Bitte eine Zahl eingeben.")

# Spieler wechseln
def spieler_wechseln(spieler):
    return 'O' if spieler == 'X' else 'X'

# Kontrolle auf Gewinnen
def kontrolle_gewonnen():
    kombinationen = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for a, b, c in kombinationen:
        if spielfeld[a] == spielfeld[b] == spielfeld[c]:
            return spielfeld[a]
    return None

# Kontrolle auf Unentschieden
def kontrolle_unentschieden():
    return all(spielfeld[i] in ['X', 'O'] for i in range(1, 10))

# Hauptschleife
spielfeld_ausgeben()
while spiel_aktiv:
    print(f"Der Spieler {spieler_aktuell} ist am Zug.")
    
    spielzug = spieler_eingabe()
    if spielzug is None:
        break

    spielfeld[spielzug] = spieler_aktuell
    spielfeld_ausgeben()

    if kontrolle_gewonnen():
        print(f"Spieler {spieler_aktuell} hat gewonnen!")
        break

    if kontrolle_unentschieden():
        print("Das Spiel ist Unentschieden ausgegangen")
        break

    spieler_aktuell = spieler_wechseln(spieler_aktuell)