import pandas as pd
import numpy as np

def basic_qc_filter(X):
    """
    Simple QC: remove genes with zero variance
    """
    return X.loc[:, X.var() > 0]


def zscore(X):
    """
    Z-score normalization per gene
    """
    return (X - X.mean()) / X.std()

