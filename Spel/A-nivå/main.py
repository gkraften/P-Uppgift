# P-Uppgift - Oscar Gustavsson (ogust@kth.se)
# A-nivå

# Fult hack för att kunna importera reversi-modulerna
# som ligger i en annan mapp
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.sep + "..")

# Här börjar själva programmet

from sfml import sf

from interface.scene.mainmenu import MainMenu

WIDTH = 800
HEIGHT = 600

settings = sf.ContextSettings()
settings.antialiasing_level = 8

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), "Reversi", sf.Style.DEFAULT, settings)

scene = MainMenu(window)

clock = sf.Clock()
while window.is_open:
    events = []

    try:
        for event in window.events:
            if type(event) is sf.CloseEvent:
                window.close()
            else:
                events.append(event)
    except UnboundLocalError: # Catch exception caused by bug in pysfml
        pass

    scene.event(events)

    next_scene = scene.update(clock.restart())

    scene.draw()

    window.display()

    if not next_scene is None:
        scene = next_scene