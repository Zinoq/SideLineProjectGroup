class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Tile:
    def __init__(self, position, type):
        self.Position = position
        if type is not "neutral" and type is not "fight" and type is not "spawn":
            raise Exception("Invalid Type, use \'neutral\', \'fight\' or \'spawn\'")
        else:
            self.Type = type


# a = Tile(Point(2,5),"spawn")
