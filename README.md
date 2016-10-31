# Specifikation

## Inledning

Jag tänkte programmera ett reversi-spel (egentligen othello) där man dels ska kunna spela två spelare men även mot datorn. Programmet kommer ha ett grafiskt gränssnitt och börja med en meny där man kan välja om man vill köra mot en annan spelare, om man vill spela mot datorn eller avsluta. När man startar ett spel får man välja storlek på planen inom vissa gränser och när spelet är över kommer man tillbaka till menyn.

Gränsnittet kommer till huvuddelen att bestå av en spelplan. Över spelplanen står det vems tur det är och det finns även en knapp som låter en stå över en runda. När någon vunnit kommer ett meddelande upp i fönstret.

En av de större utmaningarna kommer att vara att se till att man bara kan spela när det är sin egen tur och att man inte kan göra otillåtna drag.

## Användarscenarier

### Två spelare

Leo har utmanat Sofie på reversi. De öppnar programmet och möts av en meny där de väljer att spela ett spel med två spelare. De väljer en spelplan av storleken 10x10 rutor. En spelplan dyker upp där det står att svart börjar och eftersom de har kommit överrens om att Sofie är svart är det hon som börjar. Efter att ha spelat ett tag lägger Leo den sista brickan och fyller spelplanen. Ett meddelande dyker upp som säger att svart hade flest brickor så svart vinner. Dessutom blev det ett highscore. De klickar på "avsluta" i huvudmenyn och Sofie går sedan lyckligt iväg medan Leo sitter kvar och tjurar.

## En spelare

Leo bestämmer att köra en omgång mot datorn för att öva så han kan vinna mot Sofie nästa gång. Han öppnar programmet och möts av en meny där han väljer att spela en spelare. Han tillåts nu att välja färg och han väljer vit. Därefter får han välja storlek på planen och väljer 7x7 rutor. En spelplan dyker upp på skärmen och det står att vit börjar. Efter att ha spelat ett tag tvingas både Leo och datorn att stå över en runda och spelet tar då slut. Ett meddelande dyker upp att svart har fläst brickor och vinner. I menyn väljer Leo "avsluta" och inser att han borde göra något annat med sitt liv.
