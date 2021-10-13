def rules():
    print(
    '''
    RULES FOR TIC-TAC-TOE.
The game is played on a grid that's 3 squares by 3 squares.
one player will take X and other player should take O 
The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
then the game will be over.

the numpad is given below and you must press the number in which you want to fill your symbol

 ________ ________ ________
|        |        |        |         
|   1    |   2    |   3    |      
|        |        |        |         
|________|________|________|              
|        |        |        |    
|   4    |   5    |   6    |      
|        |        |        |          
|________|________|________|                 
|        |        |        |          
|   7    |   8    |   9    |         
|        |        |        |              
|________|________|________|                       
    
    ''')
    
def numpad():
    
    print('''
 ________ ________ ________
|        |        |        |         
|   1    |   2    |   3    |      
|        |        |        |         
|________|________|________|              
|        |        |        |    
|   4    |   5    |   6    |      
|        |        |        |          
|________|________|________|                 
|        |        |        |          
|   7    |   8    |   9    |         
|        |        |        |              
|________|________|________|                       
    

''')
    
def board(x):
    print('________ ________ _________')
    print('|       |        |        |')
    print('|   '+x[1] +'   |   '+x[2]+ '    |   '+x[3]+ '    |   ')
    print('|_______|________|________|')
    print('|       |        |        |')
    print('|   '+x[4] +'   |   '+x[5]+ '    |   '+x[6]+ '    |   ')
    print('|_______|________|________|')
    print('|       |        |        |')
    print('|   '+x[7] +'   |   '+x[8]+ '    |   '+x[9]+ '    |   ')
    print('|_______|________|________|')
    
    
#I wroe it like x in x[1] intead of equating the string bcoz i was having ' x' intead of 'x' ehich is not checking properly
# thats why i wrote istead of equating it
def check(x,p,q,r,s):
    if (('X' in x[1]) and ('X' in x[2]) and ('X' in x[3])) or (('X' in x[4]) and ('X' in x[5]) and ('X' in x[6])) or (('X' in x[7]) and ('X' in x[8]) and ('X' in x[9])) or (('X' in x[1]) and ('X' in x[4]) and ('X' in x[7])) or (('X' in x[2]) and ('X' in x[5]) and ('X' in x[8])) or (('X' in x[3]) and ('X' in x[6]) and ('X' in x[9])) or (('X' in x[1]) and ('X' in x[5]) and ('X' in x[9])) or (('X' in x[3]) and ('X' in x[5]) and ('X' in x[7])): 
        print(f'congratulations!!!, {p} {s} is winner')
        return True
        
    elif (('O' in x[1]) and ('O' in x[2]) and ('O' in x[3])) or (('O' in x[4]) and ('O' in x[5]) and ('O' in x[6])) or (('O' in x[7]) and ('O' in x[8]) and ('O' in x[9])) or (('O' in x[1]) and ('O' in x[4]) and ('O' in x[7])) or (('O' in x[2]) and ('O' in x[5]) and ('O' in x[8])) or (('O' in x[3]) and ('O' in x[6]) and ('O' in x[9])) or (('O' in x[1]) and ('O' in x[5]) and ('O' in x[9])) or (('O' in x[3]) and ('O' in x[5]) and ('O' in x[7])): 
        print(f'congratulations!!!, {q} {r} is winner')
        return False
    
    else:
        return None


from IPython.display import clear_output

def play3(a,p,q,r,s,f):
    
    c=int(input(f'{p}{s}, enter the number where you want to place your mark:'))
    if c not in f:
            a[c]="X"
    else:
            print(f'{p}{s},you must not enter the filled number')
            play3(a,p,q,r,s,f)
           
    clear_output()      
    numpad()
    board(a)
    check(a,p,q,r,s)
    
    f.append(c)
    return f

def play4(a,p,q,r,s,f):
    
    c=int(input(f'{q}{r}, enter the number where you want to place your mark:'))
    if c not in f:
            a[c]="O"
    else:
            print(f'{r}{q},you must not enter the filled number')
            play4(a,p,q,r,s,f)
           
    clear_output()      
    numpad()       
    board(a)
    check(a,p,q,r,s)
    
    f.append(c)
    return f
       
    
def game3():
    a=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
    
    
    rules()
    
    
    b=input('You are player one, will you take X or O: ')
    
    
    if b=='X':
        print('player 2 is O')
        r=''
        s=''
        
        p=input('enter player 1 name:')
        q=input('enter player 2 name:')
        
        f=[]
        
        while(check(a,p,q,r,s)!=True or False):
            
           
            if check(a,p,q,r,s)==True or False:
                break
            play3(a,p,q,r,s,f)
            
            
            if check(a,p,q,r,s)==True or False:
                break
            play4(a,p,q,r,s,f)
           
            
    elif b=='O':
        print('player 2 is X')
        p=''
        q=''
        
        r=input('enter player 1 name:')
        s=input('enter player 2 name:')
        
        f=[]
        
        while(check(a,p,q,r,s)!=True or False):
            
           
            if check(a,p,q,r,s)==True or False:
                break
            
            play4(a,p,q,r,s,f)
           
            if check(a,p,q,r,s)==True or False:
                break
            
            play3(a,p,q,r,s,f)
            
game3()            
           
           
           
            
           
        
