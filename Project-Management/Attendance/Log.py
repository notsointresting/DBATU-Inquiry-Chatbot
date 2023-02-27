import os , random

for i in range(2):
    d = str(i) + 'days ago'
    rand = 27
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2023-'+str(rand)+'-'+d+'" -m 9')
os.system('git push -u origin main')