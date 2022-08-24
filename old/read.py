import pyautogui
import string
import random
from PIL import Image
import time
from pynput.mouse import Button, Controller
mouse = Controller()

import finder

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


game_level = 0
first1 = True
first2 = True
first3 = True
first4 = True

while False:
    print('------')
    mouse.position = (100, 100)
    im = pyautogui.screenshot()
    pix = im.load()

    #if game_level == 0:     # GAME didnt start
    thePix = pix[1146, 808] #(48, 160, 56)
    if thePix[1] > 150 and  thePix[1] < 170:
        mouse.position = (1146, 808)
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print('start Green')
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
                name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                im1.save(r"myshot\{}00.png".format(name))
        else:
            thePix1 = pix[824, 394] #(238, 238, 238)
            if thePix1[0] > 225 and thePix1[1] > 225 and thePix1[2] > 225:
                first1 = True
                game_level = 2
                print('move to 2')

    elif game_level == 2:   #Flop
        if first2:
            first2 = False
            for i in range(0, 6, 2):
                print(i)
                left = flop[i][0]
                top = flop[i][1]
                right = flop[i+1][0]
                bottom = flop[i+1][1]

                im1 = im.crop((left, top, right, bottom))
                name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
                im1.save(r"shot\{}.png".format(name))
        else:
            thePix2 = pix[929, 394] #(238, 238, 238)
            if thePix2[0] > 225 and thePix2[1] > 225 and thePix2[2] > 225:
                first2 = True
                game_level = 3
                print('move to 3')

    elif game_level == 3:   #flop4
        if first3:
            print(6)
            first3 = False
            left = flop[6][0]
            top = flop[6][1]
            right = flop[6+1][0]
            bottom = flop[6+1][1]

            im1 = im.crop((left, top, right, bottom))
            name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            im1.save(r"shot\{}.png".format(name))

        else:
            thePix3 = pix[1029, 394] #(238, 238, 238)
            if thePix3[0] > 225 and thePix3[1] > 225 and thePix3[2] > 225:
                first3 = True
                game_level = 4
                print('move to 4')
    elif game_level == 4:
        if first4:
            print(8)
            first4 = False
            left = flop[8][0]
            top = flop[8][1]
            right = flop[8+1][0]
            bottom = flop[8+1][1]

            im1 = im.crop((left, top, right, bottom))
            name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            im1.save(r"shot\{}.png".format(name))

        else:
            first4 = True
            game_level = 0
            print('move to 0')



    thePix_red = pix[1057, 848] #(199, 69, 64)
                                #(164, 58, 57)
    if thePix_red[0] > 150 and thePix_red[0] < 210:
        mouse.position = (1057, 848)
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)

    time.sleep(2)
