material = [[0 for x in range(1000)] for y in range(1000)] # creating the 1000 x 1000 array that represents the area of the fabric
total_overlap = 0 # counter # of square inches of overlap

for line in open("area.txt"):
    overlap = False
    line = line.split() #split the line on whitespace. this creates 4 parts

    id = int(line[0][1:]) # get id, strip the '#' char and then convert to int
    col, row = line[2].split(',') # split the rows and cols on the ','
    # convert to ints
    col = int(col)
    row = int(row[:-1]) # remove the ':'
    # same deal here
    col_offset, row_offset = line[3].split('x')
    col_offset = int(col_offset)
    row_offset = int(row_offset)
    end_col = col + col_offset
    end_row = row + row_offset

    for r in range(row,end_row):
        for c in range(col, end_col):

            if material[r][c] == 0: # if the space has not been claimed place the id down
                material[r][c] = id

            else: # place X to represent overlap
                material[r][c] = 'X'



for line in open("area.txt"):
    overlap = False
    line = line.split() #split the line on whitespace. this creates 4 parts

    id = int(line[0][1:]) # get id, strip the '#' char and then convert to int
    col, row = line[2].split(',') # split the rows and cols on the ','
    # convert to ints
    col = int(col)
    row = int(row[:-1]) # remove the ':'
    # same deal here
    col_offset, row_offset = line[3].split('x')
    col_offset = int(col_offset)
    row_offset = int(row_offset)
    end_col = col + col_offset
    end_row = row + row_offset

    for r in range(row,end_row):
        for c in range(col, end_col):

            # if the space has not been claimed place the id down
            if material[r][c] == id:
                pass

            else:
                overlap = True

    if overlap == False:
        print(id)