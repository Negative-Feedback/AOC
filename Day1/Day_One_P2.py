total_drift = 0 # variable that holds the total
hist = [0] # initalize the list with 0 as the first element as we start at 0
repeat = True # set loop flag

while(repeat):
    for drift in open('fdrift.txt'):  # loops through each value in the file
        total_drift += int(drift)  # converts value to an integer, then adds that value to the total
        if total_drift in hist: # looks for the value of total_drift in our history list
            print(str(total_drift)) # if found print out the value
            repeat = False # set the flag to false
            break # break out of the for loop

        hist.append(total_drift) # if not found the value of total_drift is appended to the list

