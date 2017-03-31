# takes as input a matrix with each column representing a ranking.....
# outputs kendal tau similarity values between every pair of rankings......


import sys
fs=open(sys.argv[1])
temp=[]
rank=[]
for line in fs:
	line=line.replace("\n","")
	temp=line.split("\t")
	len_d=len(temp)
	rank.append(line)
fs.close()
#print "H_S\tH_k\tlNk-Hk Hk/lHk   Pur\t NMI\t ARI"
const=len(rank)*((len(rank)**2)-1)
for k in xrange(len_d):
	to_comp={}
	for i in xrange(len(rank)):
		temp=rank[i].split("\t")
		to_comp[temp[k]]=i
	str1=""
	for i in xrange(len_d):
		with_comp={}
		for j in xrange(len(rank)):
			temp=rank[j].split("\t")
			with_comp[temp[i]]=j
		d_m=0.0
		for key in to_comp:
			d_m+=(to_comp[key]-with_comp[key])**2
		val=1-(6*d_m)/const
		str1+=str(val)+"\t"
	print str1
