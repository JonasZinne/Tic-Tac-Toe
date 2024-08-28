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

# Spielereingabe 
def spieler_eingabe():
    global spiel_aktiv

    while True:
        spielzug = input("Eingabe Feld: ")

        if spielzug.lower() == 'exit':
            spiel_aktiv = False
            print("Das Spiel wurde beendet.")
            return

        try:
            spielzug = int(spielzug)
            if 1 <= spielzug <= 9:
                if spielfeld[spielzug] in ['X', 'O']:
                    print("Dieses Feld ist bereits belegt! Bitte ein anderes Feld eingeben.")
                else:
                    return spielzug
            else:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")

        except ValueError:
            print("Bitte eine Zahl eingeben.")
            
# Spieler wechseln
def spieler_wechseln():
    global spieler_aktuell

    spieler_aktuell = 'O' if spieler_aktuell == 'X' else 'X'

# Kontrolle auf Gewinnen
def kontrolle_gewonnen():
    kombinationen = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for a, b, c in kombinationen:
        if spielfeld[a] == spielfeld[b] == spielfeld[c]:
            return spielfeld[a]
        return None

# Kontrolle auf Unentschieden
def kontrolle_unentschieden():
    if all(spielfeld[i] in ['X', 'O'] for i in range(1, 10)):
        return 'unentschieden'
    return None

# Hauptschleife
spielfeld_ausgeben()
while spiel_aktiv:
    print(f"Der Spieler {spieler_aktuell} ist am Zug.")
    
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()

        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print (f"Spieler {gewonnen} hat gewonnen!")
            spiel_aktiv = False
            break

        unentschieden = kontrolle_unentschieden()
        if unentschieden:
            print ("Das Spiel ist Unentschieden ausgegangen")
            spiel_aktiv = False

        spieler_wechseln()