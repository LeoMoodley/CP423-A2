# imports
from Q1 import PositionalIndex, preprocess_text, search_phrase
from Q2 import *
import os

# Properties
# the list of ID's to document names
documents: dict = {}

# the Positional Index that will hold all the document data
positionalIndex: PositionalIndex = None

'''
Reads all the documents in the data folder, tokenize the text, and stores it in the Inverted Index data structure.
'''
def createPositionalIndex():
    inverted_index = PositionalIndex()
    file_names = os.listdir("./data/")
    total_files = len(file_names)
    current_index = 0
    doc_id = 1

    while current_index < total_files:
        file_name = file_names[current_index]
        file_path = "./data/" + file_name

        try:
            file = open(file_path, "r", encoding="utf-8", errors="replace")
            content = file.read()
            file.close()
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
            current_index += 1
            continue

        tokens = preprocess_text(content)
        word_list = list(tokens.items())
        word_index = 0
        num_words = len(word_list)

        while word_index < num_words:
            word, positions = word_list[word_index]
            inverted_index.addIndex(word, doc_id, positions)
            word_index += 1

        documents[doc_id] = file_name
        doc_id += 1
        current_index += 1

    return inverted_index


def checkToLoadDataFiles():
    global positionalIndex
    if (positionalIndex == None):
        print("\nInitializing positional index...")
        positionalIndex = createPositionalIndex()

        print("Index creation complete.\n")

'''
Main function
'''

def main():
    def print_main_menu():
        print("\nSelect an Option:")
        print("0 - Exit")
        print("1 - Phrase Query")
        print("2 - TF-IDF Search")
        print("3 - Cosine Similarity Search\n")

    def get_valid_input(prompt, valid_range):
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
        except ValueError:
            pass
        return None

    def get_query_input():
        return input("Enter your query: ").strip()

    def run_phrase_query():
        query = get_query_input()
        tokens = preprocess_text(query)
        checkToLoadDataFiles()

        normalized_phrase = " ".join(tokens.keys())
        results = search_phrase(positionalIndex.indexList, normalized_phrase)

        print("\nPhrase Match Results:")
        print("Format: { doc_id: [positions] }")
        print(results)

    def run_vector_search(method="tfidf"):
        query = get_query_input()
        tokens = preprocess_text(query)

        print("\nChoose a TF weighting scheme:")
        print("1 - Binary")
        print("2 - Raw Count")
        print("3 - Term Frequency")
        print("4 - Log Normalization")
        print("5 - Double Normalization\n")

        scheme = get_valid_input("Enter a number (1-5): ", range(1, 6))
        if scheme is None:
            print("Invalid input. Please enter a number between 1 and 5.")
            return

        checkToLoadDataFiles()

        tfidf_matrix = generate_tfidf_matrix(positionalIndex, len(documents), scheme)
        query_vec = query_vector(tokens, len(positionalIndex.indexList), positionalIndex)

        if method == "tfidf":
            top_docs = relevant_doc(query_vec, tfidf_matrix, len(documents))
            title = "TF-IDF Result"
        else:
            top_docs = cosine_sim(query_vec, tfidf_matrix, len(documents))
            title = "Cosine Similarity Result"

        print(f"\n{title}:")
        print("Top 5 documents:")
        for doc_id in top_docs:
            print(f"Document {doc_id + 1}")

    actions = {
        1: run_phrase_query,
        2: lambda: run_vector_search("tfidf"),
        3: lambda: run_vector_search("cosine")
    }

    while True:
        print_main_menu()
        choice = get_valid_input("Enter option: ", range(0, 4))

        if choice is None:
            print("Invalid input. Please enter a number between 0 and 3.")
            continue

        if choice == 0:
            print("Exiting program.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Unexpected error: No action defined.")

if __name__ == "__main__":
    main()
