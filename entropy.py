##calculates h[s] and h[k] for communities given in linewise format
import sys
import math
fs = open(sys.argv[1]) # cluster output from algorithm in linewise format....
nodes = float(sys.argv[2]) # number of datapoints
mid = []
comm = []
for line in fs:
	temp = line.strip().split("\t")
	mid.append(len(temp))
fs.close()
mid.sort()
comm_count = len(mid)
count = 1
if len(mid)==1:
	comm.append(str(mid[0])+"\t"+str(count))
else:  
	for i in range(len(mid)-1):
		if mid[i] == mid[i+1]:
			count += 1
		else:
			comm.append(str(mid[i])+"\t"+str(count))
			count=1
	comm.append(str(mid[i+1])+"\t"+str(count))
#print str(mid[i+1])+"\t"+str(count)
temp = []
entr = 0.0
for line in comm:
	temp=line.split("\t")
	a=float(temp[0])/nodes
	val=a*math.log(a,2)*(-1)
	entr+=val*float(temp[1])
#fs.close()
entr_hk = 0.0
for line in comm:
	temp=line.split("\t")
	#print temp[0]+"\t"+temp[1]
	a=float(temp[0])*float(temp[1])/nodes
	val=a*math.log(a,2)*(-1)
	#print val
	entr_hk+=val
print(str(comm_count)+"\t"+str(entr)+"\t"+str(entr_hk))