# import sources.game as game


from asyncio.windows_events import NULL

import os


class GameInfo:
    """Class contenant toutes les informations du jeu"""

    # save_actions data needed ---------------
    actionsFileName = "Game_Actions.txt"
    # grid
    # all game info
    # actions_list

    def __init__(self) -> None:
        """Constructeur de la class"""
        pass


    def save_actions(self, actionsFileName, actions):
        
        #   Check existance
        if os.path.exists(actionsFileName):

            os.remove(actionsFileName)  #   Remove if exist

        else:

            # Create file 
            CmdFile = open(actionsFileName, "w+")

        # TODO insert game info in the output file ---------------------
        
        # TODO insert map in the ouput command file --------------------
        CmdFile.write("###Grid###\n")

        # insert here using writelines(gameGrid)

        CmdFile.write("###End Grid###\n")

        # Write actions part-------------------------------------------

        CmdFile.write("Start !\n")    #   fisrt 

        # Write all actions
        for i in range(len(actions)):
            CmdFile.write(actions[i] + "\n")

        # Close file to finish
        CmdFile.close()
