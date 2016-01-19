class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return str(self.X) + "," + str(self.Y)


class Tile:
    def __init__(self, position, type, color):
        self.Position = position
        self.Color = color
        self.Width = 40
        self.Height = 40
        if type is not "neutral" and type is not "fight" and type is not "spawn":
            raise Exception("Invalid Type, use \'neutral\', \'fight\' or \'spawn\'")
        else:
            self.Type = type
            if type == "spawn":
                self.Width = 60
                self.Height = 60
            elif type == "fight":
                self.Width = 40
                self.Height = 40

    def __str__(self):
        return self.Position






