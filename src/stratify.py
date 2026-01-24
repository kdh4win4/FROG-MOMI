import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import umap

def embed_umap(X, n_neighbors=15, min_dist=0.1, random_state=42):
    reducer = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        random_state=random_state
    )
    emb = reducer.fit_transform(X)
    return pd.DataFrame(emb, index=X.index, columns=["UMAP1", "UMAP2"])


def cluster_kmeans(emb, k=3, random_state=42):
    km = KMeans(n_clusters=k, n_init=10, random_state=random_state)
    labels = km.fit_predict(emb)
    return pd.Series(labels, index=emb.index, name="cluster")

