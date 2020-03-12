from sklearn.cluster import SpectralClustering, Birch
import numpy as np


def saveOutputlinewise(fname, clustering):
    clusters = {}

    for i,value in enumerate(clustering.labels_):
        if value not in clusters:
            clusters[value] = [str(i+1)]
        else:
            clusters[value].append(str(i+1))

    with open(fname, 'w') as ft:
        for key in clusters:
            ft.write('	'.join(clusters[key]))
            ft.write('\n')

def saveOutput(fname, clustering): # saves output with each line as the label and index as the datapoint
    with open(fname, 'w') as ft:
        for v in clustering.labels_:
            ft.write(f'{v}\n')



data = np.loadtxt('Data-GT/Whitewine/rank_features',delimiter=',')
data = np.transpose(data)
print(data.shape)

'''
print('fitting clusters')
clustering_spec = SpectralClustering(n_clusters=7, assign_labels="discretize").fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/Whitewine/spectral_cluster_rank', clustering_spec)
saveOutput('Data-GT/plos-one/Whitewine/spectral_cluster_rank', clustering_spec)
'''
print('fitting clusters')
clustering_b = Birch(n_clusters=7).fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/Whitewine/birch_cluster_rank', clustering_b)
saveOutput('Data-GT/plos-one/Whitewine/birch_cluster_rank', clustering_b)
