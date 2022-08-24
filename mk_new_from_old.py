from PIL import Image
import string
import random

import os

arr = os.listdir('C:\\Users\eliran\Desktop\projects 2022\poker god2\shot')
print(arr)

bottom = [
    (721, 709),
    (761, 749),
    (788, 704),
    (828, 744)
]


for z in arr:
    im = Image.open(r"shot\{}".format(z))

    im1 = im.crop((0, 0, 40, 40))
    name = ''.join(random.choice(string.ascii_lowercase) for w in range(5))
    im1.save(r"myshot2\top\{}.png".format(name))

    im2 = im.crop((0, 40, 40, 80))
    name2 = ''.join(random.choice(string.ascii_lowercase) for w in range(5))
    im2.save(r"myshot2\bottom\{}.png".format(name))




