polymer = []
not_done = True

for line in open('polymer.txt'):
    polymer = list(line)

while not_done:
    not_done = False
    for i in range(len(polymer)-1):
        if (((polymer[i].islower() and polymer[i+1].isupper()) or (polymer[i+1].islower() and polymer[i].isupper())) and polymer[i].lower() == polymer[i+1].lower()):
            not_done = True
            del polymer[i]
            del polymer[i]
            break
print(len(polymer))