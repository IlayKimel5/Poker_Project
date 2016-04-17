import random
import copy

# TODO: General Notes:
# comments should be one line before the code, not in the same line. see below:
# comment
pass

# you should seperate functional parts with a newline and put a short comment documenting what each part does for clearity

# for easily renaming of a variables name (refactoring) right click on it refactor->rename or shift+F6




all_cards = []  # a list of all the cards

# TODO: variable names in python are written with Snake Case naming convention - https://en.wikipedia.org/wiki/Snake_case

# e.g type_card instead of typecard

# TODO: having descriptive names is preferable to comments when readable. consider a name like:
# possible_card_types instead of type_card
typecard = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # a list of the card types possible
suit = [' spades', ' diamonds', ' hearts', ' clubs']  # a list of the card suits possible

# TODO: change to a more pythonic way
# you can create all_cards in one line (hint: use list comprehensions)
for typec in typecard:  # creats the list all_cards
    for suitcard in suit:
        lentypec = len(typec)
        typec += suitcard
        all_cards.append(typec)
        typec = typec[0:lentypec]


def cards():
    # the output is a list of a random card (card_type and suit)
    # the output is a list of all cards possible
    # TODO: It cant be both above, can't it? ^^

    # TODO: h is non descriptive name, I can't understand what it represents without diving into your code. This should be avoided when possible
    h = 1
    card = 0
    while h > 0:
        # TODO: consider representing a card as type other then string with easy acess to type and suit.
        # TODO: I would suggest using a neat thing called namedtuple - https://docs.python.org/2/library/collections.html#collections.namedtuple

        # TODO: reuse the previous list of available card types and suits
        rand_typecard = random.choice(
            ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])  # random card type
        rand_suit = random.choice([' spades', ' diamonds', ' hearts', ' clubs'])  # selects a random suit for the card
        rand_typecard += rand_suit
        card = rand_typecard

        # TODO: I may be missing somethign here, but I think your entire function is too complex. check out the following lines
        # card = random.choice(all_cards)
        # all_cards.remove(card)
        # return card

        for i in all_cards:
            if i == card:
                all_cards.remove(i)
                h -= 1
        if h >= 1:
            card = 0
    return card


def hand():
    l_hand = []
    # the input is the function card()
    # the output is a list of two cards

    # TODO: use a list comprehension

    for i in range(5):
        l_hand.append(cards())
    return l_hand


def hand_big_to_small(l_hand):
    # the input is a hand
    # the output is the hand from biggest to smallest
    # an example of a hand - Hand = ['Q hearts', 'K spades']
    c = 10
    # Hand()
    while c == 10:
        old = copy.copy(l_hand)
        for card in l_hand[0:len(l_hand) - 1]:
            a, b = ord(card[0]), ord(l_hand[l_hand.index(card) + 1][0])
            if a == 65:
                a = 83
            elif b == 65:
                b = 83
            if a == 49:
                a = 70
            elif b == 49:
                b = 70
            if a == 75:
                a = 82
            elif b == 75:
                b = 82
            if a < b:
                newordercard = l_hand[l_hand.index(card) + 1]
                l_hand[l_hand.index(card) + 1] = card
                l_hand[l_hand.index(card)] = newordercard
        if old == l_hand:
            c = 0
    return l_hand


def is_pair(l_hand):
    # the input is a list of a hand
    # the output if you have a pair or not
    # An example of an hand -l_hand = ['J spades', '9 diamonds', '10 spades', '10 diamonds', '9 spades']
    pairt = 0
    for card in hand_big_to_small(l_hand):
        pair = 0
        for i in range(0, len(l_hand)):
            if card[0:2] == l_hand[i][0:2]:  # Checks if first char of card is the same the first char of the other card
                pair += 1
        if pair >= 2:
            pairt = ['pair', card[0:2]]
            return pairt
        else:
            pairt = ['no pair']
    return pairt


def is_three_of_a_kind(l_hand):
    # the input is a list of a hand
    # the output if you have a three of a kind or not
    # An example of an hand - Hand=['9 diamonds','A spades','A diamonds','A clubs']
    for card in hand_big_to_small(l_hand):
        three = 0
        for i in range(0, len(l_hand)):  # Checks if first char of the card is same as the first char in the other cards
            if card[0:2] == l_hand[i][0:2]:
                three += 1
        if three >= 3:
            print ['three of a kind', card[0:2]]
        else:
            return ['no three of a kind']


