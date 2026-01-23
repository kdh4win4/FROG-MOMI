# TCGA-BRCA Stratification

This step identifies latent molecular subtypes from RNA-seq expression
without using clinical labels.

---

## 1. Feature preparation
```python
from src.preprocess import basic_qc_filter, zscore

Xf = basic_qc_filter(X)
Xf = zscore(Xf)
Xf.shape
```

## 2. Dimensionality reduction (UMAP)
```python
from src.stratify import embed_umap

emb = embed_umap(Xf)
emb.head()
```

## 3. Unsupervised clustering
```python
from src.stratify import cluster_kmeans

clusters = cluster_kmeans(emb, k=3)
clusters.value_counts()
```
