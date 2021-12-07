class Submarine:

    x: int = 0
    y: int = 0
    aim: int = 0

    def __init__(self, file):
        [self.move(command) for command in file.readlines()]
        print(self.x * self.y)

    def move(self, command):

        distance: int = int(command.split(' ')[1])

        if 'up' in command:
            self.aim = self.aim - distance

        if 'down' in command:
            self.aim = self.aim + distance

        if 'forward' in command:
            self.x = self.x + distance
            self.y = self.y + (distance * self.aim)


if __name__ == '__main__':
    with open('/Users/whaley/Dev/AOC21/D2/d2_input.txt') as f:
        sub = Submarine(f)
