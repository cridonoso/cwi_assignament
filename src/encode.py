from sentence_transformers import SentenceTransformer


def encode_corpus_query(corpus, queries):
    corpus_sequences  = [x.to_html() for x in corpus['table']]
    queries_sequences = [x for x in queries['query']]
    context_sequences = [str(x) for x in corpus['context']]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    tables_embeddings  = model.encode(corpus_sequences)
    context_embeddings = model.encode(context_sequences)
    corpus_embeddings  = (tables_embeddings+context_embeddings)/2
    queries_embeddings = model.encode(queries_sequences)

    return corpus_embeddings, queries_embeddings