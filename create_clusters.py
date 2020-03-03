from sklearn.cluster import SpectralClustering, Birch
import numpy as np


def saveOutputlinewise(fname, clustering):
    clusters = {}

    for i,value in enumerate(clustering.labels_):
        if value not in clusters:
            clusters[value] = [str(i)]
        else:
            clusters[value].append(str(i))

    with open(fname, 'w') as ft:
        for key in clusters:
            ft.write('	'.join(clusters[key]))
            ft.write('\n')

def saveOutput(fname, clustering): # saves output with each line as the label and index as the datapoint
    with open(fname, 'w') as ft:
        for v in clustering.labels_:
            ft.write(f'{v}\n')



data = np.loadtxt('Data-GT/abalone/feat_mat',delimiter='	 ')


print('fitting clusters')
clustering_spec = SpectralClustering(n_clusters=28, assign_labels="discretize").fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/abalone/spectral_cluster_abalone', clustering_spec)
saveOutput('Data-GT/plos-one/abalone/spectral_cluster', clustering_spec)

print('fitting clusters')
clustering_b = Birch(n_clusters=None).fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/abalone/birch_cluster_abalone', clustering_b)
saveOutput('Data-GT/plos-one/abalone/birch_cluster', clustering_b)
