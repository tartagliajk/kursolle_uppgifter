#moment 2 inlämnings uppgift a, med fördjupning
#importerar pi från math
from math import pi
#input blir till str, sedan ändras svaret till versaler för att kunna funka i if-satsen
tal=str(input("Vill du skriva in ett heltal eller decimaltal?\n"))
tal=tal.upper()
if tal=="HELTAL":
    r=int(input("Skriv in en radie\n"))
    omkrets=r*2*pi
    area=r**2*pi
    print("Cirkelns radie är {} och detta gör så att omkretsen är {:.2f} och arean är {:.2f}".format(r,omkrets,area))
if tal=="DECIMALTAL":
    r=float(input("Skriv in en radie\n"))
    omkrets=r*2*pi
    area=r**2*pi
    print("Cirkelns radie är {} och detta gör så att omkretsen är {:.2f} och arean är {:.2f}".format(r,omkrets,area))