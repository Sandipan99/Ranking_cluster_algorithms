# additional metrics for comparison...

from sklearn.metrics import silhouette_score, davies_bouldin_score
import numpy as np
import os


#data = np.loadtxt('Data-GT/synt/',delimiter='\t')

'''
files = os.listdir('Data-GT/plos-one/abalone/')

for f in files:
    labels = np.loadtxt('Data-GT/plos-one/abalone/'+f)
    print(f'{f}, {silhouette_score(data, labels)}, {davies_bouldin_score(data, labels)}')
'''
labels = np.loadtxt('Data-GT/plos-one/MNIST/all_clusters',delimiter='\t')
#print(clusters.shape)
#data_rank = np.loadtxt('Data-GT/Whitewine/rank_features',delimitr',')
#data_rank = np.transpose(data_rank)
#print(data_rank.shape)
data_raw = np.loadtxt('Data-GT/MNIST/dataset',delimiter=',')
print(data_raw.shape)
#data = np.transpose(data)

#rank_index = [_ for _ in range(8)] + [18]
#print(rank_index)
with open('Data-GT/MNIST/metric_sh_db', 'w') as ft:
    for i in range(9):
        #if i in rank_index:
        #    ft.write(f'{silhouette_score(data_rank,labels[:,i])}\t{davies_bouldin_score(data_rank, labels[:,i])}\n')
        #else:
        ft.write(f'{silhouette_score(data_raw, labels[:, i])}\t{davies_bouldin_score(data_raw, labels[:, i])}\n')
        #print(f'{silhouette_score(data,labels[:,i])}, {davies_bouldin_score(data, labels[:,i])}')