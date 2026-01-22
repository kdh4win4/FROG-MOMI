import pandas as pd
from pathlib import Path
import requests

def load_tcga_expression_stub():
    """
    STUB: replace with real TCGA download (GDC API or preprocessed source)
    For now, returns random matrix for pipeline wiring.
    """
    import numpy as np
    rng = np.random.default_rng(0)
    X = pd.DataFrame(
        rng.normal(size=(200, 8000)),
        index=[f"TCGA_{i}" for i in range(200)],
        columns=[f"G{i}" for i in range(8000)]
    )
    meta = pd.DataFrame({
        "vital_status": rng.choice(["Alive", "Dead"], size=200)
    }, index=X.index)
    return X, meta
