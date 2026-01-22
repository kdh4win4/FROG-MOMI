# FROG-MOMI
**Multi-Omics + Clinical Stratification → Target Discovery → Evidence Report**

End-to-end, reproducible pipeline that connects public multi-omics data with
machine learning and explainable AI to identify patient subtypes and
biologically grounded target candidates.

---

## What this shows
- Patient/sample stratification from transcriptomics + clinical metadata
- Phenotype prediction with explainability (SHAP)
- Target / biomarker shortlist via DEG + pathway analysis
- Evidence-backed reporting (retrieval-first, LLM-ready)

This project is designed to demonstrate **how AI supports biomedical decision-making**, not just model accuracy.

---

## Demo workflow
1. Load public dataset (TCGA)
2. Stratify samples (UMAP + clustering)
3. Predict phenotype (XGBoost)
4. Explain drivers (SHAP)
5. Discover targets (DEG + GSEA)
6. Generate evidence report (Markdown)

---

## Tech stack
- Python (pandas, scikit-learn, xgboost, shap)
- UMAP, GSEA (gseapy)
- Streamlit (demo UI)
- Modular, reproducible pipeline

---

## Status
🚧 MVP in progress (single TCGA cancer type)

---

## Disclaimer
Public data only. No PHI used.

## Demo (visual overview)

> This section will show the full end-to-end workflow once the MVP is complete.

### 1. Sample stratification
UMAP embedding of samples with unsupervised clustering to reveal latent subtypes.

![Stratification](docs/figures/stratify.png)

---

### 2. Phenotype prediction + explainability
XGBoost model predicts clinical phenotype, with SHAP highlighting key drivers.

![Prediction](docs/figures/shap.png)

---

### 3. Target discovery
Differential expression and pathway enrichment identify candidate targets.

![Targets](docs/figures/targets.png)

---

### 4. Evidence report (auto-generated)
Top candidates are summarized with retrieved literature evidence in a Markdown report.

![Report](docs/figures/report.png)


