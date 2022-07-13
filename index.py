import pyautogui
import string
import random
from PIL import Image
import time
from pynput.mouse import Button, Controller
mouse = Controller()


mouse.position = (500, 100)
mouse.press(Button.left)
mouse.release(Button.left)


itsTheFirst = True

import finder
import odds
import get_text
flop = [
    (543, 366),
    (627, 450),
    (650, 366),
    (734, 450),
    (757, 366),
    (841, 450),
    (864, 366),
    (948, 450),
    (971, 366),
    (1055, 450)
]
my = [
    (721, 669),
    (778, 740),
    (788, 664),
    (845, 735)
]

def fold_check():
    mouse.position = (1057, 848)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
def go_in():
    mouse.position = (1169, 848)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)



game_level = 0
hand = []
table = []
first1 = True
first2 = True
first3 = True
first4 = True
lop2 = True
continue0 = True
loop_num = 0
currentOdds = 0


def checkRed(screen, cards_odds):
    pix = screen.load()
    thePix_red = pix[1057, 848]
    if thePix_red[0] > 150 and thePix_red[0] < 210:
        print('Red Button found')
        redBut = get_text.theReds(screen)

        totalPot = get_text.getPot(screen)
        if redBut['text'] == 'Check':
            go_in()
        elif redBut['text'] == 'Call':
            print(redBut)
            totalPot = totalPot + float(redBut['money'])
            oddsPot = (float(redBut['money']) / totalPot) * 100
            oddsPot = int(round(oddsPot , 2))
            if cards_odds == 0:
                if redBut['money'] <= 0.04:
                    go_in()
                else:
                    fold_check()
            else:
                print('pot odds: ', oddsPot)
                print('cards odds: ', cards_odds)
                if cards_odds >= oddsPot:
                    go_in()
                else:
                    fold_check()


while True:
    print('------')
    if lop2:
        lop2 = False
        mouse.position = (100, 100)
    else:
        lop2 = True

    im = pyautogui.screenshot()
    pix = im.load()

    thePix = pix[1146, 808] #(48, 160, 56)
    if thePix[1] > 150 and  thePix[1] < 170:
        mouse.position = (1146, 808)

        first1 = True
        first2 = True
        first3 = True
        first4 = True
        continue0 = False
        itsTheFirst = True
        currentOdds = 0
        mouse.press(Button.left)
        time.sleep(1)
        mouse.release(Button.left)
        print('start Green')
        loop_num = loop_num + 1
        print(loop_num)
        hand = []
        table = []
        time.sleep(1)
        game_level = 1
        print('move to 1')



    elif game_level == 1:   #Got 2 cards
        if first1:
            first1 = False
            for z in range(0, 4, 2):
                left = my[z][0]
                top = my[z][1]
                right = my[z+1][0]
                bottom = my[z+1][1]
                im1 = im.crop((left, top, right, bottom))

                card = finder.machine(im1)
                #print(card)
                hand.append(card)
            print(hand)
        else:
            checkRed(im, 0)
            thePix1 = pix[824, 394] #(238, 238, 238)
            if thePix1[0] > 225 and thePix1[1] > 225 and thePix1[2] > 225:
                first1 = True
                game_level = 2
                print('move to 2')
                continue0 = True


    elif game_level == 2:   #Flop
        if first2:
            first2 = False
            for i in range(0, 6, 2):
                left = flop[i][0]
                top = flop[i][1]
                right = flop[i+1][0]
                bottom = flop[i+1][1]
                im1 = im.crop((left, top, right, bottom))
                table.append(finder.machine(im1))

                name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                im1.save(r"shot\{}.png".format(name))
            print(table)
            #odds.calculate(table, hand)
            currentOdds = odds.calculateMonte(table, hand)
        else:
            checkRed(im, currentOdds)
            thePix2 = pix[929, 394] #(238, 238, 238)
            if thePix2[0] > 225 and thePix2[1] > 225 and thePix2[2] > 225:
                #first2 = True
                game_level = 3
                print('move to 3')

    elif game_level == 3:   #flop4
        if first3:
            first3 = False
            left = flop[6][0]
            top = flop[6][1]
            right = flop[6+1][0]
            bottom = flop[6+1][1]
            im1 = im.crop((left, top, right, bottom))
            table.append(finder.machine(im1))

            name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            im1.save(r"shot\{}.png".format(name))
            print(table)
            currentOdds = odds.calculate(table, hand)
        else:
            checkRed(im, currentOdds)
            thePix3 = pix[1029, 394] #(238, 238, 238)
            if thePix3[0] > 225 and thePix3[1] > 225 and thePix3[2] > 225:
                #first3 = True
                game_level = 4
                print('move to 4')
    elif game_level == 4:
        if first4:
            first4 = False
            left = flop[8][0]
            top = flop[8][1]
            right = flop[8+1][0]
            bottom = flop[8+1][1]

            im1 = im.crop((left, top, right, bottom))
            table.append(finder.machine(im1))

            name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            im1.save(r"shot\{}.png".format(name))
            print(table)
            currentOdds = odds.calculate(table, hand)
        else:
            checkRed(im, currentOdds)
            #first4 = True
            #game_level = 0
            #print('move to 0')





    time.sleep(2)
