
### Understanding where we are on our machine
import os, sys  

path, dirs, files = next(os.walk("./"))   # 'This Folder'
file_count = len(files)

### Reading input

Data_store = [[],[]]

with open('Data.txt') as f:      ### You may need to change this file name!!!
    lines = f.readlines()
    for j in range(0, len(lines)):
        k = lines[j].split(' ')    ### Parsing line after line based on a 'space'
        if j > 0:                               ### You may also need to change this line!!!
            Data_store[0].append(float(k[0]))
            Data_store[1].append(float(k[1]))
    f.close()

print(Data_store)
### I did some math, and now I want to save the data

### Writing Output

kk = open('Output.txt','w')
kk.write('Output Data \n')
for i in range(0, len(Data_store[0])):
    kk.write(str(Data_store[0][i])+' '+str(Data_store[1][i])+' \n')
    
kk.close()



    
