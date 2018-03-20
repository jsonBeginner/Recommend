import time
import os

os.chdir('F:/ADD/tianchi/data')

file = open('log_train_item.csv')
line = file.readline()
line = file.readline()
item_set = set()
while line:
    segs = line.split(',')
    item_set.add(segs[0])
    line = file.readline()
file.close()

file_read = open('log_train_user_all.csv')
file_write = open('log_train_user_o2o.csv', 'w')
line = file_read.readline()
file_write.write(line)
line = file_read.readline()
while line:
    segs = line.split(',')
    if segs[1] in item_set:
        file_write.write(line)
    line = file_read.readline()
file_read.close()
file_write.close()






