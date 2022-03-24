
import math 

class Distance:
    
    def __init__(self, xCoord, yCoord, zCoord) -> None:
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord


    def dist_from_origin(self) -> int:
        dist = math.sqrt((self.xCoord**2)+(self.yCoord**2)+(self.zCoord**2))
        return dist

    def get_coordinates(self) -> tuple:
        return (self.xCoord, self.yCoord, self.zCoord)

