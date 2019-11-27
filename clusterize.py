import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster
import typing


class Cluster:
    def __init__(self, features: np.ndarray, **kwargs):
        self.features = features
        self.clust = hac.linkage(self.features, **kwargs)

    def dendogram(self):
        plt.figure(figsize=(25, 10))
        plt.title("Hierarchical Clustering Dendrogram")
        plt.xlabel("sample index")
        plt.ylabel("distance")
        hac.dendrogram(self.clust, leaf_rotation=90.0, leaf_font_size=8)
        plt.show()

    def print_clusters(self, n, plot=False):
        results = fcluster(self.clust, n, criterion="maxclust")

        s = pd.Series(results)
        clusters = s.unique()

        for clust in clusters:  # TODO: reformat as print/plot
            cluster_indeces = s[s == clust].index
            print(
                f"Cluster {clust}: {list(cluster_indeces)}"
            )
            if plot:
                self.features.T.iloc[:, cluster_indeces].plot()
                plt.show()
