from tkinter.tix import TList


board  = {'tl' : ' ', 'tm' : ' ', 'tr' : ' ',
          'ml' : ' ', 'mm' : ' ', 'mr' : ' ',
          'bl' : ' ', 'bm' : ' ', 'br' : ' '}

def PrintLine():
    print("-+-+-")
def State():
    print('%s|%s|%s'%(board['tl'],board['tm'],board['tr']))
    PrintLine()
    print('%s|%s|%s'%(board['ml'],board['mm'],board['mr']))
    PrintLine()
    print('%s|%s|%s'%(board['bl'],board['bm'],board['br']))
def TestWin():
    if (board['tl'] == board['tm'] == board['tr'] and board['tr'] != ' '):
        print ('%s Wins' %board['tl'])
        return True
    elif (board['ml'] == board['mm'] == board['mr']and board['mr'] != ' '):
        print ('%s Wins' %board['mm'])
        return True
    elif (board['bl'] == board['bm'] == board['br']!=' ' and board['br'] != ' '):
        print ('%s Wins' %board['br'])
        return True
    elif (board['tl'] == board['ml'] == board['bl']!=' ') and board['bl']!=' ':
        print ('%s Wins' %board['ml'])
        return True
    elif (board['tm'] == board['mm'] == board['bm']!=' ') and board['bm']!=' ':
        print ('%s Wins' %board['mm'])
        return True
    elif (board['tr'] == board['mr'] == board['br']!=' ') and board['br']!=' ':
        print ('%s Wins' %board['mr'])
        return True
    elif (board['tl'] == board['mm'] == board['br']!=' ') and board['br']!=' ':
        print ('%s Wins' %board['mm'])
        return True
    elif (board['bl'] == board['mm'] == board['tr']!=' ') and board['tr']!=' ':
        print ('%s Wins' %board['mm'])
        return True
    return False
i = 0
turn = 'X'
while (not TestWin() and i <=8):
    State()
    print ("Place the piece: ")
    move = input()
    if (board[move] == ' '):
        board[move] = turn
        if (turn == 'X'):
            turn = 'O'
        else :
            turn = 'X'
    else:
        print("Nope.avi")
State()