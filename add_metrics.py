# additional metrics for comparison...

from sklearn.metrics import silhouette_score, davies_bouldin_score
import numpy as np
import os


data = np.loadtxt('Data-GT/abalone/feat_mat',delimiter='	 ')

files = os.listdir('Data-GT/plos-one/abalone/')

for f in files:
    labels = np.loadtxt('Data-GT/plos-one/abalone/'+f)
    print(f'{f}, {silhouette_score(data, labels)}, {davies_bouldin_score(data, labels)}')


