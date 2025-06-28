# imports
from collections import Counter, defaultdict
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

'''
PositionalIndex:
Maintains a mapping from each term to its document frequency and positional postings.
'''
class PositionalIndex:
    def __init__(self):
        self.index = {}

    def append_index(self, term: str, doc_id: int, pos: list):
        # Adds a term and its position to the index for a specific doc
        for element in pos:
            if term in self.index:
                doc_map = self.index[term][1]

                if doc_id in doc_map:
                    doc_map[doc_id].add(element)
                else:
                    self.index[term][0] += 1  
                    doc_map[doc_id] = {element}
            else:
                # First occurance of term - intialize entry with document and position
                self.index[term] = [1, {doc_id: {element}}]

    def Output_Index_List(self):
        # Prints a formatted view of the positional index
        print("Positional Inverted Index:\n")
        for term, (doc_freq, postings) in self.index.items():
            print(f"Term: '{term}' | Document Frequency: {doc_freq}")
            for doc_id, positions in postings.items():
                print(f"  Doc {doc_id}: Positions {sorted(list(positions))}")
        print()

    @property
    def indexList(self):
        # Getter of index dictionary
        return self.index

'''
Preprocess raw text into a dictionary of valid tokens with their first positions.
Steps:
 1. Lowercase text and tokenize.
 2. Track position of each token.
 3. Remove stopwords.
 4. Remove non-alphabetic characters.
 5. Trim and discard single-character tokens.
 6. Return cleaned tokens with their original positions.
'''
def text_preprocessor(raw_text) -> dict:

    lowered = raw_text.lower()
    # print(f"lowered : {lowered}")
    raw_tokens = word_tokenize(lowered)
    # print(f"raw_tokens : {raw_tokens}")

    token_positions = defaultdict(list)
    for idx, token in enumerate(raw_tokens, start=1):
        token_positions[token].append(idx)

    stopword_set = set(stopwords.words("english"))
    filtered = [t for t in raw_tokens if t not in stopword_set]

    alpha_tokens = [re.sub(r"[^a-zA-Z]", " ", t) for t in filtered]

    cleaned = [t.strip() for t in alpha_tokens if len(t.strip()) > 1]

    # print(f"cleaned : {cleaned}")

    # Filter valid tokens with recorded positions
    final_output = {term: token_positions[term] for term in cleaned if term in token_positions}

    # print("final output : ", final_output)

    return final_output


'''
Search for exact phrases across indexed documents.
Only supports phrases with up to 5 words.
'''

def phrase_finder(inverted_index, phrase):
    terms = phrase.lower().split()
    term_count = len(terms)

    if term_count > 5:
        raise ValueError("Maximum allowed phrase length is 5 words.")

    first_term = terms[0]
    if first_term not in inverted_index:
        return {}

    initial_docs = inverted_index[first_term][1]
    candidate_docs = list(initial_docs.keys())
    positional_data = {doc: [] for doc in candidate_docs}

    # Checks each successive terms proximity
    for offset, term in enumerate(terms[1:], start=1):
        if term not in inverted_index:
            return {}

        current_docs = inverted_index[term][1]
        candidate_docs = merge(candidate_docs, list(current_docs.keys()))

        if not candidate_docs:
            return {}

        candidate_docs, updated_positions = verify_positional_prox(
            candidate_docs, positional_data, initial_docs, current_docs, offset
        )

        if not candidate_docs:
            return {}

        positional_data = updated_positions

    # Only return documents that match the full phrase
    return {
        doc_id: positions
        for doc_id, positions in positional_data.items()
        if len(positions) == term_count
    }

# Merge two sorted lists of doc ID's 
def merge(docs_a, docs_b):
    result = []
    ptr_a, ptr_b = 0, 0

    while ptr_a < len(docs_a) and ptr_b < len(docs_b):
        doc_a = docs_a[ptr_a]
        doc_b = docs_b[ptr_b]

        if doc_a == doc_b:
            result.append(doc_a)
            ptr_a += 1
            ptr_b += 1
        elif doc_a < doc_b:
            ptr_a += 1
        else:
            ptr_b += 1

    return result

"""
Checks if two terms appear exactly 'expected_gap' positions apart in each document.
Used to validate phrase sequence during phrase search.
"""
def verify_positional_prox(doc_ids, current_positions, first_term_map, next_term_map, expected_gap):
    matched_docs = []
    new_position_map = {doc: [] for doc in doc_ids}

    for doc in doc_ids:
        first_positions = first_term_map[doc]
        next_positions = next_term_map[doc]
    
        for pos1 in first_positions:
            for pos2 in next_positions:
                if pos2 - pos1 == expected_gap:
                    matched_docs.append(doc)
                    sequence_range = list(range(pos1, pos2 + 1))
                    new_position_map[doc].extend(sequence_range)
                    break
            if doc in matched_docs:
                break

    return matched_docs, new_position_map
