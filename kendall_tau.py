# takes as input a matrix with each column representing a ranking.....
# outputs kendal tau similarity values between every pair of rankings......

fs = open('Data-GT/MNIST/all_ranks_use')
temp = []
rank = []
for line in fs:
	temp=line.strip().split("\t")
	len_d=len(temp)
	rank.append(line.strip())
fs.close()
with_comp = []
print('H[s] & Purity & NMI & ARI & SH & DB & Majority')
label = ['H[s]','Purity','NMI','ARI','SH','DB','Majority']
for k in range(len_d):
	to_comp=[]
	for i in range(len(rank)):
		temp=rank[i].split("\t")
		to_comp.append(temp[k])
	str1 = label[k]+" & "
	for i in range(len_d):
		for j in range(len(rank)):
			temp=rank[j].split("\t")
			with_comp.append(temp[i])
		co_pa=0
		do_pa=0
		for x in range(len(to_comp)-1):
			for y in range(x+1,len(to_comp)):
				x_s=to_comp[x]
				y_s=to_comp[y]
				if with_comp.index(y_s)>with_comp.index(x_s):
					co_pa+=1
				else:
					do_pa+=1
		kt_val=round(float(co_pa - do_pa)/(len(rank)*(len(rank)-1)*0.5),2)
		str1+=str(kt_val)+"& "
		with_comp=[]
	print(str1)

