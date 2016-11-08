# P-Uppgift - Oscar Gustavsson (ogust@kth.se)
# E-nivå

# Fult hack för att kunna importera reversi-modulerna
# som ligger i en annan mapp
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.sep + "..")

# Här börjar själva programmet