from string import ascii_lowercase
polymer = []
best_len = 0


def getPolymerSize(polymer):
    not_done = True

    while not_done:
        not_done = False
        for i in range(len(polymer) - 1):
            if (((polymer[i].islower() and polymer[i + 1].isupper()) or (
                    polymer[i + 1].islower() and polymer[i].isupper())) and polymer[i].lower() == polymer[i + 1].lower()):
                not_done = True
                del polymer[i]
                del polymer[i]
                break
    return len(polymer)

file = open('polymer.txt', 'r')
line = file.readline()
file.close()

for c in ascii_lowercase:
    cur_size = 0
    polymer = [i for i in line if i.lower() != c]
    cur_len = getPolymerSize(polymer)

    if best_len == 0:
        best_len = cur_len

    elif best_len > cur_len:
        best_len = cur_len

    polymer.clear()

print(best_len)
