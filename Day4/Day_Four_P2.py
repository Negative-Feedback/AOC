from datetime import datetime
import re
import sleep as sp

# 2d array to hold the lines from the file
arr = [[0 for x in range(2)] for y in range(1056)]
ids = [] # array to hold the ids

numbers = re.compile('\d+(?:\.\d+)?')# regex to strip the ids from the text

file = open('sorted_sleep.txt', 'r')

for i, line in enumerate(file):
    date = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
    string = line[20:]
    if re.search("^Guard #[0-9]{3,4} begins shift$", string):
        id = numbers.findall(string)
        id = int(id[-1])
        if id not in ids:
            ids.append(id)

    arr[i][0] = date
    arr[i][1] = string


file.close()

sp.part_two(arr, ids)