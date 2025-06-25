# imports
import numpy as np 
import math as math 
from numpy.linalg import norm
from Q1 import *

# Creates a zero-intialized TF-IDF matrix with shape
def generate_matrix(doc_count: int, index_data: PositionalIndex):
    num_rows = doc_count
    num_cols = len(index_data.indexList)

    flat_zeros = [0.0] * (num_rows * num_cols)
    empty_matrix = np.reshape(np.array(flat_zeros, dtype=float), (num_rows, num_cols))

    return empty_matrix

# Computes the TF-IDF score for a document
def tf_idf(term: str, doc_id: int, index: PositionalIndex, total_docs: int, scheme: int):
    tf_value = 0.0

    if term not in index.indexList:
        return 0.0

    term_docs = index.indexList[term][1]
    term_freq = len(term_docs.get(doc_id, []))

    if scheme == 1:  # Binary
        tf_value = 1.0 if term_freq > 0 else 0.0

    elif scheme == 2:  # Raw Count
        tf_value = float(term_freq)

    elif scheme == 3:  # Term Frequency (Normalized by total terms in document)
        total_terms = 0
        for token, (_, doc_map) in index.indexList.items():
            if doc_id in doc_map:
                total_terms += len(doc_map[doc_id])
        tf_value = float(term_freq) / total_terms if total_terms > 0 else 0.0

    elif scheme == 4:  # Log Normalization
        tf_value = math.log(1 + term_freq, 10)

    elif scheme == 5:  # Double Normalization
        max_freq = 0
        for _, (_, doc_map) in index.indexList.items():
            freq = len(doc_map.get(doc_id, []))
            if freq > max_freq:
                max_freq = freq
        if max_freq > 0:
            normalized = term_freq / max_freq
            tf_value = 0.5 + 0.5 * normalized
        else:
            tf_value = 0.0

    # Computes IDF component
    doc_freq = index.indexList[term][0]
    idf_value = math.log(total_docs / (doc_freq + 1), 10)

    return tf_value * idf_value


# Populates an TF-IDF matrix for documents
def generate_tf_idf_matrix(pos_ind:PositionalIndex, document_count:int, weight_scheme: int):
    matrix = generate_matrix(document_count, pos_ind)
    col = 0

    for word in pos_ind.indexList:
        for doc in pos_ind.indexList[word][1]:
            tfidf = tf_idf(word, doc, pos_ind, document_count, weight_scheme)
            matrix[doc -1][col]= tfidf
        col += 1 
    return matrix

def vector_query(query_terms: list, vocab_size: int, index: PositionalIndex):
    vector = np.zeros(vocab_size, dtype=int)
    position = 0

    for term in index.indexList.keys():
        if term in query_terms:
            vector[position] = 1
        position += 1

    return vector

# Computes top 5 relevant docs based on raw TF-IDF score
def top_5_relevant_docs(query_vec, tfidf_data, num_docs: int):
    relevance_scores = np.zeros(num_docs, dtype=float)

    doc_id = 0
    while doc_id < num_docs:
        relevance_scores[doc_id] = np.dot(query_vec, tfidf_data[doc_id])
        doc_id += 1

    # Sorts in descending order
    ranked_docs = np.argsort(-relevance_scores) 
    top_matches = ranked_docs[:5]

    return top_matches


# Computes top 5 docs using cosine similarity between document and query vectors
def cosine_sims(query_vec, tfidf_matrix, num_documents: int):
    similarities = np.zeros(num_documents, dtype=float)
    idx = 0

    while idx < num_documents:
        doc_vec = tfidf_matrix[idx]
        dot_product = np.dot(query_vec, doc_vec)

        if dot_product > 0:
            denominator = norm(query_vec) * norm(doc_vec)
            if denominator != 0:
                similarities[idx] = dot_product / denominator
        idx += 1

    ranked_indices = np.argsort(-similarities)
    top_five = ranked_indices[:5]

    return top_five
