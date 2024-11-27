import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

def naive_pipeline(corpus_embedding, queries_embedding, dbids=None):  
    cosim = cosine_similarity(queries_embedding, corpus_embedding)
    sorted_indices = np.argsort(cosim, axis=1)
    naive_top_five = dbids[sorted_indices[:, ::-1][:, :5]]
    return naive_top_five