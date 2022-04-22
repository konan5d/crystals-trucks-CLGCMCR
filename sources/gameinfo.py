import os
from game.game import init_game
import argparse
from io import StringIO
from contextlib import redirect_stdout


class GameInfo:
    """Class contenant toutes les informations du jeu"""
    def __init__(self, arg_seed, arg_filename) -> None:
        """Constructeur de la class"""
        self.seed = arg_seed
        self.output_filemane = arg_filename

        self.read_initiale_information()

    def read_initiale_information(self):
        """Lecture des données brutes provenant de init_game"""
        f_input = StringIO()
        with redirect_stdout(f_input):
            init_game(self.seed)
        f_output = f_input.getvalue()

        print(f_output)

        return f_output

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
