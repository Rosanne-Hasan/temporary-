
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import re 
import glob


########
#1 fork
f4 = [] 
x = [1,2,4, 8] 
for i in x:
    path = "./stdc_1f{}t/*.out".format(i)
    sum = 0 
    events = []
    times = []
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f:
                if re.search("accepted", line):
                    event = re.findall(r'[\d]+', line)
                    e = float(event[0])
                    events.append(e)
                if re.search(r"\bprocess\b", line):
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
    maxt = max(times)
    index = times.index(maxt) 
    e = events[index]
    total = e * maxt *1e-3  
    print('1 fork',i,'threds',times, events, maxt, index, e, total )
    f4.append(100/total) 
y = [1,2,4,8]
plt.plot(y, f4, '--b*', label = 'Increasing threads (1 fork) ') 


########
#2 forks 
f4 = [] 
x = [1,2,4] 
for i in x:
    path = "./stdc_2f{}t/*.out".format(i)
    sum = 0 
    events = []
    times = []
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f:
                if re.search("accepted", line):
                    event = re.findall(r'[\d]+', line)
                    e = float(event[0])
                    events.append(e)
                if re.search(r"\bprocess\b", line):
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
    maxt = max(times)
    index = times.index(maxt) 
    e = events[index]
    total = e * maxt *1e-3  
    print('2 forks', i, 'threads', times, events, maxt, index, e, total )
    f4.append(100/total) 
y = [2,4,8]
plt.plot(y, f4, '--g*', label = '2 forks') 





########
#4 forks 
f4 = [] 
x = [1,2] 
for i in x:
    path = "./stdc_4f{}t/*.out".format(i)
    sum = 0 
    events = []
    times = []
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f:
                if re.search("accepted", line):
                    event = re.findall(r'[\d]+', line)
                    e = float(event[0])
                    events.append(e)
                if re.search(r"\bprocess\b", line):
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
    maxt = max(times)
    index = times.index(maxt) 
    e = events[index]
    total = e * maxt *1e-3  
    print('4 forks',i,'threads',times, events,maxt, index, e, total )
    f4.append(100/total) 
y = [4,8]
plt.plot(y, f4, '--r*', label = '4 forks') 




########
#all forks 1 thread  
f4 = [] 
x = [1,2,4,8] 
for i in x:
    path = "./stdc_{}f1t/*.out".format(i)
    sum = 0 
    events = []
    times = []
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f:
                if re.search("accepted", line):
                    event = re.findall(r'[\d]+', line)
                    e = float(event[0])
                    events.append(e)
                if re.search(r"\bprocess\b", line):
                    time = re.findall(r'[\d\.\d]+',line)
                    t = float(time[0])
                    times.append(t)
    maxt = max(times)
    index = times.index(maxt) 
    e = events[index]
    total = e * maxt *1e-3  
    print(i, 'forks', '1 thread',times, events, maxt, index, e, total )
    f4.append(100/total) 
y = [1,2,4,8]
plt.plot(y, f4, '--m*', label = 'Increasing forks (1 thread)') 

first_value = f4[0] 
y = np.array(y)
z = y * first_value
plt.plot(y, z, '--k', label = 'Ideal scaling') 


########
plt.xlabel('N events (forks * threads) ') 
plt.ylabel('throughput') 
plt.legend()
plt.savefig("threads_forks_final_stdc.png")
