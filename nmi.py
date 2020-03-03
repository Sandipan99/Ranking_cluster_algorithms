import math
import sys
fs = open(sys.argv[1])   #ground-truth(linewise)
ft = open(sys.argv[2])    #clustering-algorithm(linewise)
comm_football = []
comm_louvain = []

temp = []
temp1 = []
N = float(sys.argv[3])
for line in fs:
    comm_football.append(line.strip())

fs.close()
for line in ft:
    comm_louvain.append(line.strip())
ft.close()

mid1 = []
mid2 = []
mid = []
I_omega = 0.0
for line1 in comm_football:
    temp = line1.split("\t")
    for i in range(len(temp)):
        mid1.append(int(temp[i]))

    count = 0
    for line2 in comm_louvain:
        temp1 = line2.split("\t")
        count += 1
        for j in range(len(temp1)):
            mid2.append(int(temp1[j]))

        mid = list(set(mid1) & set(mid2))
        val1 = (N*(len(mid)))/(len(mid1)*len(mid2))
        val2 = len(mid)/N
        if val1 > 0:
            I_omega += val2*math.log(val1, 2)
        mid2 = []
        mid = []
    mid1 = []
H_omega = 0.0
H_clus = 0.0
for line in comm_football:
    temp = line.split("\t")
    val = float(len(temp))/N
    H_omega += (-1)*val*math.log(val,2)
for line in comm_louvain:
    temp = line.split("\t")
    val = float(len(temp))/N
    H_clus += (-1)*val*math.log(val,2)
nmi = float(2*I_omega)/(H_omega+H_clus)
print(nmi)
