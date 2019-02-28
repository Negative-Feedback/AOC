hist = [] #list to hold the chars we have counted already
two_char = 0 # number of ids that contain 2 of the same letter
three_char = 0 # number of ids that contain 3 of the same letter

for line in open("box_list.txt"): # loop through each line in the file

    # 2 bools to hold the stats of the count
    two = False
    three = False
    num_chars = 0

    for char in line: # loop through each char in the id string

        if len(hist) == 0 or char not in hist: # if the list is empty or its a new char
            hist.append(char) # add char to list
            num_chars = line.count(char) # count occurrences of the char

            if num_chars == 2:
                two = True

            elif num_chars == 3:
                three = True

    if two:
        two_char += 1

    if three:
        three_char += 1

    hist.clear() # clear list for new id

checksum = two_char * three_char

print("Two chars: {}\nThree chars: {}\nChecksum: {}".format(two_char, three_char, checksum))