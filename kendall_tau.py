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
with_comp=[]
for k in xrange(len_d):
	to_comp=[]
	for i in xrange(len(rank)):
		temp=rank[i].split("\t")
		to_comp.append(temp[k])
	str1=""
	for i in xrange(len_d):
		for j in xrange(len(rank)):
			temp=rank[j].split("\t")
			with_comp.append(temp[i])
		co_pa=0
		do_pa=0
		for x in xrange(len(to_comp)-1):
			for y in xrange(x+1,len(to_comp)):
				x_s=to_comp[x]
				y_s=to_comp[y]
				if(with_comp.index(y_s)>with_comp.index(x_s)):
					co_pa+=1
				else:
					do_pa+=1
		kt_val=round(float(co_pa - do_pa)/(len(rank)*(len(rank)-1)*0.5),2)
		str1+=str(kt_val)+"\t"
		with_comp=[]
	print str1

