import random
import time

pot = [n for n in range(1, 46)]

jackpot = []

for n in range(1,7):
    random.shuffle(pot)
    pick = pot.pop()

    jackpot.append(pick)
    time.sleep(1)


jackpot.sort()
print(jackpot)



