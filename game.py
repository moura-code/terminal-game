from player import *




class Game():
    
    player:Player


    ## example of propety
    _floor:int

    @property
    def floor(self) -> int:
        return self._floor

    @floor.setter
    def floor(self, floor: int) -> None:
        self._floor = floor



    def __init__(self) -> None:
        self._floor=1
        player = Player()
        print(player.life)
        
        
   

        



    
    
    

   


