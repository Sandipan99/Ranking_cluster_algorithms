# takes as input a matrix with each column representing a ranking.....
# outputs kendal tau similarity values between every pair of rankings......

fs = open('Data-GT/Whitewine/all_ranks_use')
temp = []
rank = []
for line in fs:
	temp = line.strip().split("\t")
	len_d = len(temp)
	rank.append(line.strip())
fs.close()

#print "H_S\tH_k\tlNk-Hk Hk/lHk   Pur\t NMI\t ARI"
const = len(rank)*((len(rank)**2)-1)
for k in range(len_d):
	to_comp = {}
	for i in range(len(rank)):
		temp = rank[i].split("\t")
		to_comp[temp[k]] = i

	str1 = ""
	for i in range(len_d):
		with_comp = {}
		for j in range(len(rank)):
			temp = rank[j].split("\t")
			with_comp[temp[i]] = j

		d_m = 0.0
		for key in to_comp:
			d_m += (to_comp[key]-with_comp[key])**2
		val = 1-(6*d_m)/const
		str1 += str(val)+"\t"
	print(str1)
