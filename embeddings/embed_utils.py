import numpy as np

def normalize_embeddings(embeddings):
    norm = np.linalg.norm(embeddings, axis=1, keepdims=True)
    return embeddings / norm
