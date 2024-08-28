import random

# Titel
print("Tic-Tac-Toe Spiel\n")

# Variablen
spiel_aktiv = True
spieler1_name = input("Geben Sie den Namen von Spieler 1 ein: ")
spieler2_name = input("Geben Sie den Namen von Spieler 2 ein: ")
spieler_aktuell = random.choice([spieler1_name, spieler2_name])
spieler1_wins = 0
spieler2_wins = 0

# Spielfeld definieren
spielfeld = [''] + [str(i) for i in range(1, 10)]

# Spielfeld ausgeben
def spielfeld_ausgeben():
    line_format = " {:^3} | {:^3} | {:^3} "
    separator = "-----|-----|-----"

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
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")
                continue

            if spielfeld[spielzug] in ('X', 'O'):
                print("Dieses Feld ist bereits belegt! Bitte ein anderes Feld eingeben.")
            else:
                return spielzug

        except ValueError:
            print("Bitte eine Zahl eingeben.")

def spieler_wechseln(spieler):
    return spieler2_name if spieler == spieler1_name else spieler1_name

# Kontrolle auf Gewinnen
def kontrolle_gewonnen():
    kombinationen = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for a, b, c in kombinationen:
        if spielfeld[a] == spielfeld[b] == spielfeld[c]:
            return spielfeld[a]
    return None

# Kontrolle auf Unentschieden
def kontrolle_unentschieden():
    return all(spielfeld[i] in ('X', 'O') for i in range(1, 10))

# Spiel wiederholen
def erneut_spielen():
    antwort = input("Möchten Sie erneut spielen? (Ja oder Nein) ").lower()

    if antwort == 'ja':
        return True
    elif antwort == 'nein':
        print("Danke fürs Spielen!")

        print(f"Endstand - {spieler1_name}: {spieler1_wins}, {spieler2_name}: {spieler2_wins}")
        return False
    else:
        print("Ungültige Eingabe. Bitte 'Ja' oder 'Nein' eingeben.")
        return erneut_spielen()
    
# Spiel zurücksetzen
def spiel_zuruecksetzen():
    global spielfeld, spieler_aktuell
    spielfeld = [''] + [str(i) for i in range(1, 10)]
    spieler_aktuell = random.choice([spieler1_name, spieler2_name])
    spielfeld_ausgeben()

# Hauptschleife
spielfeld_ausgeben()
while spiel_aktiv:
    print(f"Der Spieler {spieler_aktuell} ist am Zug.")
    
    spielzug = spieler_eingabe()
    if spielzug is None:
        break

    spielfeld[spielzug] = 'X' if spieler_aktuell == spieler1_name else 'O'
    spielfeld_ausgeben()

    if kontrolle_gewonnen():
        print(f"Spieler {spieler_aktuell} hat gewonnen!")
        if spieler_aktuell == spieler1_name:
            spieler1_wins += 1
        else:
            spieler2_wins += 1
        print(f"Aktueller Stand - {spieler1_name}: {spieler1_wins}, {spieler2_name}: {spieler2_wins}")
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
