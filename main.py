from guizero import *
import sys, dataset
from collections import OrderedDict

# Die Funktionen für den Betrieb werden aufgestellt


# Funktion zum schließen der Applikation
def close():
    if yesno("Beenden", "Willst du das Programm wirklich beenden?"):
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


# Hilfe ändern
def help_chooser(topic):
    help_text.value = topic


# Leere Funktion, wenn keine andere verwendet wird
def placeholder():
    pass


# Die Basis Applikation wird erstellt
app = App(title="MathDB", layout="grid", bg="white")
app.on_close(close)
menu_bar = MenuBar(app, toplevel=["Datei", "Über"],
                   options=[[["Schließen", close]], [["Hilfe", open_help], ["Version: 0.1a", extended_version_info]]])

# Hilfe Fenster erstellen
help_window = Window(app, title="Hilfe", visible=False, bg="white")
help_text_box = Box(help_window, width="fill", height="fill", border=True)
help_topic_chooser = ListBox(help_text_box, items=["Main", "   Sub", "   Another Sub", "Another Main", "   And Sub"], height="fill", align="left", command=help_chooser)
help_text = Text(help_text_box, width="fill")
help_window_buttons = Box(help_window, align="bottom", width="fill")
help_close_button = PushButton(help_window_buttons, text="Close", command=close_help, align="right", pady=1)


# Applikation wird angezeigt
app.display()
