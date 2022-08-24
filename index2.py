import pyautogui
import string
import random
from PIL import Image
import time
from pynput.mouse import Button, Controller
mouse = Controller()



itsTheFirst = True

import finderN
import finderT
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

flopN = [
    (543, 366),
    (583, 406),
    (650, 366),
    (690, 406),
    (757, 366),
    (797, 406),
    (864, 366),
    (904, 406),
    (971, 366),
    (1011, 406)
]
flopT = [
    (543, 406),
    (583, 446),
    (650, 406),
    (690, 446),
    (757, 406),
    (797, 446),
    (864, 406),
    (904, 446),
    (971, 406),
    (1011, 446)
]
myN = [
    (721, 669),
    (761, 709),
    (788, 664),
    (828, 704)
]
myT = [
    (721, 709),
    (761, 749),
    (788, 704),
    (828, 744)
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
def raise_up():
    mouse.position = (1334, 848)
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
        print('totalPot: ', totalPot)
        if redBut['text'] == 'Check':
            if cards_odds != 0:
                print('ltes maybe raise: ', cards_odds)
                if cards_odds > 40:
                    raise_up()
                else:
                    go_in()
            else: 
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
                print('pot odds: ', oddsPot)        #יחס קופה
                print('cards odds: ', cards_odds)   #יחס קלפים
                if cards_odds >= oddsPot:
                    if cards_odds - oddsPot > 30:
                        raise_up()
                    else:
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
        time.sleep(1)

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
        loop_num = loop_num + 1
        print('start Green ', loop_num)
        hand = []
        table = []
        time.sleep(1)
        game_level = 1
        print('move to 1')



    elif game_level == 1:   #Got 2 cards
        if first1:
            first1 = False
            for z in range(0, 4, 2):
                im1 = im.crop((myN[z][0], myN[z][1], myN[z+1][0], myN[z+1][1]))
                im2 = im.crop((myT[z][0], myT[z][1], myT[z+1][0], myT[z+1][1]))

                cardN = finderN.machine(im1)
                cardT = finderT.machine(im2)
                hand.append(cardN+cardT)
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
                im1 = im.crop((flopN[i][0], flopN[i][1], flopN[i+1][0], flopN[i+1][1]))
                im2 = im.crop((flopT[i][0], flopT[i][1], flopT[i+1][0], flopT[i+1][1]))
                table.append(finderN.machine(im1) + finderT.machine(im2))
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
            im1 = im.crop((flopN[6][0], flopN[6][1], flopN[6+1][0], flopN[6+1][1]))
            im2 = im.crop((flopT[6][0], flopT[6][1], flopT[6+1][0], flopT[6+1][1]))
            table.append(finderN.machine(im1) + finderT.machine(im2))
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
            im1 = im.crop((flopN[8][0], flopN[8][1], flopN[8+1][0], flopN[8+1][1]))
            im2 = im.crop((flopT[8][0], flopT[8][1], flopT[8+1][0], flopT[8+1][1]))
            table.append(finderN.machine(im1) + finderT.machine(im2))
            print(table)
            currentOdds = odds.calculate(table, hand)
        else:
            checkRed(im, currentOdds)
            #first4 = True
            #game_level = 0
            #print('move to 0')





    time.sleep(2)
