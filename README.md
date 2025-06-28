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
- 0 - Exit
- 1 - Phrase Query
- 2 - TF-IDF Search
- 3 - Cosine Similarity Search

# Phrase Query 
- Enter option: 1
- Enter the query: Good Morning
- Initializing positional index...
- Index creation complete.

- results : {2: [66, 67], 44: [1150, 1151], 59: [4611, 4612], 80: [3204, 3205], 93: [613, 614], 96: [396, 397], -124: [950, 951], 131: [1557, 1558], 212: [3880, 3881], 219: [11, 12], 223: [2169, 2170], 249: [1118, 1119]}
- tokens : {'good': [1], 'morning': [2]}


- Documents with most 'good morning' term pairs:
Doc ID: 2 | File Name: 13chil.txt
Doc ID: 44 | File Name: bluebrd.txt
Doc ID: 59 | File Name: bulprint.txt
Doc ID: 80 | File Name: dskool.txt
Doc ID: 93 | File Name: fgoose.txt
Doc ID: 96 | File Name: flktrp.txt
Doc ID: 124 | File Name: hell4.txt
Doc ID: 131 | File Name: holmesbk.txt
Doc ID: 212 | File Name: solitary.txt
Doc ID: 219 | File Name: startrek.txt
Doc ID: 223 | File Name: taxnovel.txt
Doc ID: 249 | File Name: zombies.txt

# TF-IDF Search
- Enter Option: 2
- Enter the query: Good Morning
- Choose a TF weighting scheme:
- 1 - Binary
- 2 - Raw Count
- 3 - Term Frequency
- 4 - Log Normalization
- 5 - Double Normalization

- Enter a number (1-5)L 1
- Initializing positional index...

- TF-IDF Result:
[[1.79413936 1.09516935 1.16575043 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 2.09516935 2.09516935 2.09516935]]
- Top 5 documents:
- Doc_id: 1 | file_name: 100west.txt
- Doc_id: 2 | file_name: 13chil.txt
- Doc_id: 3 | file_name: 3gables.txt
- Doc_id: 5 | file_name: 3student.txt
- Doc_id: 8 | file_name: 5orange.txt

# Cosine Similarity Search
- Enter Option: 3
- Enter the query: Good Morning
- Choose a TF weighting scheme:
- 1 - Binary
- 2 - Raw Count
- 3 - Term Frequency
- 4 - Log Normalization
- 5 - Double Normalization
- Enter a number (1-5): 1

- Cosine Similarity Result:
[[1.79413936 1.09516935 1.16575043 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 2.09516935 2.09516935 2.09516935]]
- Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 214 | file_name: spider.txt
- Doc_id: 142 | file_name: kneeslapper.txt
- Doc_id: 169 | file_name: mtinder.txt
- Doc_id: 67 | file_name: clevdonk.txt

## Cosine Similarity Report Analysis:
The query utilized is 'Good Morning'

#Binary:
Pros:
- Easy to calculate

Cons:
- Couldn't find anything bad


Output:
- TF-IDF Result:
[[1.79413936 1.09516935 1.16575043 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 2.09516935 2.09516935 2.09516935]]
- Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 214 | file_name: spider.txt
- Doc_id: 142 | file_name: kneeslapper.txt
- Doc_id: 169 | file_name: mtinder.txt
- Doc_id: 67 | file_name: clevdonk.txt

# Raw Count
Pros:
- Easy to calculate


Cons:
- Couldn't find anything bad


Output:
- Cosine Similarity Result:
[[1.79413936 1.09516935 1.16575043 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 2.09516935 2.09516935 2.09516935]]
Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 190 | file_name: psf.txt
- Doc_id: 215 | file_name: spiders.txt
- Doc_id: 198 | file_name: roger1.txt
- Doc_id: 212 | file_name: solitary.txt
# Term Frequency
Pros:
- None


Cons:
- Takes too long to calculate


Output:
- Cosine Similarity Result:
[[0.00106477 0.00064995 0.00069184 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.00038422 0.00038422 0.00038422]]
Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 190 | file_name: psf.txt
- Doc_id: 215 | file_name: spiders.txt
- Doc_id: 198 | file_name: roger1.txt
- Doc_id: 212 | file_name: solitary.txt
# Log Normalization
Pros:
- Easy to calculate
  Values are normalized
Cons:
- Couldn't find anything bad


Output:
- Cosine Similarity Result:
[[0.54008976 0.32967883 0.35092585 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.63070882 0.63070882 0.63070882]]
- Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 2 | file_name: 13chil.txt
- Doc_id: 190 | file_name: psf.txt
- Doc_id: 59 | file_name: bulprint.txt
- Doc_id: 215 | file_name: spiders.txt
# Double Normalization
Pros:
- None


Cons:
- takes too long to calculate


Output:
- Cosine Similarity Result:
[[0.94192316 0.57496391 0.61201897 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 1.05523128 1.05523128 1.05523128]]
- Top 5 documents:
- Doc_id: 82 | file_name: elveshoe.txt
- Doc_id: 214 | file_name: spider.txt
- Doc_id: 169 | file_name: mtinder.txt
- Doc_id: 142 | file_name: kneeslapper.txt
- Doc_id: 67 | file_name: clevdonk.txt
