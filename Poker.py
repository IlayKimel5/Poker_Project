import random
import copy
allcards=[]# a list of all the cards
typecard=['A','2','3','4','5','6','7','8','9','10','J','Q','K']# a list of the card types possible
suit=[' spades',' diamonds',' hearts',' clubs']# a list of the card suits possible
for typec in typecard: #creats the list allcards
    for suitcard in suit:
        lentypec=len(typec)
        typec+=suitcard
        allcards.append(typec)
        typec=typec[0:(lentypec)]
def cards():
    #the output is a list of a random card (card_type and suit)
    #the output is a list of all cards possible
    h=1
    typecard=0
    suit=0
    while h>0:
        typecard=random.choice(['A','2','3','4','5','6','7','8','9','10','J','Q','K']) #selects a random card type
        suit=random.choice([' spades',' diamonds',' hearts',' clubs']) #selects a random suit for the card
        typecard+=suit
        card=typecard
        for i in allcards:
            if i==card:
                allcards.remove(i)
                h=h-1
        if h>=1:
            card=0
    return card
def Hand():
    global hand
    hand=[]
    #the input is the function card()
    #the output is a list of two cards
    for i in range(5):
        hand.append(cards())
    return hand
def Hand_big_to_small(hand):
    #the input is a hand
    #the output is the hand from biggest to smallest
    # an example of a hand - Hand = ['Q hearts', 'K spades']
    c=10
    #Hand()
    while c==10:
        old=copy.copy(hand)
        for card in hand[0:len(hand)-1]:
            a,b= ord(card[0]),ord(hand[hand.index(card)+1][0])
            if a==65:
               a=83
            elif b==65:
                b=83
            if a==49:
                a=70
            elif b==49:
                b=70
            if  a==75:
                a=82
            elif b==75:
                b=82
            if a<b:
                newordercard=hand[hand.index(card)+1]
                hand[hand.index(card)+1] =card
                hand[hand.index(card)]=newordercard
        if old == hand:
            c=0
    return hand
def Is_pair(hand):
    #the input is a list of a hand
    #the output if you have a pair or not
    #An example of an hand - Hand=['9 diamonds','A spades','A diamonds']
    global pairT
    for card in Hand_big_to_small(hand):
        pair=0
        for i in range(0,len(hand)):
            if card[0:2]==hand[i][0:2]:#Checks if the first char of the card is the same as the first char in the other cards
                pair=pair+1
        if pair>=2:
            pairT=['pair',card[0:2]]
            return  pairT
def Is_three_of_a_kind(hand):
    #the input is a list of a hand
    #the output if you have a three of a kind or not
    #An example of an hand - Hand=['9 diamonds','A spades','A diamonds','A clubs']
    for card in Hand_big_to_small():
        three=0
        for i in range(0,len(hand)):#Checks if the first char of the card is the same as the first char in the other cards
            if card[0:2]==hand[i][0:2]:
                three=three+1
        if three>=3:
            print ['three of a kind',card[0:2]]
def Is_four_of_a_kind(hand):
    #the input is a list of a hand
    #the output if you have a four of a kind or not
    #An example of an hand - Hand=['9 diamonds','A spades','A diamonds','A clubs','A hearts']
    for card in Hand_big_to_small():
        four=0
        for i in range(0,len(hand)):#Checks if the first char of the card is the same as the first char in the other cards
            if card[0:2]==hand[i][0:2]:
                four=four+1
        if four>=4:
            print ['four of a kind',card[0:2]]
def Is_flush(hand):
    #the input is a list of a hand
    #the output if you have a flush or not
    #An example of an hand -
    hand=['9 diamonds','A diamonds','8 diamonds','10 diamonds','2 diamonds','5 spades']
    Hand_big_to_small(hand)
    start=2
    start2=2
    for card in hand:
        flush=0
        for i in range(0,len(hand)):#Checks if the first char of the card is the same as the first char in the other cards
            if card[0:2]=='10':
                start=3
            elif hand[i][0:2]=='10':
                start2=3
            if card[start:len(card)+1]==hand[i][start2:len(hand[i])+1]:
                flush=flush+1
                print flush
                start2=2
                start=2
        if flush>=5:
            print ['flush',hand[0][0:2]]
def Is_straight(hand):
    #the input is a list of a hand
    #the output if you have a straight or not
    #An example of an hand -
    hand=['A diamonds','Q diamonds','7 diamonds','J diamonds','K diamonds','10 spades']
    Hand_big_to_small(hand)
    straight=1
    for card in hand[0:len(hand)-1]:#Checks if the first char of the card is the bigger by one then the first char in the other cards
        a,b=card[0],hand[hand.index(card)+1][0]
        if a=='A':
            a=1
        elif b=='A':
            b=1
        if a=='K':
            a=13
        elif b=='K':
            b=13
        if a=='Q':
            a=12
        elif b=='Q':
            b=12
        if a=='J':
            a=11
        elif b=='J':
            b=11
        if a=='1':
            a=10
        elif b=='1':
            b=10
        a=int(a)
        b=int(b)
        if a==b+1:
            straight=straight+1
            print straight
        elif a+12==b:
            straight=straight+1
        if straight>=5:
            return ['straight',hand[0][0:2]]
def Is_two_pair(hand):
    #the input is a list of a hand
    #the output if you have two pairs or not
    #An example of an hand -hand=['J spades','9 diamonds','10 spades','10 diamonds','9 spades']
    global twopairT
    handcheck=copy.copy(hand)
    Hand_big_to_small(hand)
    Hand_big_to_small(handcheck)
    If_pair=Is_pair(handcheck)
    if If_pair[0]=='pair':
        pair1=copy.copy(pairT[1])
        for card in handcheck:
            if card[0]==pairT[1][0]:
                handcheck.remove(handcheck[handcheck.index(card)+1])
                handcheck.remove(card)
        If_pair2=Is_pair(handcheck)
        if If_pair[0]=='pair':
            pair2=copy.copy(pairT[1])
            if pair1!=pair2:
                twopairT=['Two pair',str(pair1),str(pair2)]
                return twopairT
def Full_house(hand):
    #the input is a list of a hand
    #the output if you have a full house or not
    #An example of an hand -hand=['k spades','Q diamonds','Q hearts','10 diamonds','Q spades','10 hearts']
    handcheck=copy.copy(hand)
    Hand_big_to_small(hand)
    Hand_big_to_small(handcheck)
    if Is_two_pair(handcheck)[0]=='Two pair':
        for card in handcheck:
            pair1f=twopairT[1]
            pair2f=twopairT[2]
            if card[0]==twopairT[1][0]:
                handcheck.remove(handcheck[handcheck.index(card)+1])
                handcheck.remove(card)
            if card[0]==twopairT[2][0]:
                handcheck.remove(handcheck[handcheck.index(card)+1])
                handcheck.remove(card)
        for card in handcheck:
            if card[0]==pair1f[0]:
                print ['full house',str(pair1f),str(pair2f)]
            if card[0]==pair2f[0]:
                print ['full house',str(pair2f),str(pair1f)]
Hand()
Is_two_pair(hand)
class Player:
    def __init__(self,Money,Hand,Strongest_hand):
        self.Money = Money
        self.Hand=Hand
        self.Strongest_hand=Strongest_hand
        print self.Hand,Money
#Player(100,Hand(),True)

#An example of a class





# Main script - P0ker GaM3


