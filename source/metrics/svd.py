import numpy as np
import pandas as pd
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import PCA
from tqdm import tqdm

def _sparse_pca(geneset, data, genes):
    genes_in_ds = [gene in geneset for gene in genes]
    in_gs = data[genes_in_ds, :]
    if (in_gs.T == in_gs.T[0]).all():
        return np.zeros(data.shape[1])
    gs_expression = SparsePCA(n_components=1).fit_transform(in_gs.T)
    return gs_expression.flatten()

def sparse_PCA(genesets, data, genes):
    res = np.empty((len(genesets), data.shape[1]))
    for i, (gs_name, geneset_genes) in tqdm(enumerate(genesets.items()), total=len(genesets)):
        res[i] = _sparse_pca(geneset_genes, data, genes)
    return res

def _svd(geneset, data, genes):
    genes_in_ds = [gene in geneset for gene in genes]
    in_gs = data[genes_in_ds, :]
    if (in_gs.T == in_gs.T[0]).all():
        return np.zeros(data.shape[1])
    gs_expression = PCA(n_components=1).fit_transform(in_gs.T)
    return gs_expression.flatten()

def SVD(genesets, data, genes):
    res = np.empty((len(genesets), data.shape[1]))
    for i, (gs_name, geneset_genes) in tqdm(enumerate(genesets.items()), total=len(genesets)):
        res[i] = _svd(geneset_genes, data, genes)
    return res