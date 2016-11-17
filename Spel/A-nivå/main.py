# P-Uppgift - Oscar Gustavsson (ogust@kth.se)
# A-nivå

# Fult hack för att kunna importera reversi-modulerna
# som ligger i en annan mapp
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.sep + "..")

# Här börjar själva programmet

import sfml as sf

WIDTH = 640
HEIGHT = 480

window = sf.graphics.RenderWindow(sf.window.VideoMode(WIDTH, HEIGHT), "Reversi")

while window.is_open:
    for event in window.events:
        if type(event) is sf.window.CloseEvent:
            window.close();

    window.clear(sf.graphics.Color.WHITE)

    window.display()