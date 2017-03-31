import sys
fs=open(sys.argv[1])   #football_community_map
node_comm={}
temp=[]
intm=[]
for line in fs:
	line=line.replace("\n","")
	temp=line.split("\t")
	node_comm[temp[0]]=int(temp[1])

fs.close()
#print len(node_comm)
sum1=0
fs=open(sys.argv[2])		#football_community_louvain
for line in fs:
	line=line.replace("\n","")
	#print line
	temp=line.split("\t")
	for i in xrange(len(temp)-1):
		if(temp[i] in node_comm):
			intm.append(int(node_comm[temp[i]]))
		#print temp[i]+"\t"+str(node_comm[temp[i]])
	intm.sort()
	max_count=0
	count=1
	#print intm
	if(len(intm)>1):
		for i in xrange(len(intm)-1):
			if(intm[i]==intm[i+1]):
				count+=1
			else:
				if(max_count<count):
					max_count=count
					index=intm[i]
				count=1
		if(max_count<count):
			max_count=count
			index=intm[i+1]
		#print str(max_count)+"#"+str(index)
		#print "%%%%%%%-------------------%%%%%%%"
		sum1+=max_count
		max_count=0
		index=0
		intm=[]
	else:
		sum1+=1
		intm=[]
		max_count=0
		index=0
print float(sum1)/int(sys.argv[3])
