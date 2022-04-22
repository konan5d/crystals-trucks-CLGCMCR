# import sources.game as game
import argparse


class GameInfo:
    """Class contenant toutes les informations du jeu"""

    def __init__(self, arg_seed, arg_filename) -> None:
        """Constructeur de la class"""
        self.seed = arg_seed
        self.output_filemane = arg_filename

    def run(self):
        print("Seed {0}, Output File {1}".format(self.seed, self.output_filemane))


def parse_argument():
    parser = argparse.ArgumentParser(description="Play Crystals vs Trucks")
    parser.add_argument("game_number", type=int, help="Game number")
    parser.add_argument("output_file", type=str, help="Output filename")

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_argument()

    gi = GameInfo(args.game_number, args.output_file)
    gi.run()
