# P-Uppgift - Oscar Gustavsson (ogust@kth.se)
# E-nivå

# Fult hack för att kunna importera reversi-modulerna
# som ligger i en annan mapp
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.sep + "..")

# Här börjar själva programmet

import reversi
from reversi.highscore import Highscore
import interface


colors = {reversi.WHITE: "vit", reversi.BLACK: "svart"} # Table to translate colors into strings

print(r''' _______  _______           _______  _______  _______ _________
(  ____ )(  ____ \|\     /|(  ____ \(  ____ )(  ____ \\__   __/
| (    )|| (    \/| )   ( || (    \/| (    )|| (    \/   ) (
| (____)|| (__    | |   | || (__    | (____)|| (_____    | |
|     __)|  __)   ( (   ) )|  __)   |     __)(_____  )   | |
| (\ (   | (       \ \_/ / | (      | (\ (         ) |   | |
| ) \ \__| (____/\  \   /  | (____/\| ) \ \__/\____) |___) (___
|/   \__/(_______/   \_/   (_______/|/   \__/\_______)\_______/

''')

print("Välkommen till Reversi av Oscar Gustavsson!")
print("Utmana en kompis i reversi.")
print()

size = int(input("Skriv storleken på brädet (måste vara delbart med två och ligga mellan 4 och 26): "))
print()

board = reversi.Board(size)
game = reversi.Reversi(board)

winner = None
while not winner:
    interface.display_board(board)

    print("Nu ska %s spela!" % colors[game.get_turn()])
    row, col = interface.get_row_col()

    if row is None:
        game.skip()
    else:
        game.place(row, col)

    winner = game.winner()

    print("\n")

if len(winner) == 1:
    print("Det blev lika!")
else:
    print("Vinnaren är %s som vann med %d pjäser!" % (colors[winner[0]], winner[1]))

    score_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "highscore.txt" # Path to high score file. Same directory as script
    Highscore.load(score_path)

    if winner[1] > Highscore.get_highscore():
        print("Nytt high score dessutom!!")

        Highscore.set_highscore(winner[1])
        Highscore.save(score_path)