import os
import random

for i in range(10):
    d = 'just checking that is everything is fine or not'
    rand = i + 1 # Generate a random day between 1 and 28
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system('git commit --date="2024-01-' + str(rand) + ' ' + d + '" -m "Commit message"')

os.system('git push -u origin main')
