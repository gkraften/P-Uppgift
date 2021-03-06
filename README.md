# Specifikation

## Inledning

Jag tänkte programmera ett reversi-spel (egentligen othello) där man dels ska kunna spela två spelare men även mot datorn. Programmet kommer ha ett grafiskt gränssnitt och börja med en meny där man kan välja om man vill köra mot en annan spelare, om man vill spela mot datorn eller avsluta. När man startar ett spel får man välja storlek på planen inom vissa gränser och när spelet är över kommer man tillbaka till menyn.

Gränsnittet kommer till huvuddelen att bestå av en spelplan. Över spelplanen står det vems tur det är och det finns även en knapp som låter en stå över en runda. När någon vunnit kommer ett meddelande upp i fönstret.

En av de större utmaningarna kommer att vara att se till att man bara kan spela när det är sin egen tur och att man inte kan göra otillåtna drag.

## Användarscenarier

### Två spelare

Leo har utmanat Sofie på reversi. De öppnar programmet och möts av en meny där de väljer att spela ett spel med två spelare. De väljer en spelplan av storleken 10x10 rutor. En spelplan dyker upp där det står att svart börjar och eftersom de har kommit överrens om att Sofie är svart är det hon som börjar. Efter att ha spelat ett tag lägger Leo den sista brickan och fyller spelplanen. Ett meddelande dyker upp som säger att svart hade flest brickor så svart vinner. Dessutom blev det ett highscore. De klickar på "avsluta" i huvudmenyn och Sofie går sedan lyckligt iväg medan Leo sitter kvar och tjurar.

### En spelare

Leo bestämmer att köra en omgång mot datorn för att öva så han kan vinna mot Sofie nästa gång. Han öppnar programmet och möts av en meny där han väljer att spela en spelare. Han tillåts nu att välja färg och han väljer vit. Därefter får han välja storlek på planen och väljer 7x7 rutor. En spelplan dyker upp på skärmen och det står att vit börjar. Efter att ha spelat ett tag tvingas både Leo och datorn att stå över en runda och spelet tar då slut. Ett meddelande dyker upp att svart har flest brickor och vinner. I menyn väljer Leo "avsluta" och inser att han borde göra något annat med sitt liv.

## Kodskelett

#### Klasser som representerar själva spelet.
```python
'''WHITE and BLACK are constants representing the two types of pieces.
1 and -1 were chosen because to switch turn the value just has to
be negated.'''
WHITE = 1
BLACK = -1

class Board:
  '''A class representing the board and what's placed on it.'''
  
  def __init__(self, size):
    '''Initialize a new board of dimensions size*size. It will be initialized
    with two black and two white pieces placed on diagonals in the center.'''
  
  def nflips(self, type, row, col):
    '''Returns how many pieces would be flipped if a piece of color type
    were to be placed at row row and column col. Returns zero if no pieces would
    be flipped or if the cell at row row and column col is already occupied.'''
    
  def is_empty(self, row, col):
    '''Returns whether the cell at row row and column col is empty or not'''
  
  def is_full(self):
    '''Returns whether the board has been filled or not.'''
    
  def place(self, type, row, col):
    '''Places a piece of color type at row row and column col. If the cell
    is occupied or if no pieces are flipped or if the cell lies outside of the board
    an exception will be raised. Returns a list with the positions of all
    pieces that were flipped.'''

class Reversi:
  '''A class representing a game of reversi.'''
  
  def __init__(self, board):
    '''Initializes a game using board board of type Board. The color that
    starts is randomized.'''
  
  def set_turn(self, type):
    '''Sets whose turn it is.'''
  
  def place(self, row, col):
    '''Places a piece of same type as whose turn it currently is at row row
    and column col. Raises the same exceptions as Board.place. Returns a
    list with the positions of all pieces that were flipped.'''
  
  def skip(self):
    '''Lets the color whose turn it currently is to skip its turn.'''
  
  def winner(self):
    '''If both players have skipped their turn or if the board is full a list
    containing the color that has won and by how many pieces is returned. If
    no one has won yet, None is returned.'''
```

#### Klass som representerar en reversi-bot

```python
class Bot:
  '''A class representing a reversi-playing bot. Can be used to play
  one-player games.'''
  
  def __init__(self, game, type):
    '''Initializes the bot with the game game of type Reversi. type is the
    color that the bot plays as.'''
  
  def play(self):
    '''Makes a move. Raises an exception if it is not the bot's turn.
    Returns a list of all pieces that were flipped and None if it skipped its
    turn.'''
```

#### Fel

```python
class OccupiedCellException(Exception):
  '''Exception raised when a piece is placed on a cell that is already
  occupied.'''
  
class NoFlipsException(Exception):
  '''Exception raised when a piece is placed in a way that no pieces
  are flipped.'''
  
class WrongTurnException(Exception):
  '''Exception raised by Bot when it tries to play when it is not
  its turn.'''
```

#### Highscore

```python
def load(path):
  '''Loads highscore from path. If en exception occurs, the highscore
  is set to zero and False is returned. If it is loaded correctly True
  is returned. If the highscore has already been loaded it will be
  overwritten in memory.'''
  
def has_loaded():
  '''Returns whether the highscore has already been loaded.'''

def get_highscore():
  '''Returns the highscore or None if it hasn't been loaded yet.'''
  
def set_highscore(score):
  '''Sets highscore. Does not check if it is higher than the loaded
  one.'''

def save(path):
  '''Writes the highscore to path.'''
```
## Programflöde och dataflöde

Programmet börjar med att ett fönster görs i ordning och kontroll över grafik och input ges till en klass som ansvarar för huvudmenyn. En meny ritas upp med alternativen "En spelare", "Två spelare" och "Avsluta". Väljs "En spelare" lämnas kontroll över grafik och input över till en klass som visar en meny där man tillåts välja färg. När man valt färg eller om man valt "Två spelare" i huvudmenyn lämnas kontrollen över till en klass som visar en meny där man får välja storlek på brädet. Slutligen lämnas kontrollen över till en klass som har hand om själva spelet. Den instansierar ett objekt av Board och ett objekt av Reversi. Har man valt att spela en spelare instansieras även en Bot. Klassen låter spelaren/na placera sina brickor och låter boten spela. När spelet är slut läser den in highscore och uppdaterar den vid behov. Highscoren sparas och kontroll lämnas över till huvudmenyn.
