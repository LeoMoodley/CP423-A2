# imports
from Q1 import PositionalIndex, text_preprocessor, phrase_finder
from Q2 import *
import os

# A dictionary that stores doc ID's in documents names keys
documents = {}

# Intializes postional index
positionalIndex: PositionalIndex = None

'''
Processes all files in the data directory by tokenizing their content and indexing the results into a positional inverted index.
'''
def createPositionalIndex():
    # Initialize a new positional inverted index
    inverted_index = PositionalIndex()

    # Retrieve all file names from the data directory
    file_names = os.listdir("./data/")
    # print(file_names)
    total_files = len(file_names)

    # counters for looping through files and document ID's
    current_index = 0
    doc_id = 1

    # While that loops through each file of the "data" directory
    while current_index < total_files:
        file_name = file_names[current_index]
        file_path = "./data/" + file_name

        try:
            # This tries to open and read the file, with UTF-8 encoding
            file = open(file_path, "r", encoding="utf-8", errors="replace")
            content = file.read()
            file.close()
        except Exception as e:
            # If reading fails, prints error and skips the next file
            print(f"Error reading {file_name}: {e}")
            current_index += 1
            continue
        
        # Preprocess the file contnt into tokens with positions
        tokens = text_preprocessor(content)
        
        # Converts the dictionary to list
        word_list = list(tokens.items())
        word_index = 0
        num_words = len(word_list)

        # Add each token and its poition ot the inverted index
        while word_index < num_words:
            word, positions = word_list[word_index]
            inverted_index.append_index(word, doc_id, positions)
            word_index += 1

        # Maps document ID to its file
        documents[doc_id] = file_name
        
        # Increments doc ID and move on to next file
        doc_id += 1
        current_index += 1

    return inverted_index


# Ensures the positional index data structure is only created once
def checkToLoadDataFiles():
    global positionalIndex
    if (positionalIndex == None):
        print("\nInitializing positional index...")
        positionalIndex = createPositionalIndex()

        print("Index creation complete.\n")



# Main function, handles the command-line interface
def main():
    # Function that displays main menu options
    def print_main_menu():
        print("\nSelect an Option:")
        print("0 - Exit")
        print("1 - Phrase Query")
        print("2 - TF-IDF Search")
        print("3 - Cosine Similarity Search\n")

    # Asks the user for input and checks if it's in valid range 
    def get_valid_input(prompt, valid_range):
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
        except ValueError:
            pass
        return None
    
    # Gets query string from user and gets rid of whitespace
    def get_query_input():
        return input("Enter your query: ").strip()

    # Handles the execution of the phrase query search
    def run_phrase_query():
        query = get_query_input()
        # print(f"Query Input : {query}")
        tokens = text_preprocessor(query)
        checkToLoadDataFiles()

        # Limit the number of terms in the query
        if len(tokens) > 5:
            print("Error: Phrase queries are limited to a maximum of 5 terms.")
            return

        # Normalize the query into a cleaned string
        normalized_phrase = " ".join(tokens.keys())
        results = phrase_finder(positionalIndex.indexList, normalized_phrase)

        print(f"results : {results}")
        print(f"tokens : {tokens}")
        print()
        print()

        # Count how many positions each doc has
        doc_hits = [(doc_id, len(positions)) for doc_id, positions in results.items()]

        # Sort by number of hits descending
        top_docs = sorted(doc_hits, key=lambda x: x[1], reverse=True)
        keys_string = ' '.join(tokens.keys())
        print(f"Documents with most '{keys_string}' term pairs:")
        for doc_id, count in top_docs:
            print(f"Doc ID: {doc_id} | File Name: {documents.get(doc_id, 'unknown')}")

    # Controls execution of TF-IDF and cosine similarity searches
    def run_vector_search(method="tfidf"):
        query = get_query_input()
        tokens = text_preprocessor(query)

        # Prompts user to select TF-weighting scheme
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

        # Generates TF-IDF matrix 
        tfidf_matrix = generate_tf_idf_matrix(positionalIndex, len(documents), scheme)
        # Create query vector
        query_vec = vector_query(tokens, len(positionalIndex.indexList), positionalIndex)

        # Chooses the appropriate ranking method
        if method == "tfidf":
            top_docs = top_5_relevant_docs(query_vec, tfidf_matrix, len(documents))
            title = "TF-IDF Result"
        else:
            top_docs = cosine_sims(query_vec, tfidf_matrix, len(documents))
            title = "Cosine Similarity Result"

        # Outputs top 5 most relevant documents
        print(f"\n{title}:")
        print(tfidf_matrix)
        print("Top 5 documents:")
        for doc_id in top_docs:
            file_name = documents.get(doc_id + 1, "Unknown")
            print(f"Doc_id: {doc_id + 1} | file_name: {file_name}")

    # Maps user choices to their corresponding action functions
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

# Starts program
if __name__ == "__main__":
    main()
