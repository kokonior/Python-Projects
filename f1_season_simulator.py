import random
import itertools
from sys import maxsize
from itertools import permutations
import matplotlib.pyplot as plt




ds = {44:['HAM',0,'United Kingdom','MERCEDES','LEWIS HAMILTON'],77:['BOT',0,'Finland','MERCEDES','VALTTERI BOTTAS'],
          33:['VER',0,'Netherlands','RED BULL RACING-HONDA','MAX VERSTAPPEN'],11:['PER',0,'Mexico','RED BULL RACING-HONDA','SERGIO PEREZ'],
          16:['LEC',0,'Monaco','SCUDERIA FERRARI','CHARLES LECLERC'],55:['SAI',0,'Spain','SCUDERIA FERRARI','CARLOS SAINZ'],
          4:['NOR',0,'United Kingdom','McLAREN-MERCEDES', 'LANDO NORRIS'],3:['RIC',0,'Australia','McLAREN-MERCEDES','DANIEL RICCIARDO'],
          10:['GAS',0,'France','ALPHA TAURI-HONDA','PIERRE GASLY'],22:['TSU',0,'Japan','ALPHA TAURI-HONDA','YUKI TSUNODA'],
          5:['VET',0,'Germany','ASTON MARTIN-MERCEDES','SEBASTIAN VETTEL'],18:['STR',0,'Canada','ASTON MARTIN-MERCEDES','LANCE STROLL'],
          14:['ALO',0,'Spain','ALPINE-RENAULT','FERNANDO ALONSO'],31:['OCO',0,'France','ALPINE-RENAULT','ESTEBAN OCON'],
          7:['RAI',0,'Finland','ALFA ROMEO','KIMI RAIKKONEN'],99:['GIO',0,'Italy','ALFA ROMEO','ANTONIO GIOVANNAZI'],
          47:['SCH',0,'Germany','HAAS-FERRARI','MICK SCHUMACHER'],9:['MAZ',0,'Russia','HAAS-FERRARI','NIKITA MAZEPIN'],
          63:['RUS',0,'United Kingdom','WILLIAMS RACING','GEORGE RUSSEL'],6:['LAT',0,'Canada','WILLIAMS RACING','NICHOLAS LATIFI']
}


point_sys=[25,18,15,12,10,8,6,4,2,1,0,0,0,0,0,0,0,0,0,0]


point_trajectory={44:[], 77:[], 33:[], 11:[], 16:[], 55:[], 4:[], 3:[], 10:[], 22:[], 5:[], 18:[], 14:[], 31:[],
                    7:[], 99:[], 47:[], 9:[], 63:[], 6:[]}


places = {0: 'Australian GP', 1: 'GP of China', 2: 'Canadian GP', 3: 'Turkish GP',
              4: 'South African GP', 5: 'British GP', 6: 'GP of Bahrain', 7: 'Italian GP',
              8: 'Egyptian GP', 9: 'Indian GP'}


dates = ['Mar 25', 'Apr 12', 'May 6', 'May 22', 'June 2',
             'July 10', 'Sept 15', 'Oct 20', 'Nov 14', 'Nov 28']


graph = [[0, 8, 999, 999, 999, 18, 10, 999, 999, 999],
             [8, 0, 20, 999, 999, 999, 9, 999, 999, 999],
             [999, 20, 0, 15, 999, 999, 16, 999, 999, 999],
             [999, 999, 15, 0, 11, 999, 999, 999, 3, 999],
             [999, 999, 999, 11, 0, 22, 999, 999, 999, 8],
             [18, 999, 999, 999, 22, 0, 999, 4, 999, 999],
             [10, 9, 16, 999, 999, 999, 0, 10, 999, 999],
             [999, 999, 999, 999, 999, 4, 10, 0, 6, 999],
             [999, 999, 999, 3, 999, 999, 999, 6, 0, 7],
             [999, 999, 999, 999, 8, 999, 999, 999, 7, 0]]



