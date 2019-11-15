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


def clusterize(tss: pd.DataFrame, metric: typing.Callable = "correlation"):
    return hac.linkage(tss, method="single", metric=metric)


def print_clusters(tss, Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion="maxclust")

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    for clust in clusters:
        cluster_indeces = s[s == clust].index
        print(
            f"Cluster {clust} number of entries {len(cluster_indeces)} : {list(cluster_indeces)}"
        )
        if plot:
            tss.T.iloc[:, cluster_indeces].plot()
            plt.show()


def build_test_dataframe(n) -> pd.DataFrame():
    x = np.linspace(0, 5, n)
    scale = 4

    a = scale * np.sin(x)
    b = scale * (np.cos(1 + x * 3) + np.linspace(0, 1, n))
    c = scale * (np.sin(2 + x * 6) + np.linspace(0, -1, n))
    d = scale * (np.cos(3 + x * 9) + np.linspace(0, 4, n))
    e = scale * (np.sin(4 + x * 12) + np.linspace(0, -4, n))
    f = scale * np.cos(x)

    #
    # from each main series build 'group_size' series
    #

    return pd.DataFrame([a, b, c, d, e, f])


if __name__ == "__main__":
    timeSeries = build_test_dataframe(8)

    cluster = clusterize(timeSeries, metric=spearman_metric)
    print(cluster)
    # plot_dendogram(cluster)

    #
    # To retrieve the Clusters we can use the fcluster function.
    # It can be run in multiple ways (check the documentation).
    # In this example we'll give it as target the number of clusters we want:
    #

    print_clusters(timeSeries, cluster, 6, plot=True)
