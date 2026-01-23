# TCGA-BRCA Prediction

This step trains a supervised model to predict clinical phenotype
and explains model decisions using SHAP.

---

## 1. Prepare data
```python
from sklearn.model_selection import train_test_split

y = meta["label"]
X_model = Xf.loc[y.index]

X_train, X_test, y_train, y_test = train_test_split(
    X_model, y, test_size=0.2, random_state=42, stratify=y
)

X_train.shape, X_test.shape
````

## 2. Train model (XGBoost)

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_train, y_train)
```

## 3. Evaluate performance

```python
from sklearn.metrics import roc_auc_score

proba = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, proba)
auc
```

## 4. Explain model (SHAP)

```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

shap.summary_plot(shap_values, X_test, show=False)
```

## 5. Interpretation
The model captures a small set of genes that strongly drive
clinical outcome prediction. These features will be prioritized
in the next step for target discovery and pathway analysis.

