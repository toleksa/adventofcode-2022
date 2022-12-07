import sys
import os

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    exit(1)

FILE=sys.argv[1]

if not os.path.exists(FILE):
    print(f'ERR: file {FILE} not found')
    exit(2)

SUM=0
MAX=[0,0,0]
with open(FILE) as file:
    for LINE in file:
        LINE=LINE.rstrip()
        print(LINE)
        if LINE != "":
            SUM=SUM+int(LINE)
        else:
            print("sum: " + str(SUM))
            print(MAX)
            if SUM > MAX[0]:
                MAX[2]=MAX[1]
                MAX[1]=MAX[0]
                MAX[0]=SUM
                SUM=0
            elif SUM > MAX[1]:
                MAX[2]=MAX[1]
                MAX[1]=SUM
                SUM=0
            elif SUM > MAX[2]:
                MAX[2]=SUM
                SUM=0
            else:
                SUM=0
            print(MAX)
print(sum(MAX))

