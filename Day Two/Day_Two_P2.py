#function to find the number of differences between equal length strings
def diff(str1, str2):
    #convert strings to lists so i can compare char by char
    str1 = list(str1)
    str2 = list(str2)

    size = len(str1) # get the length of list

    num_diffs = 0
    for i in range(0,size):
        if str1[i] != str2[i]:
            num_diffs += 1
    return (num_diffs)


#conver file to list of strings
box_list = []
file = open('box_list.txt', 'r')
for line in file:
    box_list.append(line)

# loop through the list and compare all of the strings
for i in range(0,len(box_list)):
   for j in range(i+1, len(box_list)-1):

       diffs = diff(box_list[i],box_list[j])

       # there sould only be one set of strings that differ by one
       # so I print that out and can remove the difference myself to get the answer
       if diffs == 1:
           print('str1: {}\nstr2: {}'.format(box_list[i], box_list[j]))