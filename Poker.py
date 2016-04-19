import random
import copy
from collections import namedtuple

possible_card_types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
possible_suits = ['spades', 'diamonds', 'hearts', 'clubs']
all_cards = [(type_c, suit_card) for type_c in possible_card_types for suit_card in possible_suits]


def cards():
    # the output is a list of a random card (card_type and suit)
    card = namedtuple('card', ['card_type', 'suit_type'])
    card_choice = random.choice(all_cards)
    card = card(card_choice[0], card_choice[1])
    all_cards.remove(card_choice)
    return card


def hand():
    # the input is the function card()
    # the output is a list of two cards
    l_hand = [cards() for i in range(5)]
    return l_hand


def hand_big_to_small(l_hand):
    # the input is a hand
    # the output is the hand from biggest to smallest
    while True:
        old_hand = copy.copy(l_hand)
        for card in l_hand[0:len(l_hand) - 1]:
            first_card_size, second_card_size = ord(card[0][0]), ord(l_hand[l_hand.index(card) + 1][0][0])
            if first_card_size == 65:
                first_card_size = 83
            elif second_card_size == 65:
                second_card_size = 83
            if first_card_size == 49:
                first_card_size = 70
            elif second_card_size == 49:
                second_card_size = 70
            if first_card_size == 75:
                first_card_size = 82
            elif second_card_size == 75:
                second_card_size = 82
            if first_card_size < second_card_size:
                new_order_card = l_hand[l_hand.index(card) + 1]
                l_hand[l_hand.index(card) + 1] = card
                l_hand[l_hand.index(card)] = new_order_card
        if old_hand == l_hand:
            break
    return l_hand


def is_pair(l_hand):
    # the input is a list of a hand
    # the output if you have a pair or not
    hand_big_to_small(l_hand)
    for card in l_hand:
        pair = 0
        for i in range(0, len(l_hand)):
            # if the suit_type of the card is the same as the suit_type of the other card
            if card.card_type == l_hand[i].card_type:
                pair += 1
        if pair >= 2:
            return ['pair', card.card_type]
    return ['no pair']


def is_three_of_a_kind(l_hand):
    # the input is a list of a hand
    # the output if you have a three of a kind or not
    hand_big_to_small(l_hand)
    for card in l_hand:
        three = 0
        # if the suit_type of the card is the same as the suit_type of the other card
        for i in range(0, len(l_hand)):
            if card.card_type == l_hand[i].card_type:
                three += 1
        if three >= 3:
            return ['three of a kind', card.card_type]
    return ['no three of a kind']


def is_four_of_a_kind(l_hand):
    # the input is a list of a hand
    # the output if you have a four of a kind or not
    hand_big_to_small(l_hand)
    for card in l_hand:
        four = 0
        # if the suit_type of the card is the same as the suit_type of the other card
        for i in range(0, len(l_hand)):
            if card.card_type == l_hand[i].card_type:
                four += 1
        if four >= 4:
            return ['four of a kind', card.card_type]
    return ['no four of a kind']


def is_flush(l_hand):
    # the input is a list of a hand
    # the output if you have a flush or not
    hand_big_to_small(l_hand)
    for card in l_hand:
        flush = 0
        for i in range(0, len(l_hand)):
            # Checks if the suit_type of the card is same as the suit_type of the other cards
            if card.suit_type == l_hand[i].suit_type:
                flush += 1
            if flush >= 5:
                for k in range(3):
                    if l_hand[k].suit_type == card.suit_type:
                        print ['flush', l_hand[k].card_type, l_hand[k].suit_type]
    return ['no flush']


def is_straight(l_hand):
    # the input is a list of a hand
    # the output if you have a straight or not
    backwards = 3
    hand_big_to_small(l_hand)
    straight = 1
    for card in l_hand[0:len(l_hand) - 1]:
        first_card_type, second_card_type = card.card_type, l_hand[l_hand.index(card) + 1].card_type
        if first_card_type == 'A':
            first_card_type = 14
        if second_card_type == 'A':
            second_card_type = 14
        if first_card_type == 'K':
            first_card_type = 13
        if second_card_type == 'K':
            second_card_type = 13
        if first_card_type == 'Q':
            first_card_type = 12
        if second_card_type == 'Q':
            second_card_type = 12
        if first_card_type == 'J':
            first_card_type = 11
        if second_card_type == 'J':
            second_card_type = 11
        first_card_type = int(first_card_type)
        second_card_type = int(second_card_type)
        # Check if the card_type of the card is bigger by one then the card_type of the other card
        if first_card_type == second_card_type + 1:
            straight += 1
            if second_card_type == 2:
                if l_hand[0].card_type == 'A':
                    straight += 1
        elif first_card_type == second_card_type:
            straight = straight
            backwards += 1
        else:
            straight = 1
        if straight >= 5:
            if second_card_type == 2:
                backwards -= 1
                high_card = l_hand[l_hand.index(card) - backwards].card_type
                return ['straight', high_card]
            else:
                high_card = l_hand[l_hand.index(card) - backwards].card_type
                return ['straight', high_card]
    return ['No straight']


def is_two_pair(l_hand):
    # the input is a list of a hand
    # the output if you have two pairs or not
    hand_copy = copy.copy(l_hand)
    hand_big_to_small(l_hand)
    hand_big_to_small(hand_copy)
    if_first_pair = is_pair(hand_copy)
    if if_first_pair[0] == 'pair':
        first_pair = copy.copy(is_pair(hand_copy)[1])
        for card in hand_copy:
            if card.card_type == is_pair(hand_copy)[1]:
                hand_copy.remove(hand_copy[hand_copy.index(card) + 1])
                hand_copy.remove(card)
                break
        if_second_pair = is_pair(hand_copy)
        if if_second_pair[0] == 'pair':
            second_pair = copy.copy(is_pair(hand_copy)[1])
            if first_pair != second_pair:
                return ['Two pair', str(first_pair), str(second_pair)]
    return ['No two pair', 'no', 'no']


def full_house(l_hand):
    # the input is a list of a hand
    # the output if you have a full house or not
    hand_copy_full_house = copy.copy(l_hand)
    hand_big_to_small(l_hand)
    hand_big_to_small(hand_copy_full_house)
    if is_three_of_a_kind(l_hand)[0] == 'three of a kind':
        full_house_three = is_three_of_a_kind(l_hand)[1]
        for card in l_hand:
            if is_three_of_a_kind(l_hand)[1] == card.card_type:
                hand_copy_full_house.remove(card)
        if is_pair(hand_copy_full_house)[0] == 'pair':
            full_house_pair = is_pair(hand_copy_full_house)[1]
            print ['full house', str(full_house_three), str(full_house_pair)]
    return ['no full house']


def straight_flush(l_hand):
    # the input is a list of a hand
    # the output if you have a straight-flush or not
    hand_big_to_small(l_hand)
    if is_flush(l_hand)[0] == 'flush' and is_straight(l_hand)[0] == 'straight':
        flush_color = [card for card in l_hand if card.suit_type == is_flush(l_hand)[2]]
        if is_straight(flush_color)[0] == 'straight':
            return ['straight-flush', is_straight(flush_color)[1]]
    return ['no straight-flush']


class Player:
    def __init__(self, money, my_hand, strongest_hand):
        self.money = money
        self.my_hand = my_hand
        self.strongest_hand = strongest_hand
        print self.my_hand, money

        # Player(100,Hand(),True)
        # An example of a class
        # Main script - P0ker GaM3

