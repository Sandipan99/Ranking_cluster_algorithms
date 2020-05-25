
def check_for_cycle(net_w1, l, algo):
    rank = []
    for i in range(l):
        flag = 0
        for j in range(l):
            if len(net_w1[j]) == 0:
                rem = j
                rank.append(algo[rem])
                flag = 1
                break
        if flag == 1:
            for j in range(l):
                if rem in net_w1[j]:
                    net_w1[j].remove(rem)
            net_w1[rem].append(100)
        else:
            return 0
    print(rank)
    ft = open("MNIST/combined_rank","w")
    for i in range(len(rank)):
        ft.write(rank[i])
        ft.write("\n")
    ft.close()
    return 1

fs = open("MNIST/all_results_w_labels")
algo = {}
temp = []
count = 0
feat_vector = []
for line in fs:
    temp = line.strip().split("  ")
    algo[count] = temp[0]
    count += 1
    str1 = temp[3]+"\t"+temp[4]+"\t"+temp[5]
    feat_vector.append(str1)
fs.close()

temp1 = []
temp2 = []
net_w = [[] for i in range(len(feat_vector))]
for i in range(len(feat_vector)-1):
    temp1 = feat_vector[i].split("\t")
    for j in range(i+1,len(feat_vector)):
        temp2 = feat_vector[j].split("\t")
        count = 0
        for k in range(3):
            if float(temp1[k])>float(temp2[k]):
                count+=1

        if count>1:
            net_w[j].append(i)

        else:
            net_w[i].append(j)

x = check_for_cycle(net_w, len(feat_vector), algo)
if x == 1:
    print('no cycle')
else:
    print('has cycle')



