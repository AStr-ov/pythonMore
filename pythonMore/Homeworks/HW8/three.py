import csv
import os
from pathlib import Path

res = []
with open('newest_csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['Name', 'Type', 'Parent', 'Size'])
    w.writeheader()
    os.chdir('C://For Python')
    tot_size = 0
    for path, dir, files, in os.walk(os.getcwd()):
        parent = path.split('\\')
        parent = parent[-1]
        dir_size=0
        for directory in dir:
            if dir != []:
                d = {}
                l = []
                d['Name'] = directory
                d['Type'] = 'DIR'
                d['Parent'] = parent
                l.append(d)
                w.writerows(l)
            for fi in files:
                if files != []:
                    d1 = {}
                    l1 = []
                    d1['Name'] = fi
                    d1['Type'] = 'FILE'
                    d1['Parent'] = parent
                    fp = os.path.join(path, fi)
                    # file_size = os.path.getsize(f'{path}/{fi}')
                    file_size = os.path.getsize(fp)
                    dir_size +=file_size


                    #d['Size'] = file_size
                    #print(d)
                    d1['Size'] = f'{file_size} bytes'
                    l1.append(d1)
                    w.writerows(l1)
print(l1)
