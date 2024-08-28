import random

# Titel
print("Tic-Tac-Toe Spiel")

# Variablen
spiel_aktiv = True
spieler_aktuell = random.choice(['X', 'O'])
x_wins = 0
o_wins = 0

# Spielfeld definieren
spielfeld = [''] + [str(i) for i in range(1, 10)]

# Spielfeld ausgeben
def spielfeld_ausgeben():
    line_format = " {:^3} | {:^3} | {:^3} "
    separator = "-----|-----|-----"

    print()
    for i in range(1, 10, 3):
        print(line_format.format(spielfeld[i], spielfeld[i+1], spielfeld[i+2]))
        if i < 7:
            print(separator)
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
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.\n")
                continue

            if spielfeld[spielzug] in ['X', 'O']:
                print("Dieses Feld ist bereits belegt! Bitte ein anderes Feld eingeben.\n")
            else:
                return spielzug

        except ValueError:
            print("Bitte eine Zahl eingeben.\n")

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

# Spiel wiederholen
def erneut_spielen():
    antwort = input("\nMöchten Sie erneut spielen? (Ja oder Nein) ").lower()

    if antwort == 'ja':
        return True
    elif antwort == 'nein':
        print("Danke fürs Spielen!\n")

        print(f"Endstand - Spieler X: {x_wins}, Spieler O: {o_wins}")
        return False
    else:
        print("Ungültige Eingabe. Bitte 'Ja' oder 'Nein' eingeben.")
        return erneut_spielen()
    
# Spiel zurücksetzen
def spiel_zuruecksetzen():
    global spielfeld, spieler_aktuell
    spielfeld = [''] + [str(i) for i in range(1, 10)]
    spieler_aktuell = random.choice(['X', 'O'])
    spielfeld_ausgeben()

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
        if spieler_aktuell == 'X':
            x_wins += 1
        else:
            o_wins += 1
        print(f"Aktueller Stand - X: {x_wins}, O: {o_wins}")
        if erneut_spielen():
            spiel_zuruecksetzen()
            continue
        break

    if kontrolle_unentschieden():
        print("Das Spiel ist Unentschieden ausgegangen.")
        if erneut_spielen():
            spiel_zuruecksetzen()
            continue
        break

    spieler_aktuell = spieler_wechseln(spieler_aktuell)