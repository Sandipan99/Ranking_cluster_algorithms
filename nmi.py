import math
import sys
fs=open(sys.argv[1])   #ground-truth(linewise) 
ft=open(sys.argv[2])    #clustering-algorithm(linewise)
comm_football=[]
comm_louvain=[]
#comm_football_count=[]
#comm_louvain_count=[]
temp=[]
temp1=[]
N=float(sys.argv[3])
for line in fs:
	line=line.replace("\n","")
	#temp=line.split("\t")
	comm_football.append(line)
	#comm_football_count.append(len(temp)-1)
fs.close()
for line in ft:
	line=line.replace("\n","")
	#temp=line.split("\t")
	comm_louvain.append(line)
	#comm_louvain_count.append(len(temp)-1)
ft.close()
mid1=[]
mid2=[]
mid=[]
I_omega=0.0
for line1 in comm_football:
	temp=line1.split("\t")
	for i in xrange(len(temp)-1):
		mid1.append(int(temp[i]))
	count=0
	for line2 in comm_louvain:
		temp1=line2.split("\t")
		count+=1
		#print count
		for j in xrange(len(temp1)-1):
			mid2.append(int(temp1[j])) 
		mid=list(set(mid1)&set(mid2))
		val1=(N*(len(mid)))/(len(mid1)*len(mid2))
		val2=len(mid)/N
		#print len(mid1)
		#print len(mid2)
		#print len(mid)
		#print val1
		#print val2
		#print "-------------"
		if(val1>0):
			I_omega+=val2*math.log(val1,2)
		mid2=[]
		mid=[]
	mid1=[]
H_omega=0.0
H_clus=0.0
for line in comm_football:
	temp=line.split("\t")
	val=float(len(temp)-1)/N
	H_omega+=(-1)*val*math.log(val,2)
for line in comm_louvain:
	temp=line.split("\t")
	val=float(len(temp)-1)/N
	H_clus+=(-1)*val*math.log(val,2)
nmi=float(2*I_omega)/(H_omega+H_clus)
#print I_omega
#print H_omega
#print H_clus
print nmi
