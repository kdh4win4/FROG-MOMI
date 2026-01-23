# TCGA-BRCA Target Discovery

This step identifies candidate genes and pathways that differentiate
molecular subtypes and are predictive of clinical outcome.

---

## 1. Define comparison groups
```python
groups = clusters
groups.value_counts()
```

## 2. Differential expression analysis
```python
import pandas as pd
from scipy.stats import ttest_ind

group0 = Xf[groups == 0]
group1 = Xf[groups == 1]

stat, pval = ttest_ind(group0, group1, axis=0, equal_var=False)
deg = pd.DataFrame({
    "gene": Xf.columns,
    "pvalue": pval,
    "logFC": group1.mean() - group0.mean()
}).sort_values("pvalue")

deg.head()
```

## 3. Select top candidate genes
```python
top_genes = deg.query("pvalue < 0.01").head(50)
top_genes
```

## 4. Pathway enrichment (GSEA)
```python
import gseapy as gp

rnk = deg.set_index("gene")["logFC"]
pre_res = gp.prerank(
    rnk=rnk,
    gene_sets="KEGG_2021_Human",
    min_size=15,
    max_size=500,
    permutation_num=100,
    outdir=None,
    seed=42
)

pre_res.res2d.head()
```

## 5. Interpretation
Top genes and pathways represent candidate targets or biomarkers
associated with molecular subtypes and clinical outcome.
These will be passed to the evidence reporting step.
