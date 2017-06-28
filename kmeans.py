from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabaz_score
from sklearn.decomposition import PCA 
from scipy import cluster
import pylab as pl
import numpy as np

#ucitavanje vektora sa znacajkama
text_file = open("all_vectors.txt", "r")
vectors = []
for line in text_file:
  splitted_line = line.split(',')
  float_line = []
  for values in splitted_line:
    value_as_float = float(values)
    float_line.append(value_as_float)
  vectors.append(float_line)
text_file.close()

#scipy elbow - odredivanje broja klastera
initial = [cluster.vq.kmeans(vectors,i) for i in range(1,15)]
pl.plot([var for (cent,var) in initial])
pl.show()

#pca
pca = PCA(n_components=900)
pca.fit(vectors)
vectors = pca.transform(vectors)

#kmeans
k_means = KMeans(n_clusters=11)
k_means.fit(vectors)

#mjere evaluacije
print("silhouette: ",silhouette_score(vectors, k_means.labels_, metric='euclidean'))
print("calinski_harabaz: ",calinski_harabaz_score(vectors, k_means.labels_))

#ispis u file 
file = open("ispis.txt", 'w')
for i in range(0, len(vectors)):
  value = str(i+1).zfill(4)+str(".jpg")
  file.write(value)
  file.write("\t")
  label = str(k_means.labels_[i])
  file.write(label)
  file.write("\n")
file.close()
