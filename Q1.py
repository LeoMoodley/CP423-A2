# imports
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

'''
PositionalIndex:
 - Stores a list of key-value pair for the tokens and their data.
    - The key is the word/token.
    - The value is a list. The first element of the list is the document frequency. The second is another dict that maps the doc ID's to a positional list (set).
'''
class PositionalIndex:
    def __init__(self):
        # Initialize an empty index dictionary
        self.index = {}

    def addIndex(self, term: str, doc_id: int, pos: int):
        # If term is already in the index
        if term in self.index:
            doc_map = self.index[term][1]

            if doc_id in doc_map:
                doc_map[doc_id].add(pos)
            else:
                self.index[term][0] += 1  # Increment document frequency
                doc_map[doc_id] = {pos}
        else:
            # Initialize new term entry
            self.index[term] = [1, {doc_id: {pos}}]

    def printIndexList(self):
        print("Positional Inverted Index:\n")
        for term, (doc_freq, postings) in self.index.items():
            print(f"Term: '{term}' | Document Frequency: {doc_freq}")
            for doc_id, positions in postings.items():
                print(f"  Doc {doc_id}: Positions {sorted(list(positions))}")
        print()

    @property
    def indexList(self):
        return self.index


'''
Tests for the PositionalIndex class
'''
# add a single word
def test_single_word_single_doc_single_position():
    print("test_single_word_single_doc_single_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 1)

    index.printIndexList()

# add the same word and document but different positions
def test_single_word_single_doc_multi_position():
    print("test_single_word_single_doc_multi_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 1)
    index.addIndex("word", 1, 2)
    index.addIndex("word", 1, 3)
    index.addIndex("word", 1, 4)
    index.addIndex("word", 1, 5)

    index.printIndexList()

# add the same word with different documents and different positions
def test_single_word_multi_doc_multi_position():
    print("test_single_word_multi_doc_multi_position:")
    index = PositionalIndex()

    index.addIndex("word", 1, 2)
    index.addIndex("word", 2, 4)
    index.addIndex("word", 3, 6)
    index.addIndex("word", 4, 8)
    index.addIndex("word", 5, 10)

    index.printIndexList()

'''
Function for preprocessing the text
'''
def preprocess_text(raw_text) -> dict:
    import re
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

    # Step 1: Normalize and tokenize
    lowered = raw_text.lower()
    raw_tokens = word_tokenize(lowered)

    # Step 2: Capture original token positions
    token_positions = {}
    for idx, token in enumerate(raw_tokens, start=1):
        token_positions[token] = idx

    # Step 3: Define stopwords and filter them out
    stopword_set = set(stopwords.words("english"))
    filtered = [t for t in raw_tokens if t not in stopword_set]

    # Step 4: Remove non-alphabetic characters
    alpha_tokens = [re.sub(r"[^a-zA-Z]", " ", t) for t in filtered]

    # Step 5: Trim and filter single-character tokens
    cleaned = [t.strip() for t in alpha_tokens if len(t.strip()) > 1]

    # Step 6: Create final dictionary with valid positions
    final_output = {term: token_positions[term] for term in cleaned if term in token_positions}

    return final_output


'''
Function for searching phrase queries
'''

def search_phrase(inverted_index, phrase):
    terms = phrase.lower().split()
    term_count = len(terms)

    if term_count > 5:
        raise ValueError("Maximum allowed phrase length is 5 words.")

    # Get documents containing the first term
    first_term = terms[0]
    if first_term not in inverted_index:
        return {}

    initial_docs = inverted_index[first_term][1]
    candidate_docs = list(initial_docs.keys())
    positional_data = {doc: [] for doc in candidate_docs}

    for offset, term in enumerate(terms[1:], start=1):
        if term not in inverted_index:
            return {}

        current_docs = inverted_index[term][1]
        candidate_docs = merge(candidate_docs, list(current_docs.keys()))

        if not candidate_docs:
            return {}

        candidate_docs, updated_positions = check_positional_proximity(
            candidate_docs, positional_data, initial_docs, current_docs, offset
        )

        if not candidate_docs:
            return {}

        positional_data = updated_positions

    return {
        doc_id: positions
        for doc_id, positions in positional_data.items()
        if len(positions) == term_count
    }


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


def check_positional_proximity(doc_ids, current_positions, first_term_map, next_term_map, expected_gap):
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


''''
Run tests for Q1 functions (DEBUG)
'''
# if __name__ == "__main__":
#     '''
#     Tests for Positional Index
#     '''
#     test_single_word_single_doc_single_position()
#     test_single_word_single_doc_multi_position()
#     test_single_word_multi_doc_multi_position()

#     '''
#     Tests for the Phrase queries function
#     '''
#     print("Testing phrase queries...\n")
#     index = PositionalIndex()

#     # Add some sample data
#     index.addIndex("apple", 1, 2)
#     index.addIndex("apple", 2, 1)
#     index.addIndex("with", 2, 2)
#     index.addIndex("apple", 3, 9)
#     index.addIndex("banana", 1, 3)
#     index.addIndex("banana", 2, 2)
#     index.addIndex("banana", 2, 3)
#     index.addIndex("orange", 2, 4)
#     index.addIndex("orange", 3, 8)

#     index.printIndexList()

#     # Test the search_phrase function
#     query = "apple with banana"
#     result = search_phrase(index.indexList, query)
#     print(f"Search Query: '{query}'")
#     print(f"Result: {result}")

#     query = "banana orange"
#     result = search_phrase(index.indexList, query)
#     print(f"Search Query: '{query}'")
#     print(f"Result: {result}")

#     query = "apple banana"
#     result = search_phrase(index.indexList, query)
#     print(f"Search Query: '{query}'")
#     print(f"Result: {result}")