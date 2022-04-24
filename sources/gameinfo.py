from game import init_game

# from game.game import init_game
import argparse
from io import StringIO
from contextlib import redirect_stdout
import os


def split(data_to_split):
    data_splited = []
    if len(data_to_split):
        for data in data_to_split:
            data_splited.append(data)

    return data_splited


class Parse:
    def __init__(self, data_to_parse):
        self.data_to_parse = data_to_parse.split("\n")

    def parse_map(self):
        _map = []
        map_idx_start = self.data_to_parse.index("### Grid ###")
        map_idx_end = self.data_to_parse.index("### End Grid ###")

        tmp_map = self.data_to_parse[map_idx_start + 1 : map_idx_end]

        for y in tmp_map:
            _map.append(split(y))

        return _map

    def parse_map_size(self):
        map_size_info = self.data_to_parse[1:3]
        w = map_size_info[0].split(" ")[1]
        h = map_size_info[1].split(" ")[1]

        return w, h

    def parse_trucks(self):
        trucks_info = self.data_to_parse[0]

        return trucks_info.split(" ")[1]


class GameInfo:
    """Class contenant toutes les informations du jeu"""

    def __init__(self, arg_seed, arg_filename) -> None:
        """Constructeur de la class"""
        self.seed = arg_seed
        self.output_filemane = arg_filename

        self.raw_data = ""

        self.map_width = 0
        self.map_height = 0
        self.map = 0

        self.nb_turn = 0
        self.nb_crystals_dig = 0

        self.nb_trucks = 0
        # TODO : liste d'objet Truck
        self.trucks = []

        self.actions = []

    def read_initiale_information(self):
        """Lecture des données brutes provenant de init_game"""
        f_input = StringIO()
        with redirect_stdout(f_input):
            init_game(self.seed)
        f_output = f_input.getvalue()

        print(f_output)

        return f_output

    def init_truck(self, id, x, y):
        return Truck(id, x, y)

    def init_all_trucks(self):
        self.trucks.append(self.init_truck(0, 0, 0))

    def get_trucks(self):
        return self.trucks

    def save_actions(self, actionsFileName, actions):
        """Enregistrement des actions dans un fichier"""
        # Check existance
        CmdFile = None
        if os.path.exists(actionsFileName):
            os.remove(actionsFileName)  # Remove if exist
            CmdFile = open(actionsFileName, "w+")
        else:
            # Create file
            CmdFile = open(actionsFileName, "w+")

        # TODO insert game info in the output file ---------------------

        # TODO insert map in the ouput command file --------------------
        CmdFile.write("###Grid###\n")

        # insert here using writelines(gameGrid)

        CmdFile.write("###End Grid###\n")

        # Write actions part-------------------------------------------

        CmdFile.write("Start !\n")  # fisrt

        # Write all actions
        for i in range(len(actions)):
            CmdFile.write(actions[i] + "\n")

        # Close file to finish
        CmdFile.close()

    def add_actions(self, action):
        final_action = str(self.nb_turn) + action
        self.actions.append(final_action)

    def init_game_info(self):
        raw_data = self.read_initiale_information()
        # Parse data to get game info
        parse = Parse(raw_data)
        self.nb_trucks = parse.parse_trucks()
        self.map_width, self.map_height = parse.parse_map_size()
        self.map = parse.parse_map()

        # On initialise les camions
        self.init_all_trucks()

    def is_crystal_available(self, x, y):
        print(self.map)
        if self.map[x][y] != " ":
            return True
        else:
            return False


def parse_argument():
    """ "Fonction de lecture des arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description="Play Crystals vs Trucks")
    parser.add_argument("game_number", type=int, help="Game number")
    parser.add_argument("output_file", type=str, help="Output filename")

    args = parser.parse_args()

    return args


class Truck:
    """Class contenant toutes les informations des camions"""

    def __init__(self, id, x, y) -> None:
        """Constructeur de la class"""
        self.id = id
        self.pos_x = x
        self.pos_y = y

        self.last_turn_played = -1

    def action_move(self, x, y):
        """Deplacement du camion"""
        action = "MOVE" + " " + str(self.id) + " " + str(x) + " " + str(y)

        return action

    def action_dig(self):
        """Creuser un cristal"""
        dig = "DIG" + " " + str(self.id) + " " + str(self.pos_x) + " " + str(self.pos_y)

        return dig


if __name__ == "__main__":

    args = parse_argument()

    gi = GameInfo(args.game_number, args.output_file)
    gi.init_game_info()
