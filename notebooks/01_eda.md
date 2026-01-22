# TCGA-BRCA EDA

## 1. Load data
```python
from src.io_tcga import load_tcga_expression_stub

X, meta = load_tcga_expression_stub()
X.shape, meta.head()

meta["label"] = (meta["vital_status"] == "Dead").astype(int)
meta["label"].value_counts()
