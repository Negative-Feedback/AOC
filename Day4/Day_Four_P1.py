from datetime import datetime
import re

# function to calculate the total time spent asleep
def calcSleepTime(minutes):
    total = 0
    for x in minutes:
        total += x

    return total

# function to calculate the minute they were asleep on the most
def calcSleepMin(minutes):
    bMin = -1
    for i in range(len(minutes)):
        if bMin == -1:
            bMin = i

        elif minutes[bMin] < minutes[i]:
            bMin = i

    return bMin

# function to find the gaurd who is asleep the most and the minute they are asleep on the most
def bestMinute(arr, ids):
    bestID = 0
    bestMin = 0
    sleepTime = 0
    corrID = False
    for id in ids: # loop through the array of ids
        minutes = [0 for x in range(0, 60)] # gaurds are only asleep between 00:00 - 00:59 so this array represents the minutes

        # regex to identify the correct enteries
        query = "^Guard #" + str(id) + " begins shift$"
        for i in range(1056): # loop through the array of entries
            if re.search(query, arr[i][1]):
                corrID = True

            elif re.search("falls asleep", arr[i][1]) and corrID:
                # stripping the mintues out of the entries
                start = int(str(arr[i][0])[14:16])
                end = int(str(arr[i+1][0])[14:16])
                for i in range(start,end): #increment the minutes they are asleep
                    minutes[i] +=1
            else:
                corrID = False

        testSleepTime = calcSleepTime(minutes) # calculate the total time spent asleep

        if bestID == 0 and bestMin == 0:
            sleepTime = testSleepTime
            bestID = id
            bestMin = calcSleepMin(minutes)

        else:
            if sleepTime < testSleepTime:
                sleepTime = testSleepTime
                bestID = id
                bestMin = calcSleepMin(minutes)

    print("ID: {} Minute: {} Sleep Time: {}".format(bestID, bestMin, sleepTime))


# 2d array to hold the lines from the file
arr = [[0 for x in range(2)] for y in range(1056)]
ids = [] # array to hold the ids

numbers = re.compile('\d+(?:\.\d+)?')# regex to strip the ids from the text

file = open('sleep.txt', 'r')

for i, line in enumerate(file):
    date = line[1:17]
    date = date.replace('-', ' ')
    string = line[19:]
    if re.search("^Guard #[0-9]{3,4} begins shift$", string):
        id = numbers.findall(string)
        id = int(id[-1])
        if id not in ids:
            ids.append(id)

    date = datetime.strptime(date, '%Y %m %d %H:%M')
    arr[i][0] = date
    arr[i][1] = string


file.close()

arr = sorted(arr, key=lambda dates: dates[0])
bestMinute(arr, ids)


# this was to convert the sorted array to a file
# i did this because i had a feeling that the sorted list
# would come in handy for the second part
'''file = open("sorted_sleep.txt", "w+")
for i in range(1056):
    line = str(arr[i][0]) + ' ' + arr[i][1]
    file.write(line)
file.close()'''
