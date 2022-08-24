from PIL import Image
import string
import random

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

num = 0
for z in range(1):
    print(z)
    im = Image.open(r"pix\aaa7.png")

    for z in range(0, 4, 2):
        left = myN[z][0]
        top = myN[z][1]
        right = myN[z+1][0]
        bottom = myN[z+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im1.save(r"myshot\{}.png".format(name))

    for t in range(0, 4, 2):
        left = myT[t][0]
        top = myT[t][1]
        right = myT[t+1][0]
        bottom = myT[t+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im1.save(r"myshot\{}.png".format(name))




    for i in range(0, 10, 2):
        left = flopN[i][0]
        top = flopN[i][1]
        right = flopN[i+1][0]
        bottom = flopN[i+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for w in range(5))
        im1.save(r"myshot\{}.png".format(name))

    for w in range(0, 10, 2):
        left = flopT[w][0]
        top = flopT[w][1]
        right = flopT[w+1][0]
        bottom = flopT[w+1][1]
        im1 = im.crop((left, top, right, bottom))
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im1.save(r"myshot\{}.png".format(name))
