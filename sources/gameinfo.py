from game.game import init_game
import argparse
from io import StringIO
from contextlib import redirect_stdout


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

    def read_initiale_information(self):
        """Lecture des données brutes provenant de init_game"""
        f_input = StringIO()
        with redirect_stdout(f_input):
            init_game(self.seed)
        f_output = f_input.getvalue()

        print(f_output)

        return f_output

    def run(self):
        raw_data = self.read_initiale_information()
        # Parse data to get game info
        parse = Parse(raw_data)
        self.nb_trucks = parse.parse_trucks()
        self.map_width, self.map_height = parse.parse_map_size()
        self.map = parse.parse_map()

        print("Seed {0}, Output File {1}".format(self.seed, self.output_filemane))


def parse_argument():
    """ "Fonction de lecture des arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description="Play Crystals vs Trucks")
    parser.add_argument("game_number", type=int, help="Game number")
    parser.add_argument("output_file", type=str, help="Output filename")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_argument()

    gi = GameInfo(args.game_number, args.output_file)
    gi.run()
