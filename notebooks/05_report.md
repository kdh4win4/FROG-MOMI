# TCGA-BRCA Evidence Report

This step generates a human-readable report that summarizes
candidate targets with supporting evidence for interpretation.

---

## 1. Select final candidates
```python
final_genes = top_genes["gene"].head(10).tolist()
final_genes
```

## 2. Retrieve evidence (literature or annotations)
```python
evidence = {
    g: f"Literature evidence placeholder for {g} (to be replaced by PubMed / RAG retrieval)"
    for g in final_genes
}
evidence
```

## 3. Build report table
```python
import pandas as pd

report_df = pd.DataFrame({
    "Gene": final_genes,
    "Evidence": [evidence[g] for g in final_genes]
})

report_df
```

## 4. Export Markdown report
```python
from src.report import write_markdown_report

sections = [
    ("Candidate targets", report_df.to_markdown(index=False))
]

write_markdown_report(
    "data/processed/TCGA_BRCA_target_report.md",
    "TCGA-BRCA Target Evidence Report",
    sections
)
```

## 5. Interpretation
This report represents the final output of the pipeline.
It connects data-driven target discovery with human-readable evidence,
and can be extended with LLM/RAG-based literature synthesis.
