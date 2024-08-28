# Titel 
print("Tic-Tac-Toe Spiel")

# Variablen
spiel_aktiv = True
feld_belegt = False
spieler_aktuell = "X"

# Spielfeld definieren
spielfeld = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# Spielfeld ausgeben
def spielfeld_ausgeben():
    print(spielfeld[1] + '|' + spielfeld[2] + '|' + spielfeld[3])
    print(spielfeld[4] + '|' + spielfeld[5] + '|' + spielfeld[6])
    print(spielfeld[7] + '|' + spielfeld[8] + '|' + spielfeld[9])

# Spielereingabe 
def spieler_eingabe():
    global spiel_aktiv, feld_belegt

    while True:
        if feld_belegt:
            spielzug = input("Bitte ein anderes Feld eingeben: ")
        else:
            spielzug = input("Bitte Feld eingeben: ")

        if spielzug == 'exit':
            spiel_aktiv = False
            return print("Das Spiel wurde beendet.")

        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte eine Zahl eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == 'X' or spielfeld[spielzug] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                    feld_belegt = True
                else:
                    return spielzug
            else:
                print("Bitte eine Zahl zwischen 1 und 9 eingeben")

# Spieler wechseln
def spieler_wechseln():
    global spieler_aktuell

    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'

# Kontrolle auf Gewinnen
def kontrolle_gewonnen():
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[1]
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        return spielfeld[3]

# Kontrolle auf Unentschieden
def kontrolle_unentschieden():
    if (spielfeld[1] == 'X' or spielfeld[1] == 'O') and (spielfeld[2] == 'X' or spielfeld[2] == 'O') and (spielfeld[3] == 'X' or spielfeld[3] == 'O') and \
       (spielfeld[4] == 'X' or spielfeld[4] == 'O') and (spielfeld[5] == 'X' or spielfeld[5] == 'O') and (spielfeld[6] == 'X' or spielfeld[6] == 'O') and \
       (spielfeld[7] == 'X' or spielfeld[7] == 'O') and (spielfeld[8] == 'X' or spielfeld[8] == 'O') and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
        return ('unentschieden')

# Hauptschleife
spielfeld_ausgeben()
while spiel_aktiv:
    print("Der Spieler " + spieler_aktuell + " ist am Zug.")
    
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()

        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print ("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
            break

        unentschieden = kontrolle_unentschieden()
        if unentschieden:
            print ("Das Spiel ist Unentschieden ausgegangen")
            spiel_aktiv = False

        spieler_wechseln()