from PIL import Image
import string
import random

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

num = 0
for z in range(12):
    print(z)
    im = Image.open(r"pix\aaa{}.png".format(z))

    for z in range(0, 4, 2):
        left = my[z][0]
        top = my[z][1]
        right = my[z+1][0]
        bottom = my[z+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im1.save(r"myshot\{}.png".format(name))


    for i in range(0, 10, 2):
        left = flop[i][0]
        top = flop[i][1]
        right = flop[i+1][0]
        bottom = flop[i+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im1.save(r"myshot\{}.png".format(name))
