from typing import ChainMap


wtable = []
copy = []
ch_seq = []


def setUp(data, num_st):
    global wtable, copy, ch_seq
    wtable = [[0]*num_st for i in range(num_st)]
    #copy = [[0]*num_st for i in range(num_st)]
    buildWalshTable(num_st, 0, num_st-1, 0, num_st-1, False)
    showWalshTable(num_st)
    copy = wtable.copy()
    for i in range(num_st):
        for j in range(num_st):
            wtable[i][j] *= data[i]
    for i in range(num_st):
        for j in range(num_st):
            ch_seq[i] += wtable[j][i]


def buildWalshTable(size, i1, i2, j1, j2, isBar):
    if size == 2:
        if not isBar:
            global wtable
            wtable[i1][j1] = 1
            wtable[i2][j2] = 1
            wtable[i2][j1] = 1
            wtable[i2][j2] = -1
        else:
            wtable[i1][j1] = -1
            wtable[i1][j2] = -1
            wtable[i2][j1] = -1
            wtable[i2][j2] = 1
        return 0
    midi = (i1+i2)/2
    midj = (j1+j2)/2

    buildWalshTable(size / 2, i1, midi, j1, midj, isBar)
    buildWalshTable(size / 2, i1, midi, midj + 1, j2, isBar)
    buildWalshTable(size / 2, midi + 1, i2, j1, midj, isBar)
    buildWalshTable(size / 2, midi + 1, i2, midj + 1, j2, not isBar)


def showWalshTable(num_st):
    global wtable
    for i in range(num_st):
        for j in range(num_st):
            print(wtable[i][j], " ", end="")
        print('\n')
    print('------------------------------')
    print('\n')
