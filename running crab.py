from os import getcwd , replace , makedirs
from time import sleep
from random import choice
cwd=getcwd()

paths=[]
while True:
    try:
        level=int(input("enter a number between 2 and 9"))
        if level>=2 and level<=9:
            break
        else:
            print('the number you entered out of range')
    except:
        print('please enter numeric value')
currentLevel=0
while currentLevel <=level:
    t = cwd
    foldern=0
    while foldern<=level:
        for i in range(level+1):
            t=t+f'\\{currentLevel}\\{foldern}\\{i}'
            paths.append(t)
            try:
                makedirs(t)
            except:
                pass
            t = cwd
        foldern=foldern+1
    currentLevel=currentLevel+1
chosen=choice(paths)
print('I will disappear in 2 second ha ha ha')
sleep(2)
try:
    replace(cwd+'\\running crab.exe',f'{chosen}\\running crab.exe')
except:
    pass
try:
    replace(cwd+'\\running crab.py',f'{chosen}\\running crab.py')
except:
    pass
