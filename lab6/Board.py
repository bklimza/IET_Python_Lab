from Figures import *

def check_name(name):
    if name[0].isdigit():
        raise ValueError("Name cannot start with a digit")
    for char in name:
        if not char.isalnum() and char != '_':
            raise ValueError("Name cannot contain")
    return name


class Board:
    available_figures = {"triangle": Triangle, "rectangle": Rectangle, "square": Square, "circle": Circle}

    def __init__(self):
        self.figures = dict()

    def add(self, figure, name, *size):
        name = check_name(name)

        if name in self.figures.keys():
            raise ValueError("Name is already taken")
        if figure not in Board.available_figures:
            raise ValueError("There is not this figure")
        else:
            self.figures[name] = Board.available_figures[figure.lower()](*size)

    def remove(self, name):
        if name in self.figures.keys():
            del self.figures[name]
        else:
            raise ValueError("Unknown name")

    def quit(self):
        for figure in self.figures.values():
            print(figure)

    def help(self):
        print('add <figure> <name> <size>\n\
        remove <name>\n\
        move <name> <vector>\n\
        scale <name> <ratio>\n\
        rotate <name> <angle>\n\
        set_border_colour <name> <colour>\n\
        set_background_colour <name> <colour>\n\
        help\n\
        quit\n\n\
        <figure> - jedna z figur: circle, square, rectangle, triangle\n\
        <name> - dowolny unikatowy identyfikator mogący zawierać litery, cyfry i podkreślniki, nie zaczynający się od \
         cyfry\n\
        <ratio> - dowolna liczba rzeczywista, różna od 0\n\
        <angle> - dowolny kąt w stopniach\n\
        <colour> to jedno z: black, white, red, green, blue, cyan, magenta, yellow\n\
        Każda figura po dodaniu ma środek w punkcie (0, 0).')

    board_commands = {"help": help, "quit": quit, "add": add, "remove": remove}
    figure_commands = {"move", "scale", "rotate", "set_border_colour", "set_background_colour"}

    def make_figure_command(self, function, name, parameters):
        if name in self.figures.keys():
            if function == "scale":
                self.figures[name].scale(*parameters)
            if function == "move":
                self.figures[name].move(*parameters)
            if function == "rotate":
                self.figures[name].rotate(*parameters)
            if function == "set_background_colour":
                self.figures[name].set_background_colour(*parameters)
            if function == "set_border_colour":
                self.figures[name].set_border_colour(*parameters)
        else:
            raise ValueError("Unknown name")

    class CommandLine:
        def __init__(self, line):
            parts = line.split()
            self.command = parts[0].lower()
            if self.command in Board.figure_commands:
                self.name = parts[1]
                self.params = parts[2:]
            else:
                self.params = parts[1:]

    def run(self):
        while True:
            try:
                line = self.CommandLine(input('Type command: '))
                if line.command == 'quit':
                    self.board_commands[line.command](self)
                    break
                elif line.command in self.figure_commands:
                    self.make_figure_command(line.command, line.name, line.params)
                elif line.command in self.board_commands:
                    self.board_commands[line.command](self, *line.params)

                else:
                    print('Unknown command. Type \'help\' for see commands with description.')
            except (ValueError, IndexError, TypeError) as e:
                print(e)
