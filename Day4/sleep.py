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

        elif minutes[bMin] <= minutes[i]:
            bMin = i

    return bMin

# function to find the gaurd who is asleep the most and the minute they are asleep on the most
def part_one(arr, ids):
    bestID = -1
    bestMin = -1
    sleepTime = -1
    corrID = False
    for id in ids: # loop through the array of ids
        minutes = [0 for x in range(0, 60)] # gaurds are only asleep between 00:00 - 00:59 so this array represents the minutes

        # regex to identify the correct enteries
        query = re.compile("^Guard #" + str(id) + " begins shift$")
        for i in range(len(arr)): # loop through the array of entries
            if query.search(arr[i][1]):
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

        if bestID == -1 and bestMin == -1:
            sleepTime = testSleepTime
            bestID = id
            bestMin = calcSleepMin(minutes)

        elif sleepTime < testSleepTime:
            sleepTime = testSleepTime
            bestID = id
            bestMin = calcSleepMin(minutes)

    print("ID: {} Minute: {} Sleep Time: {}".format(bestID, bestMin, sleepTime))

# function to find the gaurd who is asleep the most and the minute they are asle
def part_two(arr, ids):
    bestID = -1
    bestMin = -1
    numTimes = -1
    corrID = False
    for id in ids: # loop through the array of ids
        minutes = [0 for x in range(0, 60)] # gaurds are only asleep between 00:

        # regex to identify the correct enteries
        query = re.compile("^Guard #" + str(id) + " begins shift$")
        for i in range(len(arr)): # loop through the array of entries
            if query.search(arr[i][1]):
                corrID = True

            elif re.search("falls asleep", arr[i][1]) and corrID:
                # stripping the mintues out of the entries
                start = int(str(arr[i][0])[14:16])
                end = int(str(arr[i+1][0])[14:16])
                for i in range(start,end+1): #increment the minutes they are asleep
                    minutes[i] +=1

            else:
                corrID = False

        BMin = calcSleepMin(minutes)
        NTime = minutes[BMin]

        if bestID == -1 and bestMin == -1 and numTimes == -1:
            bestID = id
            bestMin = BMin
            numTimes = NTime

        elif numTimes < NTime:
            bestID = id
            bestMin = BMin
            numTimes = NTime

    print("ID: {} Minute: {} Num Times: {}".format(bestID, bestMin, numTimes))