def is_four_of_a_kind(l_hand):
    # the input is a list of a hand
    # the output if you have a four of a kind or not
    # An example of an hand - Hand=['9 diamonds','A spades','A diamonds','A clubs','A hearts']
    for card in hand_big_to_small(l_hand):
        four = 0
        for i in range(0, len(l_hand)):  # Checks if first char of the card is same as the first char in the other cards
            if card[0:2] == l_hand[i][0:2]:
                four += 1
        if four >= 4:
            print ['four of a kind', card[0:2]]


def is_flush(l_hand):
    # the input is a list of a hand
    # the output if you have a flush or not
    # An example of an hand -hand = ['9 diamonds', 'A diamonds', '8 diamonds', '10 diamonds', '2 diamonds', '5 spades']
    hand_big_to_small(l_hand)
    start = 2
    start2 = 2
    for card in l_hand:
        flush = 0
        for i in range(0, len(l_hand)):  # Checks if first char of the card is same as the first char in the other cards
            if card[0:2] == '10':
                start = 3
            elif l_hand[i][0:2] == '10':
                start2 = 3
            if card[start:len(card) + 1] == l_hand[i][start2:len(l_hand[i]) + 1]:
                flush += 1
                print flush
                start2 = 2
                start = 2
        if flush >= 5:
            print ['flush', l_hand[0][0:2]]


def is_straight(l_hand):
    # the input is a list of a hand
    # the output if you have a straight or not
    # An example of an hand - hand = ['A diamonds', 'Q diamonds', '7 diamonds', 'J diamonds', 'K diamonds', '10 spades']
    hand_big_to_small(l_hand)
    straight = 1
    for card in l_hand[0:len(l_hand) - 1]:  # Check if first char of card is bigger by one then first char of other card
        a, b = card[0], l_hand[l_hand.index(card) + 1][0]
        if a == 'A':
            a = 1
        elif b == 'A':
            b = 1
        if a == 'K':
            a = 13
        elif b == 'K':
            b = 13
        if a == 'Q':
            a = 12
        elif b == 'Q':
            b = 12
        if a == 'J':
            a = 11
        elif b == 'J':
            b = 11
        if a == '1':
            a = 10
        elif b == '1':
            b = 10
        a = int(a)
        b = int(b)
        if a == b + 1:
            straight += 1
            print straight
        elif a + 12 == b:
            straight += 1
        if straight >= 5:
            return ['straight', l_hand[0][0:2]]


def is_two_pair(l_hand):
    # the input is a list of a hand
    # the output if you have two pairs or not
    # An example of an hand - l_hand=['J spades', '9 diamonds', '10 spades', '10 diamonds', '9 spades']
    handcheck = copy.copy(l_hand)
    hand_big_to_small(l_hand)
    hand_big_to_small(handcheck)
    if_pair = is_pair(handcheck)
    if if_pair[0] == 'pair':
        pair1 = copy.copy(is_pair(handcheck)[1])
        for card in handcheck:
            if card[0] == is_pair(handcheck)[1][0]:
                handcheck.remove(handcheck[handcheck.index(card) + 1])
                handcheck.remove(card)
        if_pair2 = is_pair(handcheck)
        if if_pair2[0] == 'pair':
            pair2 = copy.copy(is_pair(handcheck)[1])
            if pair1 != pair2:
                twopairt = ['Two pair', str(pair1), str(pair2)]
                return twopairt


def full_house(l_hand):
    # the input is a list of a hand
    # the output if you have a full house or not
    # An example of an hand -hand=['k spades','Q diamonds','Q hearts','10 diamonds','Q spades','10 hearts']
    handcheck = copy.copy(l_hand)
    hand_big_to_small(l_hand)
    hand_big_to_small(handcheck)
    if is_two_pair(handcheck)[0] == 'Two pair':
        for card in handcheck:
            pair1f = is_two_pair(handcheck)[1]
            pair2f = is_two_pair(handcheck)[2]
            if card[0] == is_two_pair(handcheck)[1][0]:
                handcheck.remove(handcheck[handcheck.index(card) + 1])
                handcheck.remove(card)
            if card[0] == is_two_pair(handcheck)[2][0]:
                handcheck.remove(handcheck[handcheck.index(card) + 1])
                handcheck.remove(card)
        for card in handcheck:
            if card[0] == pair1f[0]:
                print ['full house', str(pair1f), str(pair2f)]
            if card[0] == pair2f[0]:
                print ['full house', str(pair2f), str(pair1f)]


is_two_pair(hand())


class Player:
    def __init__(self, money, my_hand, strongest_hand):
        self.money = money
        self.my_hand = my_hand
        self.strongest_hand = strongest_hand
        print self.my_hand, money

        # Player(100,Hand(),True)
        # An example of a class
        # Main script - P0ker GaM3
