"""
Code for selecting spells from a deck of "cards"
The goal is to have Tural's known spells be represented by a deck of cards.
A spell can be cast from a card if Tural has an appropriate spell slot.
Spells are cast as an action, bonus action or reaction depending on the spell.

What if he doesn't have the spell slot?
Nothing.

Tural can use any card to cast a cantrip.


"""

from numpy import random

class spell(object):
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def desc(self):
        print('{:s} ({:d})'.format(self.name,self.level))


HAND = 4


spells = []
with open('spells.txt') as file:
    for i,line in enumerate(file):
        if i == 0:
            continue
        formatted_line = line.strip('\n').rsplit('\t')
        name, level = formatted_line[0],formatted_line[1]
        spells.append(spell(name,int(level)))


while True:
    random.shuffle(spells)

    for s in range(HAND):
        spells[s].desc()

    x = input()
    if x == 'q':
        break
    




