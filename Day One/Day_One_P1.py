total_drift = 0 # variable that holds the total

for drift in open('fdrift.txt'): # loops through each value in the file
    total_drift += int(drift) # converts value to an integer, then adds that value to the total

print("The total drift is: " + str(total_drift)) # prints the total