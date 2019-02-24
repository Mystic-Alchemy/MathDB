from guizero import *
import sys, dataset
from collections import OrderedDict

# Die Funktionen für den Betrieb werden aufgestellt


# Funktion zum schließen der Applikation
def close():
    if yesno("CLose", "Do you really want to quit?"):
        exit(1)


# Öffne mehr Informationen über die App/Version
def extended_version_info():
    info("Version: 0.1a", "Geschrieben von PilleniusMC|Mystic-Alchemy.\nDiese Applikation ist komplett Open Source.")


# Hilfe öffnen
def open_help():
    help_window.show(wait=True)


# Hilfe schließen
def close_help():
    help_window.hide()


# Leere Funktion, wenn keine andere verwendet wird
def placeholder():
    pass


# Die Basis Applikation wird erstellt
app = App(title="MathDB", layout="grid", bg="white")
menu_bar = MenuBar(app, toplevel=["Datei", "Über"],
                   options=[[["Schließen", close]], [["Hilfe", open_help], ["Version: 0.1a", extended_version_info]]])

# Hilfe Fenster erstellen
help_window = Window(app, title="Hilfe", layout="grid", visible=False, bg="white")
help_close_button = PushButton(help_window, text="Close", command=close_help, grid=[0, 0], pady=1)


# Applikation wird angezeigt
app.display()
