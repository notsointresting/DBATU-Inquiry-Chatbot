import os
import random

for i in range(2):
    d = str(i) + 'days ago'
    rand = 27 # Generate a random day between 1 and 28
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system('git commit --date="2023-01-' + str(rand) + ' ' + d + '" -m "Commit message"')

os.system('git push -u origin main')
