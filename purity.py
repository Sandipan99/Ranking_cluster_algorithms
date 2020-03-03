import sys

node_comm = {}
temp = []
intm = []
with open(sys.argv[1]) as fs: # ground-truth in linewise format
    i = 0
    for line in fs:
        temp = line.strip().split('\t')
        for item in temp:
            node_comm[item] = i
        i += 1


sum1 = 0
fs = open(sys.argv[2])		# cluster output from algorithm in linewise format
for line in fs:
    temp = line.strip().split("\t")
    for i in range(len(temp)):
        if temp[i] in node_comm:
            intm.append(int(node_comm[temp[i]]))
    intm.sort()
    max_count = 0
    count=1
    if len(intm) > 1:
        for i in range(len(intm)-1):
            if intm[i] == intm[i+1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                    index = intm[i]
                count = 1
        if max_count < count:
            max_count = count
            index = intm[i+1]

        sum1 += max_count
        max_count = 0
        index = 0
        intm = []
    else:
        sum1 += 1
        intm = []
        max_count = 0
        index = 0
print(float(sum1)/int(sys.argv[3]))
