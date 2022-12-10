import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

file=sys.argv[1]

if not os.path.exists(file):
    print(f'ERR: file {file} not found')
    exit(2)

#############################

forrest = []

def check(forrest,x,y):
    #right
    right=True
    left=True
    top=True
    down=True
    #print(f"range:{x+1}-{len(forrest[y])}")
    for i in range(x+1,len(forrest[y])):
        #print(i)
        #print(f"{i}x{y} - {forrest[y][i]}")
        if forrest[y][i] >= forrest[y][x]:
            #print(f"{i}x{y}:{forrest[y][i]} - higher")
            right=False
    #print("left")
    #print(f"range:0-{x}")
    for i in range(0,x):
        #print(i)
        #print(f"{i}x{y} - {forrest[y][i]}")
        if forrest[y][i] >= forrest[y][x]:
            #print(f"{i}x{y}:{forrest[y][i]} - higher")
            left=False
    #print("top")
    #print(f"range:0-{y}")
    for i in range(0,y):
        #print(i)
        #print(f"{x}x{i} - {forrest[i][x]}")
        if forrest[i][x] >= forrest[y][x]:
            #print(f"{x}x{i}:{forrest[i][x]} - higher")
            top=False
    #print("down")
    #print(f"range:{y+1}-{len(forrest)}")
    for i in range(y+1,len(forrest)):
        #print(i)
        #print(f"{x}x{i} - {forrest[i][x]}")
        if forrest[i][x] >= forrest[y][x]:
            #print(f"{x}x{i}:{forrest[i][x]} - higher")
            down=False
    #print(right)
    #print(left)
    #print(top)
    #print(down)
    #print(right or left or top or down)
    return right or left or top or down
    #exit(0)

with open(file) as file:
    for line in file:
        line=line.rstrip()
        row=list(line)
        forrest.append(row)
        print(row)

size=2*(len(forrest)-1)+2*(len(forrest[0])-1)

counter=size
for y in range(1,len(forrest)-1):
    for x in range(1,len(forrest[1])-1):
        print(f"checking: {x}x{y} - {forrest[y][x]}")
        result=check(forrest,x,y)
        if result == True:
            counter+=1

print(counter)
