#!/usr/bin/env python3
"""Solution to Kiwi PyCon 2014 codewars problem 5

Eliot Blennerhassett
"""

print("Kiwi PyCon 2014 codewars problem 5 - RPS contest")
print("Extract contestant data by doing 'tar xf 5-rock-paper-scissors'")

class contestant(object):
    def __init__(self, index, data):
        data = [l.strip() for l in data]
        self.name = data[0].split('=')[1]
        self.move_idx = 0
        self.moves = data[1:]
        self.index = index

    def next_move(self):
        nm = self.moves[self.move_idx]
        self.move_idx += 1
        return nm

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

contestants = []
for ci in range(1,99):
    fn = 'contestants/contestant%02d' % ci
    try:
        with open(fn) as f:
            contestants.append(contestant(ci, f.readlines()))
    except FileNotFoundError:
        break



def play(c1, c2):
    m1 = c1.next_move()
    m2 = c2.next_move()
    print('1,2,3... %s x %s' % (m1, m2))

    if m1 == m2:
        winner = None
    elif ((m1=='rock') and (m2=='scissors') or
          (m1=='scissors') and (m2=='paper') or
          (m1=='paper') and (m2=='rock')):
        winner = c1
    else:
        winner = c2
        print('%s wins' % winner)

    return winner

def battle(c1, c2):
    print('%s against %s' % (c1, c2))

    for mi in range(1000):
        winner = play(c1, c2)
        if winner is not None:
            break

    return winner


for r in range(1, 100):
    print('************* Round %d ************' % r)
    winners = []
    for ci in range(0, len(contestants), 2):
        winners.append(battle(contestants[ci], contestants[ci + 1]))

    if len(contestants) == 2:
        break
    contestants = winners
    # print(contestants)

winner = winners[0]
for c in contestants:
    if c.name != winner.name:
        second = c

print('-------------------- The contest is over! -------------------')
print('Second is', second.name)
print('Winner is', winner.name)
secret = winner.name + second.name
print('********************\nSecret is', secret)
