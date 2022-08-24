import holdem_calc
import random

#print(holdem_calc.calculate(["As", "Ks", "5d", "5s", "4s"], False, 1, None, ["5h", "5c", "2s", "6d"], False))
#print('teko', 'me', 'him')
nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
colors = ['d', 'h', 'c', 's']
all_cards = []

for x in nums:
    for y in colors:
        all_cards.append('{}{}'.format(x, y))


def calculate(table, hand):
    try:
        the_hands = []
        the_hands.extend(hand)
        the_hands.extend(['?', '?'])
        res = holdem_calc.calculate(table, False, 1, None, the_hands, False)
        ret = int(round(res[0] + res[1] , 2) * 100) - 30
        #print(ret)
        return ret
    except Exception as e:
        print('odds.py 30')
        return -20

def getMixList(cards):
    mix_list = []
    for x in cards:
        for y in cards:
            if x != y:
                mix_list.append([x, y])

    random.shuffle(mix_list)
    return mix_list


def calculateMonte(table, hand):
    try:
        know_cards = []
        know_cards.extend(table)
        know_cards.extend(hand)
        newlist = list(filter(lambda x: x not in know_cards, all_cards))

        cards_imp = getMixList(newlist)
        averge = 0
        monte = 250
        for x in range(monte):
            the_hands = []
            the_hands.extend(hand)
            the_hands.extend(cards_imp[x])
            res = holdem_calc.calculate(table, False, 1, None, the_hands, False)
            averge += res[0] + res[1]
        ret = int(round(averge/monte*100, 2) - 30)
        #print(ret)
        return ret
    except Exception as e:
        print('odds.py 60')
        print(e)
        return -20

#calculate(['9s', '2s', 'Qc'], ['Js', '7d'])
