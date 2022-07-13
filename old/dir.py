#import os


parent_dir = "C:/Users/eliran/Desktop/poker god/cards/"



nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
colors = ['d', 'h', 'c', 's']
all_cards = []

for x in nums:
    for y in colors:
        all_cards.append('{}{}'.format(x, y))

for i in all_cards:
    #path = os.path.join(parent_dir, i)
    #os.mkdir(path)
