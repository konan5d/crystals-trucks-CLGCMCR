from gameinfo import parse_argument, GameInfo


class GamePlay:
    def __init__(self) -> None:
        self.args = parse_argument()
        self.game_info = GameInfo(self.args.game_number, self.args.output_file)
        self.game_info.init_game_info()


if __name__ == "__main__":
    gp = GamePlay()