# generate Calendar using TSP
def calendar(graph, V, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    pos = []
    l = []
    a = -1
    for i in next_permutation:
        l1 = []
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            l1.append(j)
            k = j
        current_pathweight += graph[k][s]
        l1.insert(0, s)
        l.append(l1)
        change = min_path
        min_path = min(min_path, current_pathweight)
        if min_path < change:
            pos.append(a + 1)
        else:
            a += 1
    p = pos[-1]
    place_path = l[p]
    print()
    for i in range(len(dates)):
        print(places[place_path[i]], end='')
        print(" " * ((16 - len(places[place_path[i]])) + 4), end='')
        print(dates[i])
    return place_path


#descending order of driver's points
def driver_tally():
    listofTuples = sorted(ds.items(),  key=lambda x: x[1][1], reverse=True)
    for i, elem in enumerate(listofTuples):
        print(f'P{i+1}'+(' ' * (3-len(str(i+1))))+ f' :: #{elem[0]}'+ (' ' * (3-len(str(elem[0]))))+ f' :: {elem[1][4]}'+(' ' * (20-len(elem[1][4])))+ f' :: {elem[1][1]}'+(' ' * (3-len(str(elem[1][1]))))+' Points')


#Driver standing
def driver_standing(driver_num):
    listofTuples = sorted(ds.items() ,  key=lambda x: x[1][1], reverse=True)
    for i,elem in enumerate(listofTuples) :
        if driver_num == elem[0]:
            return i+1


#descending order of constructor's points
def cons_tally():
    res = {}
    for i, v in ds.items():
        car = v[3]
        if car not in res.keys():
            res[car] = v[1]
        else:
            res[car] += v[1]
    listofTuples = sorted(res.items() ,  key=lambda x: x[1], reverse=True)
    for i,elem in enumerate(listofTuples) :
        print(f'P{i+1}'+(' ' * (3-len(str(i+1))))+ f' :: {elem[0]}'+ (' ' * (23-len(elem[0])))+ f' :: {elem[1]}'+(' ' * (3-len(str(elem[1]))))+' Points')


#randomize results
def results():
    a = list(ds.keys())
    random.shuffle(a)
    return a


#binary search for Driver
def find():
    target = input('\nEnter the abbreviated name of driver     (all CAPS) :   ')
    ls=[[ds[i][0],i] for i in ds]
    ls=sorted(ls, key=lambda x: x[0])

    start = 0
    end = len(ls) - 1

    while start <= end:
        middle = (start + end)// 2
        midpoint = ls[middle]
        if midpoint[0] > target:
            end = middle - 1
        elif midpoint[0] < target:
            start = middle + 1
        else:
            return midpoint[1]


#Statistical comparison between two drivers
def stat_plot():
    print('To compare the progression of any two drivers, enter their names')
    target1 = find()
    target2 = find()
    if target1 is None or target2 is None:
        print("\nPlease enter the names correctly")
        return
    plt.plot(point_trajectory[target1], marker='o', label=ds[target1][0])
    plt.plot(point_trajectory[target2], marker='o', label=ds[target2][0])
    plt.xlabel("RACES", fontsize = 15)
    plt.ylabel("POINTS",fontsize = 15)
    plt.legend()
    plt.show()


#allocate points based on results
def points_alloc(a):
    for key in ds:
        if key in a:
            ds[key][1] += point_sys[a.index(key)]
            point_trajectory[key].append(ds[key][1])


def champions():
    points = []
    for key in ds:
        points.append(ds[key][1])
    points.sort(reverse = True)
    for key in ds:
        if points[0] == ds[key][1]:
            print(f'NEWS FLASH: {ds[key][4]} is World Champion!')
            break



print('Choose the location for the first race from the following:')
print("\n--------------------------------------------------------------------------------------------\n")

for i in range(10):
    print(str(i) + ' for ' + places[i])

print("\n--------------------------------------------------------------------------------------------\n")

so = int(input("Enter your choice   :   "))
tot_race = 10
print('Here is the order in which the races are to be conducted')
sequence = calendar(graph, tot_race, so)
input("\nPRESS ENTER TO CONTINUE")

print("\n--------------------------------------------------------------------------------------------\n")

sim = False

for i in range(len(sequence)):
    
    
    if sim is False:
        print(f'\nWelcome to the {places[sequence[i]]}! \n\nThis is ROUND {i+1} of the 2021 F1 Season!')
        c = input('Enter [Y/y] to sim to the end of season  :   ')
        if c == 'y' or c == 'Y':
            sim = True
    res = results()
    points_alloc(res)

    while not sim:
        print("\n--------------------------------------------------------------------------------------------\n")
        print("ENTER 1 TO VIEW THE RACE RESULTS")
        print("ENTER 2 TO VIEW THE DRIVERS' STANDINGS")
        print("ENTER 3 TO VIEW THE CONSTRUCTORS' STANDINGS")
        print("ENTER 4 TO CHECK DRIVER'S BIO")
        print("ENTER 5 TO COMPARE THE RESULTS OF ANY 2 DRIVERS")

        if i+1 < tot_race:
            print("ENTER 6 TO ADVANCE TO THE NEXT ROUND")
        else: 
            print("ENTER 6 TO END SEASON\n\n")

        ch = int(input("\nEnter choice    :   "))
        print("\n--------------------------------------------------------------------------------------------\n")
        
        if ch == 1:
            for j, elem in enumerate(res):
                print(f'P{j+1}'+ (' ' * (3-len(str(j+1))))+' :: ' + ds[elem][0])
        
        if ch == 2:
            driver_tally()
            
        if ch == 3:
            cons_tally()
       
        if ch == 4:
            driver = find()
            if driver is None:
                print("\nDriver not found. Please check your spelling and try again" )
                continue
            else:
                print("NUMBER           :       ", str(driver))
                print("NAME             :       ", ds[driver][4])
                print("CONSTRUCTOR      :       ", ds[driver][3])
                print("COUNTRY          :       ", ds[driver][2])
                print("POINTS           :       ", ds[driver][1])
                print("POSITION         :       ", str(driver_standing(driver)))
        
        if ch == 5:
            stat_plot()
            continue

        if ch not in [1, 2, 3, 4, 5]:
            break

champions()

while True:
    print("\nENTER 1 TO VIEW THE FINAL DRIVERS' STANDINGS")
    print("ENTER 2 TO VIEW THE FINAL CONSTRUCTORS' STANDINGS")
    print("ENTER 3 TO CHECK DRIVER'S BIO")
    print("ENTER 4 TO COMPARE THE RESULTS OF ANY 2 DRIVERS")
    print("ENTER 5 TO QUIT\n")    
    ch = int(input("Enter choice: "))
        
    if ch == 1:
        driver_tally()

    if ch == 2:
        cons_tally()

    if ch == 3:
        driver = find()
        if driver is None:
            print("\nDriver not found. Please check your spelling and try again" )
            continue
        else:
            print("NUMBER           :       ", str(driver))
            print("NAME             :       ", ds[driver][4])
            print("CONSTRUCTOR      :       ", ds[driver][3])
            print("COUNTRY          :       ", ds[driver][2])
            print("POINTS           :       ", ds[driver][1])
            print("POSITION         :       ", str(driver_standing(driver)))
    
    if ch == 4:
        stat_plot()

    if ch not in [1, 2, 3, 4]:
        print('THANKS FOR PLAYING!\n')
        break

