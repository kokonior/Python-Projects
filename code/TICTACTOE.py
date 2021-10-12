#make a tic tac toe Game


def printMat(mat):
    print('    '  + mat['1'] + ' || ' + mat['2'] + ' || ' + mat['3'] )
    print('----------------')
    print('    ' + mat['4'] + ' || ' + mat['5'] + ' || ' + mat['6'] )
    print('----------------')
    print('    ' + mat['7'] + ' || ' + mat['8'] + ' || ' + mat['9'] )
    print('----------------')

def draw(digit,mat, input_1):
    if (input_1 == 'X'):
        mat[str(digit)]  = 'X '
    else:
        mat[str(digit)] = 'O '
    printMat(mat)
def play(X,counter, mat, input_1):
    draw(X,mat, input_1)
    
  
    if (mat['1'] == mat['2'] == mat['3'] != '  '):
        print(mat['1'] + ' Wins!')
        return 0
    elif (mat['4'] == mat['5'] == mat['6'] != '  '):
        print(mat['4'] + ' Wins!')
        return 0
    elif (mat['7'] == mat['8'] == mat['9'] != '  '):
        print(mat['7'] + ' Wins!')
        return 0
    elif (mat['1'] == mat['5'] == mat['9'] != '  '):
        print(mat['1'] + ' Wins!')
        return 0
    elif (mat['3'] == mat['5'] == mat['7'] != '  '):
        print(mat['3'] + ' Wins!')
        return 0
    elif (mat['1'] == mat['4'] == mat['7'] != '  '):
        print(mat['1'] + ' Wins!')
        return 0
    elif (mat['2'] == mat['5'] == mat['8'] != '  '):
        print(mat['2'] + ' Wins!')
        return 0
    elif (mat['3'] == mat['6'] == mat['9'] != '  '):
        print(mat['6'] + ' Wins!')
        return 0
    elif(counter == 9):
        print('The game was a DRAW!')
        return 0
    
    else:
        return 1



playing = 1
while playing == 1:
    mat = {'1': '  ', '2': '  ', '3': '  ', '4' : '  ', '5': '  ', '6': '  ', '7':'  ', '8': '  ', '9': '  '}
    print('Welcome to the TIC TAC TOE v2.1')
    print('Here is the mat drawn numerically')
    printMat({'1': ' 1 ', '2': ' 2 ', '3': ' 3 ', '4' : '4  ', '5': ' 5 ', '6': ' 6 ', '7':' 7 ', '8': '8 ', '9': '9  '})

    print('Player 1 is X and Player 2 is O')
    print('Press ENTER key to continue')
    xtern = input()

    game = 1;
    counter  = 0;
    while game== 1:
        print('Enter the spot for player X (1-9)')
        X = int(input())
        data = 'X'
        counter += 1
        game =  play(X, counter,  mat, data)
        if game == 0:
            break
        print('Enter the spot for player O (1-9)')
        O = int(input())
        counter += 1
        data = 'O'
        game =  play(O, counter,  mat, data)



    print('Do you want to play again!')
    playing = int(input())

print('Thanks!')

            

   
















    
