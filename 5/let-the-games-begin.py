#!/usr/bin/env python3
"""Solution to Kiwi PyCon 2014 codewars problem 5

Eliot Blennerhassett
"""

print("Kiwi PyCon 2014 codewars problem 5 - RPS contest")
print("Extract contestant data by doing 'tar xf 5-rock-paper-scissors'")

cl = []  # contestant list
for ci in range(1,65):
    fn = 'contestants/contestant%02d' % ci
    with open(fn) as f:
        ll = [l.strip() for l in f.readlines()]
        ll[0] = ll[0].split('=')[1] # just name
        cl.append(ll)


# Assuming that the moves get used up, keep track of which move to use next
next_move = [1] * 64  # index 0 is contestant name


def battle(c1, c2):
    ml1 = cl[c1]
    ml2 = cl[c2]
    winner = None
    mi1 = next_move[c1]
    mi2 = next_move[c2]
    n1 = ml1[0]
    n2 = ml2[0]
    print('%s against %s' % (n1, n2))

    for mi in range(1000):
        m1 = ml1[mi1]
        m2 = ml2[mi2]
        mi1 += 1
        mi2 += 1
        print('Play <%s> <%s>' % (m1, m2))
        if m1 == m2:
            continue
        elif ((m1=='rock') and (m2=='scissors') or
              (m1=='scissors') and (m2=='paper') or
              (m1=='paper') and (m2=='rock')):
            winner = c1
            break
        else:
            winner = c2
            break

    next_move[c1] = mi1
    next_move[c2] = mi2

    print('%s wins' % cl[winner][0])
    return winner

contestants = range(0,64)

for round in range(1, 100):
    print('************* Round %d ************' % round)
    winners = []
    for ci in range(0, len(contestants), 2):
        winners.append(battle(contestants[ci], contestants[ci + 1]))

    if len(contestants) == 2:
        break
    contestants = winners


winner = winners[0]
winner_name = cl[winner][0]
print('Winner is', winner_name)
for c in contestants:
    if c != winner:
        second = c
        second_name = cl[second][0]
        print('Second is', second_name)

secret = winner_name + second_name
print('Secret is', secret)




