from gameinfo import parse_argument, GameInfo


class GamePlay:
    def __init__(self) -> None:
        self.args = parse_argument()
        self.game_info = GameInfo(self.args.game_number, self.args.output_file)
        self.game_info.init_game_info()

    def truck_zig_zag_path(self):
        pass

    def get_next_trucks_pos(self, truck):
        pass

    def play_trucks(self):
        for truck in self.game_info.get_trucks():
            if truck.last_turn_played != self.game_info.nb_turn:
                if self.game_info.is_crystal_available(truck.pos_x, truck.pos_y):
                    self.game_info.add_actions(truck.action_dig())

                truck.last_turn_played += 1

        self.game_info.nb_turn += 1

    def run(self):
        self.play_trucks()


if __name__ == "__main__":
    gp = GamePlay()
    gp.run()
