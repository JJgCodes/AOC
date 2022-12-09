import csv
import string

def getData():
    items = []
    with open('day3/input.txt') as fd:
        reader = csv.reader(fd)
        for row in reader: 
           if(row != []):
            items.append(row)
    return items


def prioritieItemSum(items):
    count = 0
    commonItem = ''
    
    for item in items:

        firstItems = item[0][:len(item[0]) // 2 ]
        secondItems = item[0][len(item[0]) //2:]
        
        for f in firstItems:
            if f in secondItems:
                commonItem = f
                break
        
        if(commonItem.isupper()):
            count += string.ascii_uppercase.index(commonItem)+27
        else: 
            count += string.ascii_lowercase.index(commonItem)+1
    return count


result = prioritieItemSum(getData())
print(result)