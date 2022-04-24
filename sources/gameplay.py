from gameinfo import Truck, parse_argument, GameInfo


class GamePlay:
    def __init__(self) -> None:
        self.args = parse_argument()
        self.game_info = GameInfo(self.args.game_number, self.args.output_file)
        self.game_info.init_game_info()

    def get_truck_actions_available(self, map: list, truck: Truck):
        truck.actions_available.clear()

        if self.game_info.is_crystal_available(truck.pos_x, truck.pos_y):
            truck.actions_available.append(truck.action_dig())
        else:
            print(self.game_info.is_movable(truck, truck.pos_x, truck.pos_y))

    def get_next_trucks_pos(self, truck: Truck):
        pass

    def play_trucks(self):
        for truck in self.game_info.get_trucks():
            if truck.last_turn_played != self.game_info.nb_turn:
                self.get_truck_actions_available([], truck)

                truck.last_turn_played += 1

        self.game_info.nb_turn += 1

    def run(self):
        self.play_trucks()


if __name__ == "__main__":
    gp = GamePlay()
    gp.run()
