import pyautogui
import string
import random
from PIL import Image
import time
from pynput.mouse import Button, Controller
mouse = Controller()

itsTheFirst = True

import finder
import odds
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


def checkRed(thePix_red, doIt):
    if doIt:
        itsTheFirst = False
    if thePix_red[0] > 150 and thePix_red[0] < 210:
        print('its red, neet to choose')
        if doIt:
            go_in()
        elif continue0:
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
    thePix_red = pix[1057, 848]


    #if game_level == 0:     # GAME didnt start
    if game_level == 0:
        checkRed(thePix_red, False)
    thePix = pix[1146, 808] #(48, 160, 56)
    if thePix[1] > 150 and  thePix[1] < 170:
        mouse.position = (1146, 808)
        time.sleep(1)
        first1 = True
        first2 = True
        first3 = True
        first4 = True
        continue0 = False
        itsTheFirst = True
        mouse.press(Button.left)
        mouse.release(Button.left)
        print('start Green')
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
                hand.append(card)###############
                """
                a = input('yes?')
                if a == '':
                    hand.append(card)
                else:
                    hand.append(a)
                    name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                    im1.save(r"myshot\{}.png".format(name))
                """
            print(hand)
            #ods = odds.calculateMonte(['?', '?', "?"], [hand])
        else:
            checkRed(thePix_red, itsTheFirst)
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
            ods = odds.calculateMonte(table, hand)
            if ods > 45:
                continue0 = True
                print('do it')
            else:
                continue0 = False
                print('no')
        else:
            checkRed(thePix_red, False)
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
            ods = odds.calculate(table, hand)
            if ods > 45:
                continue0 = True
                print('do it')
            else:
                continue0 = False
                print('no')
        else:
            checkRed(thePix_red, False)
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
            ods = odds.calculate(table, hand)
            if ods > 45:
                continue0 = True
                print('do it')
            else:
                continue0 = False
                print('no')
        else:
            checkRed(thePix_red, False)
            #first4 = True
            game_level = 0
            print('move to 0')





    time.sleep(2)
