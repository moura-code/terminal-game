


from deck import Deck

from game import *

class Player():

    deck:Deck

    life:int

    strength:int

    agility:int

    curses:list
    
   
    def __init__(self) -> None:
        self.life = 100
        self.deck = Deck()    

