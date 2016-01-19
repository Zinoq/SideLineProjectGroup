class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return str(self.X) + "," + str(self.Y) #if we want to print the location of a player


class Tile:
    def __init__(self, position, type, color, size):
        self.Position = position
        self.Color = color
        self.Width = size
        self.Height = self.Width
        self.Size = size
        if type is not "neutral" and type is not "fight" and type is not "spawn":
            raise Exception("Invalid Type, use \'neutral\', \'fight\' or \'spawn\'")
        else:
            self.Type = type
            if type == "spawn":
                self.Width = size
                self.Height = size
            elif type == "fight":
                self.Width = size
                self.Height = size

    def __str__(self):
        return self.Position






