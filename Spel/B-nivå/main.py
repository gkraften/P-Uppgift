# P-Uppgift - Oscar Gustavsson (ogust@kth.se)
# B-nivå

# Fult hack för att kunna importera reversi-modulerna
# som ligger i en annan mapp
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.sep + "..")

# Här börjar själva programmet

import reversi
from reversi.highscore import Highscore
from reversi.exceptions import *
from reversi.bot import Bot
import interface
import time


colors = {reversi.WHITE: "vit", reversi.BLACK: "svart"} # Table to translate colors into strings
score_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "highscore.txt" # Path to high score file. Same directory as script
player = reversi.WHITE

print(r''' _______  _______           _______  _______  _______ _________
(  ____ )(  ____ \|\     /|(  ____ \(  ____ )(  ____ \\__   __/
| (    )|| (    \/| )   ( || (    \/| (    )|| (    \/   ) (
| (____)|| (__    | |   | || (__    | (____)|| (_____    | |
|     __)|  __)   ( (   ) )|  __)   |     __)(_____  )   | |
| (\ (   | (       \ \_/ / | (      | (\ (         ) |   | |
| ) \ \__| (____/\  \   /  | (____/\| ) \ \__/\____) |___) (___
|/   \__/(_______/   \_/   (_______/|/   \__/\_______)\_______/
                          Nu med bot

''')

print("Välkommen till Reversi av Oscar Gustavsson!")
print("Utmana datorn i reversi.")
print("För att avsluta tryck ctrl+C.")
print()

if not Highscore.load(score_path):
    print("High score kunde inte läsas in. Sätter till 0 poäng.\n")

try:
    size = interface.get_int("Skriv storleken på brädet (måste vara delbart med två och ligga mellan 4 och 26): ", "Du måste skriva ett tal!")
    while not 4 <= size <= 26 or size % 2 == 1:
        print("Måste vara delbart med två och ligga mellan 4 och 26!")
        size = interface.get_int("Skriv storleken på brädet (måste vara delbart med två och ligga mellan 4 och 26): ", "Du måste skriva ett tal!")
    print()

    board = reversi.Board(size)
    game = reversi.Reversi(board)
    bot = Bot(game, -player)

    winner = None
    while not winner:
        interface.display_board(board)

        if game.get_turn() == player:
            print("Din tur (%s) att spela!" % colors[player])

            if interface.should_skip():
                game.skip()
            else:
                success = False
                while not success:
                    row, col = interface.get_row_col(size)
                    error = False

                    try:
                        game.place(row, col)
                        success = True
                    except NoFlipsException:
                        print("Minst en bricka måste vändas varje omgång.")
                        error = True
                    except OccupiedCellException:
                        print("Cellen är redan upptagen.")
                        error = True

                    if error and interface.should_skip():
                        game.skip()
                        success = True
        else:
            print("Datorns tur att spela!")

            flips = bot.play()

            if flips is None:
                print("Datorn hoppade över sin tur.")
            else:
                print("Datorn har vänt %d pjäser." % len(flips))

        winner = game.winner()

        print("\n")

    if len(winner) == 1:
        print("Det blev lika!")
    else:
        win_player = "du" if winner[0] == player else "datorn"
        print("Vinnaren är %s som vann med %d pjäser!" % (win_player, winner[1]))

        if winner[1] > Highscore.get_highscore() and winner[0] == player:
            print("Nytt high score dessutom!!")

            Highscore.set_highscore(winner[1])

            try:
                Highscore.save(score_path)
            except:
                print("Misslyckades med att spara nya high score.")
except KeyboardInterrupt:
    print("\nHejdå!!")