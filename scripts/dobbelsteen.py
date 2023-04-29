import random
# print(dir(random))

lijst = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']


for i in range(1, 100):
    dobbelsteen = random.randrange(1, 6)

    print(f'{i}: {dobbelsteen}')
