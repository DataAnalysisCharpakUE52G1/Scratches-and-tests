import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster
import typing


def plot_dendogram(clust):
    plt.figure(figsize=(25, 10))
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("sample index")
    plt.ylabel("distance")
    hac.dendrogram(
        clust,
        leaf_rotation=90.0,  # rotates the x axis labels
        leaf_font_size=8,  # font size for the x axis labels
    )
    plt.show()


def spearman_metric(x, y):
    r = stats.pearsonr(x, y)[0]
    return 1 - r  # correlation to distance: range 0 to 2


def print_clusters(tss, Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion="maxclust")

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    for clust in clusters:
        cluster_indeces = s[s == clust].index
        print(
            f"Cluster {clust}: {list(cluster_indeces)}"
        )
        if plot:
            tss.T.iloc[:, cluster_indeces].plot()
            plt.show()


def build_test_dataframe(
    n, a_min=9, a_max=11, a_nb=3, phy_min=0, phy_max=np.pi, phy_nb=2, w1=1, w2=2
):
    x = np.linspace(0, 5, n)

    tab = []
    for a in np.linspace(a_min, a_max, a_nb):
        for w in [w1, w2]:
            for phy in np.linspace(phy_min, phy_max, phy_nb):
                tab.append(a * np.sin(w * x + phy))
    return np.array([*tab])


if __name__ == "__main__":
    timeSeries = build_test_dataframe(8)
    print(timeSeries)

    cluster = hac.linkage(timeSeries)
    print(cluster)
    print_clusters(timeSeries, cluster, 5, plot=False)
