from sklearn.cluster import SpectralClustering, Birch, AgglomerativeClustering, AffinityPropagation, KMeans
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



data = np.loadtxt('Data-GT/US_consensus/dataset',delimiter=',')

print('fitting clusters')
clustering_spec = SpectralClustering(n_clusters=10, assign_labels="discretize").fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/spectral_cluster', clustering_spec)
saveOutput('Data-GT/plos-one/US_consensus/spectral_cluster', clustering_spec)

print('fitting clusters')
clustering_b = Birch(n_clusters=10).fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/birch_cluster', clustering_b)
saveOutput('Data-GT/plos-one/US_consensus/birch_cluster', clustering_b)

print('fitting clusters')
clustering_comp_eu = AgglomerativeClustering(n_clusters=10, affinity='euclidean',linkage='complete').fit(data)
clustering_avg_eu = AgglomerativeClustering(n_clusters=10, affinity='euclidean',linkage='average').fit(data)
clustering_sing_eu = AgglomerativeClustering(n_clusters=10, affinity='euclidean',linkage='single').fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/complete_euclidean_cluster', clustering_comp_eu)
saveOutput('Data-GT/plos-one/US_consensus/complete_euclidean_cluster', clustering_comp_eu)
saveOutputlinewise('Data-GT/US_consensus/average_euclidean_cluster', clustering_avg_eu)
saveOutput('Data-GT/plos-one/US_consensus/average_euclidean_cluster', clustering_avg_eu)
saveOutputlinewise('Data-GT/US_consensus/single_euclidean_cluster', clustering_sing_eu)
saveOutput('Data-GT/plos-one/US_consensus/single_euclidean_cluster', clustering_sing_eu)

print('fitting clusters')
clustering_comp_cb = AgglomerativeClustering(n_clusters=10, affinity='cityblock',linkage='complete').fit(data)
clustering_avg_cb = AgglomerativeClustering(n_clusters=10, affinity='cityblock',linkage='average').fit(data)
clustering_sing_cb = AgglomerativeClustering(n_clusters=10, affinity='cityblock',linkage='single').fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/complete_cityblock_cluster', clustering_comp_cb)
saveOutput('Data-GT/plos-one/US_consensus/complete_cityblock_cluster', clustering_comp_cb)
saveOutputlinewise('Data-GT/US_consensus/average_cityblock_cluster', clustering_avg_cb)
saveOutput('Data-GT/plos-one/US_consensus/average_cityblock_cluster', clustering_avg_cb)
saveOutputlinewise('Data-GT/US_consensus/single_cityblock_cluster', clustering_sing_cb)
saveOutput('Data-GT/plos-one/US_consensus/single_cityblock_cluster', clustering_sing_cb)

print('fitting clusters')
clustering_ap = AffinityPropagation().fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/ap_cluster', clustering_ap)
saveOutput('Data-GT/plos-one/US_consensus/ap_cluster', clustering_ap)

print('fitting clusters')
clustering_km = KMeans(n_clusters=10).fit(data)
print('fitting finished')

saveOutputlinewise('Data-GT/US_consensus/kmeans_cluster', clustering_km)
saveOutput('Data-GT/plos-one/US_consensus/kmeans_cluster', clustering_km)

