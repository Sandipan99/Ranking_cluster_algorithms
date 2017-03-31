##calculates h[s] and h[k] for communities given in lnewise format
import sys
import math
fs=open(sys.argv[1])
nodes=float(sys.argv[2])
mid=[]
comm=[]
for line in fs:
	line=line.replace("\n","")
	temp=line.split("\t")
	mid.append(len(temp)-1)
fs.close()
mid.sort()
comm_count=len(mid)
count=1
if(len(mid)==1):
  comm.append(str(mid[0])+"\t"+str(count))
else:  
  for i in xrange(len(mid)-1):
	  if(mid[i]==mid[i+1]):
		  count+=1
	  else:
		  comm.append(str(mid[i])+"\t"+str(count))
		  #print str(mid[i])+"\t"+str(count)
		  count=1
  comm.append(str(mid[i+1])+"\t"+str(count))
#print str(mid[i+1])+"\t"+str(count)
temp=[]
entr=0.0
for line in comm:
	temp=line.split("\t")
	#print temp[0]+"\t"+temp[1]
	a=float(temp[0])/nodes
	val=a*math.log(a,2)*(-1)
	entr+=val*float(temp[1])
#print entr
fs.close()
entr_hk=0.0
for line in comm:
	temp=line.split("\t")
	#print temp[0]+"\t"+temp[1]
	a=float(temp[0])*float(temp[1])/nodes
	val=a*math.log(a,2)*(-1)
	#print val
	entr_hk+=val
print str(comm_count)+"\t"+str(entr)+"\t"+str(entr_hk)	