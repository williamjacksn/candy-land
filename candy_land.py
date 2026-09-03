import collections
import random


def log(message: str) -> None:
    print(message)


class Space:
    def __init__(
        self,
        start: bool = False,
        end: bool = False,
        red: bool = False,
        purple: bool = False,
        yellow: bool = False,
        blue: bool = False,
        orange: bool = False,
        green: bool = False,
        peppermint_pass_start: bool = False,
        peppermint_pass_end: bool = False,
        gummy_pass_start: bool = False,
        gummy_pass_end: bool = False,
        cupcake: bool = False,
        ice_cream: bool = False,
        gummy_star: bool = False,
        gingerbread: bool = False,
        lollypop: bool = False,
        popsicle: bool = False,
        chocolate: bool = False,
        licorice: bool = False,
    ) -> None:
        self.start = start
        self.end = end
        self.red = red
        self.purple = purple
        self.yellow = yellow
        self.blue = blue
        self.orange = orange
        self.green = green
        self.peppermint_pass_start = peppermint_pass_start
        self.peppermint_pass_end = peppermint_pass_end
        self.gummy_pass_start = gummy_pass_start
        self.gummy_pass_end = gummy_pass_end
        self.cupcake = cupcake
        self.ice_cream = ice_cream
        self.gummy_star = gummy_star
        self.gingerbread = gingerbread
        self.lollypop = lollypop
        self.popsicle = popsicle
        self.chocolate = chocolate
        self.licorice = licorice


class Board:
    def __init__(self) -> None:
        self.spaces = [
            Space(start=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True, peppermint_pass_start=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(cupcake=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(ice_cream=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True, gummy_pass_start=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True, gummy_pass_end=True),
            Space(gummy_star=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True, licorice=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True, peppermint_pass_end=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(gingerbread=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True, licorice=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(lollypop=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(popsicle=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(chocolate=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(red=True),
            Space(purple=True),
            Space(yellow=True),
            Space(blue=True),
            Space(orange=True),
            Space(green=True),
            Space(
                end=True,
                red=True,
                purple=True,
                yellow=True,
                blue=True,
                orange=True,
                green=True,
            ),
        ]

    def next_match(self, start: int, attr: str) -> int:
        for i, space in enumerate(self.spaces):
            if i > start and getattr(space, attr):
                return i
        return start


class Card:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"Card(value={self.value!r})"

    @property
    def is_single_color(self) -> bool:
        return self.value in ["red", "orange", "yellow", "green", "blue", "purple"]

    @property
    def is_double_color(self) -> bool:
        return self.value.startswith("double_")

    @property
    def is_special(self) -> bool:
        return self.value in [
            "cupcake",
            "ice_cream",
            "gummy_star",
            "gingerbread",
            "lollypop",
            "popsicle",
            "chocolate",
        ]


class Deck(list):
    def __init__(self) -> None:
        super().__init__()
        for _ in range(6):
            self.append(Card("red"))
            self.append(Card("orange"))
            self.append(Card("yellow"))
            self.append(Card("green"))
            self.append(Card("blue"))
        for _ in range(5):
            self.append(Card("purple"))
        for _ in range(4):
            self.append(Card("double_red"))
            self.append(Card("double_yellow"))
            self.append(Card("double_blue"))
            self.append(Card("double_purple"))
        for _ in range(3):
            self.append(Card("double_orange"))
            self.append(Card("double_green"))
        self.append(Card("cupcake"))
        self.append(Card("ice_cream"))
        self.append(Card("gummy_star"))
        self.append(Card("gingerbread"))
        self.append(Card("lollypop"))
        self.append(Card("popsicle"))
        self.append(Card("chocolate"))

    def draw(self) -> Card:
        return self.pop()

    def shuffle(self) -> None:
        random.shuffle(self)


class Player:
    def __init__(self, color: str) -> None:
        self.color = color
        self.space_index = 0
        self.stuck_in_licorice = False

    def __str__(self) -> str:
        return f"Player {self.color.capitalize()}"

    def __repr__(self) -> str:
        return f"Player(color={self.color!r})"


def play_game(on_screen: bool = False) -> dict:
    result = {}
    game_on = True
    if on_screen:
        log("== Let's play Candy Land!")
    players = [Player(color) for color in ("red", "yellow", "green", "blue")]
    board = Board()
    deck = Deck()
    deck.shuffle()
    round_no = 0
    while game_on:
        round_no += 1
        if on_screen:
            log(f"= Beginning of round {round_no}")
            log(f"= {len(deck)} cards left in the deck.")
        for player in players:
            if on_screen:
                m = "{} is on space {} and takes a turn."
                log(m.format(player, player.space_index))
            if player.stuck_in_licorice:
                if on_screen:
                    m = "{} is stuck in licorice and misses this turn."
                    log(m.format(player))
                player.stuck_in_licorice = False
                continue
            if len(deck) == 0:
                if on_screen:
                    log("The deck is empty! Shuffling a new deck.")
                deck = Deck()
                deck.shuffle()
            card = deck.draw()
            if on_screen:
                m = "{} draws a card: {}"
                log(m.format(player, card))
            if card.is_single_color:
                start = player.space_index
                player.space_index = board.next_match(start, card.value)
            if card.is_double_color:
                color = card.value[7:]
                start = player.space_index
                step = board.next_match(start, color)
                player.space_index = board.next_match(step, color)
            if card.is_special:
                player.space_index = board.next_match(0, card.value)
            if on_screen:
                m = "{} moves to space {}."
                log(m.format(player, player.space_index))
            space = board.spaces[player.space_index]
            if space.end:
                result["winner"] = player
                result["rounds"] = round_no
                game_on = False
                if on_screen:
                    log(f"{player} wins!")
                break
            if space.peppermint_pass_start:
                player.space_index = board.next_match(0, "peppermint_pass_end")
                if on_screen:
                    m = "{} goes down Peppermint Pass to space {}."
                    log(m.format(player, player.space_index))
                continue
            if space.gummy_pass_start:
                player.space_index = board.next_match(0, "gummy_pass_end")
                if on_screen:
                    m = "{} goes down Gummy Pass to space {}."
                    log(m.format(player, player.space_index))
                continue
            if space.licorice:
                player.stuck_in_licorice = True
                if on_screen:
                    log(f"{player} gets stuck in licorice!")
                continue
        if on_screen:
            log(f"= End of round {round_no}")
    return result


def main() -> None:
    stats = collections.Counter()
    for _ in range(10000):
        result = play_game(on_screen=False)
        winner = result["winner"]
        stats.update([winner.color + "_win"])
        rounds = str(result["rounds"])
        stats.update([rounds + "_rounds"])
    print(stats)


if __name__ == "__main__":
    main()
