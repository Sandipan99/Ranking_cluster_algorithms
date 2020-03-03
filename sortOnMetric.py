# takes the all results file with algorithms and different metrics... create a file sorted on different metrics...
import os

metrics = ['', 'H_s', '', 'pur', 'nmi', 'ari', 'sh', 'db']
metric_id = [1, 3, 4, 5, 6, 7]

ranks = {}

for id_ in metric_id:
    rank = {}
    with open('Data-GT/abalone/all_results') as fs:
        for line in fs:
            temp = line.strip().split('\t')
            rank[temp[0]] = float(temp[id_])

    ranks[metrics[id_]] = []
    for alg, val in sorted(rank.items(), key = lambda x:x[1], reverse = True):
        ranks[metrics[id_]].append(alg)

print(ranks['pur'])
print(ranks['H_s'])

with open('Data-GT/abalone/all_ranks', 'w') as ft:
    for i in range(12):
        str_ = ''
        for j in metric_id:
            str_+=ranks[metrics[j]][i]+'\t'
        ft.write(str_)
        ft.write('\n')

#os.system('paste Data-GT/abalone/all_ranks Data-GT/abalone/combined_rank > Data-GT/abalone/all_ranks')