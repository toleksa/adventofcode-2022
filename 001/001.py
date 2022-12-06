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
MAX=0
with open(FILE) as file:
    for LINE in file:
        LINE=LINE.rstrip()
        if LINE != "":
            SUM=SUM+int(LINE)
        else:
            if SUM > MAX:
                MAX = SUM
            SUM=0

print(MAX)

