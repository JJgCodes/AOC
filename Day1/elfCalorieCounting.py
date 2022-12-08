current = 0
prev = 0
top3 = [0,0,0]
count = 0

import csv
with open('day1/input.txt') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        if row != []:
            current += int(row[0])
        else:
            if current > min(top3):
                pos = top3.index(min(top3))
                top3[pos] = current 
            if current > prev:
                prev = current
            current = 0
            
            
answer = sum(top3)
    
    
print(answer)
    

    