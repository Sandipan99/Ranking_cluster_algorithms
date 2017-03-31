import sys
fs=open(sys.argv[1])  #ground truth community in line-wise format
ft=open(sys.argv[2])  #communities detected by algorithm in line-wise format
community_football=[]
community_louvain=[]
temp=[]
temp1=[]
for line in fs:
	line=line.replace("\n","")
	community_football.append(line)
fs.close()
for line in ft:
	line=line.replace("\n","")
	community_louvain.append(line)
ft.close()
nodes=int(sys.argv[3])
N_s=float(nodes*(nodes-1))/2
N_x=0.0
for line in community_louvain:
	temp=line.split("\t")
	a=int(len(temp)-1)
	N_x+=a*(a-1)/2
N_y=0.0
for line in community_football:
	temp=line.split("\t")
	a=int(len(temp)-1)
	N_y+=a*(a-1)/2
N_x_y=0.0
mid=[]
mid1=[]
mid2=[]
for line1 in community_football:
	temp=line1.split("\t")
	for i in xrange(len(temp)-1):
		mid1.append(temp[i])
	for line2 in community_louvain:
		temp1=line2.split("\t")
		for j in xrange(len(temp1)-1):
			mid2.append(temp1[j])
		mid=list(set(mid1)&set(mid2))
		val=len(mid)
		N_x_y+=val*(val-1)/2
		mid2=[]
		mid=[]
	mid1=[]
val1=N_x_y-((N_x*N_y)/N_s)
val2=0.5*(N_x+N_y)-((N_x*N_y)/N_s)
ari=val1/val2
print ari
