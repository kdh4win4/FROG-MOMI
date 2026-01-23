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

