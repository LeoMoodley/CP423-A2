# CP423-A2
Due Date: June 28th, 2025 11:59 PM

# Creator
Leonardo Moodley

Student ID: 210337850

# Summary
The overall purpose of this project was to develop a Python program capable of handling phrase queries on a dataset 
and ranking the results using a TF-IDF algorithm. The process included data processing, building a positional index,
accepting user input, implementing phrase query logic, debugging the code, and executing various queries to retrieve relevant
results from the dataset.
# Summarization of each file
### Q1.py

This file contains the positional index data structure, a preprocessing function, and the functions required to handle phrase queries.
The positonal index supports adding and updating entries. For phrase queires, two helpe functions are used; verify_positional_prox which
identifies word postions within the same document, and a merge algorithm combines matching document IDs unto a single result list.

### Q2.py

This script includes functions for calculating Term Frequency (TF), TF-IDF scores, and cosine similarity. In Q2, matricies are always intially
all zeros before being given any values. The calculation of TF-IDF values and updating their matricies and the generation of query vector is done by two indiviudal functions. 
To compute TF-IDF relevance scores, the system performs a dot product between the query vector and the TF-IDF matrix. A separate function then identifies and returns the top 5 most relevant documents based on the highest TF-IDF scores.
The cosine_sim function works similarly but ranks the top 5 documents using cosine similarity scores instead of raw TF-IDF values.
Lastly, It's assumed that all Logarithmic Calculations use base 10.
### main.py

The main.py script is the entry point for a phrase and vector-based search engines. It utlilizes functions from Q1 (handles positional index and phrase queries) and Q2 (deals with TF-IDF and cosine similarity computations).

Positional Index Creation:
- Reads and tokenizes text files from the ./data/ directory
- Constructs a positional inverted index mapping words to their positions in each document
- Each document is assigned a unique document ID.

Main Functionality:
- A command-line interface lets users choose from three search options:
  1. Phrase Query Search,
  2. TF-IDF Search,
  3. Cosine Similarity Search

Phrase Query:
- Accepts a phrase from the user, preprocesses it, and searches the positional index for exact matches (words appearing consecutively in the same document).
- Returns results in the format: {docID: [positions]}.


TF-IDF & Cosine Similarity Search:
- User provides a query and selects a term frequency (TF) weighting scheme.
- A TF-IDF matrix is generated based on the chosen scheme.
- A query vector is constructed and compared with document vectors: TF-IDF search ranks based on dot product scores. Cosine similarity search ranks based on cosine similarity scores.
- Top 5 relevant documents are displayed based on the selected method.

Efficiency:
- The positional index is created once and reused in future queries.
# Steps to running the files
1. Run main.py
2. You will be asked which function you want to execute or exit the program. Choose a number:
     0 - Exit
     1 - Phrase Query
     2 - TF-IDF Search
     3 - Cosine Similarity Search
4. Thereupon, you'll be asked to input a query. So enter a query and press enter:
5. Then the phrase query will perform calulations and output an result. If TF-IDF or Cosine was pucked you will be asked to choose
   which weight scheme to utilize. So choose a number:
      1 - Binary
      2 - Raw Count
      3 - Term Frequency
      4 - Log Normalization
      5 - Double Normalization
7. You are done!
8. In case you run into errors, repeat steps 1-5

# Example of how to run the program
Select an Option:
0 - Exit
1 - Phrase Query
2 - TF-IDF Search
3 - Cosine Similarity Search

# Phrase Query 
- Enter option: 1
- Enter the query: Good Morning
- Initializing positional index...
Phrase Match Results:
Format: { doc_id: [positions] }
{96: [698, 699], 124: [950, 951]}

# TF-IDF Search
- Enter Option: 2
- Enter the query: Good Morning
Choose a TF weighting scheme:
1 - Binary
2 - Raw Count
3 - Term Frequency
4 - Log Normalization
5 - Double Normalization
- Enter a number (1-5)L 1
- Initializing positional index...
TF-IDF Result:
Top 5 documents:
Document 1
Document 2
Document 3
Document 5
Document 8

# Cosine Similarity Search
- Enter Option: 3
- Enter the query: Good Morning
Choose a TF weighting scheme:
1 - Binary
2 - Raw Count
3 - Term Frequency
4 - Log Normalization
5 - Double Normalization
- Enter a number (1-5): 1
Cosine Similarity Result:
Top 5 documents:
Document 82
Document 214
Document 142
Document 169
Document 67
