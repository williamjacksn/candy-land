import random


def log(message):
    print(message)


class Space(object):
    def __init__(self, start=False, end=False, red=False, purple=False,
                 yellow=False, blue=False, orange=False, green=False,
                 peppermint_pass_start=False, peppermint_pass_end=False,
                 gummy_pass_start=False, gummy_pass_end=False, cupcake=False,
                 ice_cream=False, gummy_star=False, gingerbread=False,
                 lollypop=False, popsicle=False, chocolate=False,
                 licorice=False):
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


class Board(object):
    def __init__(self):
        self.spaces = [
            Space(start=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True, peppermint_pass_start=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(cupcake=True), Space(yellow=True),
            Space(blue=True), Space(orange=True), Space(green=True),
            Space(red=True), Space(purple=True), Space(yellow=True),
            Space(blue=True), Space(orange=True), Space(green=True),
            Space(ice_cream=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(yellow=True, gummy_pass_start=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True, gummy_pass_end=True),
            Space(gummy_star=True), Space(blue=True), Space(orange=True),
            Space(green=True, licorice=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True, peppermint_pass_end=True),
            Space(blue=True), Space(orange=True), Space(green=True),
            Space(red=True), Space(purple=True), Space(yellow=True),
            Space(blue=True), Space(orange=True), Space(gingerbread=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True, licorice=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(blue=True),
            Space(orange=True), Space(green=True), Space(red=True),
            Space(purple=True), Space(yellow=True), Space(lollypop=True),
            Space(blue=True), Space(orange=True), Space(green=True),
            Space(red=True), Space(purple=True), Space(yellow=True),
            Space(blue=True), Space(orange=True), Space(green=True),
            Space(popsicle=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(chocolate=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(red=True), Space(purple=True),
            Space(yellow=True), Space(blue=True), Space(orange=True),
            Space(green=True), Space(end=True, red=True, purple=True,
                                     yellow=True, blue=True, orange=True,
                                     green=True)
        ]

    def next_match(self, start, attr):
        for i, space in enumerate(self.spaces):
            if i > start and getattr(space, attr):
                return i
        return start


class Card(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return 'Card(value={})'.format(repr(self.value))

    @property
    def is_single_color(self):
        return self.value in ['red', 'orange', 'yellow',
                              'green', 'blue', 'purple']

    @property
    def is_double_color(self):
        return self.value.startswith('double_')

    @property
    def is_special(self):
        return self.value in ['cupcake', 'ice_cream', 'gummy_star',
                              'gingerbread', 'lollypop', 'popsicle',
                              'chocolate']


class Deck(object):
    def __init__(self):
        self.cards = []
        for _ in range(6):
            self.cards.append(Card(value='red'))
            self.cards.append(Card(value='orange'))
            self.cards.append(Card(value='yellow'))
            self.cards.append(Card(value='green'))
            self.cards.append(Card(value='blue'))
        for _ in range(5):
            self.cards.append(Card(value='purple'))
        for _ in range(4):
            self.cards.append(Card(value='double_red'))
            self.cards.append(Card(value='double_yellow'))
            self.cards.append(Card(value='double_blue'))
            self.cards.append(Card(value='double_purple'))
        for _ in range(3):
            self.cards.append(Card(value='double_orange'))
            self.cards.append(Card(value='double_green'))
        self.cards.append(Card(value='cupcake'))
        self.cards.append(Card(value='ice_cream'))
        self.cards.append(Card(value='gummy_star'))
        self.cards.append(Card(value='gingerbread'))
        self.cards.append(Card(value='lollypop'))
        self.cards.append(Card(value='popsicle'))
        self.cards.append(Card(value='chocolate'))

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class Player(object):
    def __init__(self, color):
        self.color = color
        self.space_index = 0
        self.stuck_in_licorice = False

    def __str__(self):
        return 'Player {}'.format(self.color.capitalize())

    def __repr__(self):
        return 'Player(color={})'.format(repr(self.color))


def main():
    game_on = True
    log('== Let\'s play Candy Land!')
    players = list()
    for color in ['red', 'yellow', 'green', 'blue']:
        players.append(Player(color))
    board = Board()
    deck = Deck()
    deck.shuffle()
    round_no = 0
    while game_on:
        round_no = round_no + 1
        log('= Beginning of round {}'.format(round_no))
        log('= {} cards left in the deck.'.format(len(deck.cards)))
        for player in players:
            m = '{} is on space {} and takes a turn.'
            log(m.format(player, player.space_index))
            if player.stuck_in_licorice:
                m = '{} is stuck in licorice and misses this turn.'
                log(m.format(player))
                player.stuck_in_licorice = False
                continue
            if len(deck.cards) == 0:
                log('The deck is empty! Shuffling a new deck.')
                deck = Deck()
                deck.shuffle()
            card = deck.draw()
            m = '{} draws a card: {}'
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
            m = '{} moves to space {}.'
            log(m.format(player, player.space_index))
            space = board.spaces[player.space_index]
            if space.end:
                game_on = False
                log('{} wins!'.format(player))
                break
            if space.peppermint_pass_start:
                player.space_index = board.next_match(0, 'peppermint_pass_end')
                m = '{} goes down Peppermint Pass to space {}.'
                log(m.format(player, player.space_index))
                continue
            if space.gummy_pass_start:
                player.space_index = board.next_match(0, 'gummy_pass_end')
                m = '{} goes down Gummy Pass to space {}.'
                log(m.format(player, player.space_index))
                continue
            if space.licorice:
                player.stuck_in_licorice = True
                log('{} gets stuck in licorice!'.format(player))
                continue
        log('= End of round {}'.format(round_no))

if __name__ == '__main__':
    main()
