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
1. Run a1_main.py
2. You will be asked how many queries you need to run. Select a number
3. Thereupon, you'll be asked to input a sentence, here's an example one:
     - Ontario is good and Quebec is massive
     - Press enter
4. Then you'll be asked to input operators. When inputting them, make sure that they're uppercase and commas seperate them.
    - Example
      - OR, OR, OR
5. You are done!
6. In case you run into errors, repeat steps 1-4

# Example of how to run the program
```
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\leomo\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\leomo\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt_tab to
[nltk_data]     C:\Users\leomo\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt_tab is already up-to-date!
How many queries do you need to run? 1

Query #1:
Please Input a Sentence: Ontario is good and Quebec is massive
Please Input Operations (comma-separated): OR, OR, OR

Expected preprocessed query: ontario OR good OR quebec OR massive

Processing query...

Reported Output:
Number of matched documents: 40
Minimum number of comparisons: 84
List of retrieved document names:
depth_1_List_of_Canadian_provinces_and_territories_by_historical_population.txt || ID: 1
depth_1_List_of_Canadian_provinces_and_territories_by_historical_population.txt || ID: 1
depth_2_1931_Canadian_census.txt || ID: 2
depth_2_1931_Canadian_census.txt || ID: 2
depth_2_Census_in_Canada.txt || ID: 3
depth_2_Census_in_Canada.txt || ID: 3
depth_2_First_Nations_in_Canada.txt || ID: 4
depth_2_First_Nations_in_Canada.txt || ID: 4
depth_2_First_Nations_in_Canada.txt || ID: 4
depth_2_Northwest_Territories.txt || ID: 5
depth_2_Northwest_Territories.txt || ID: 5
depth_2_Nunavut.txt || ID: 6
depth_2_Nunavut.txt || ID: 6
depth_3_1911_Canadian_census.txt || ID: 7
depth_3_1911_Canadian_census.txt || ID: 7
depth_3_2021_Canadian_census.txt || ID: 10
depth_3_2021_Canadian_census.txt || ID: 10
depth_3_Canada.txt || ID: 12
depth_3_Canada.txt || ID: 12
depth_3_Canada.txt || ID: 12
depth_3_Canadian_Confederation.txt || ID: 15
depth_3_Canadian_Confederation.txt || ID: 15
depth_3_Demographics_of_Canada.txt || ID: 17
depth_3_Demographics_of_Canada.txt || ID: 17
depth_3_First_Nations_(disambiguation).txt || ID: 18
depth_3_French_language.txt || ID: 19
depth_3_French_language.txt || ID: 19
depth_3_Indian_Canadians.txt || ID: 21
depth_3_Indian_Canadians.txt || ID: 21
depth_3_Indian_Canadians.txt || ID: 21
depth_3_Inuktitut_syllabics.txt || ID: 22
depth_3_Northwest_Territory.txt || ID: 26
depth_3_Northwest_Territory.txt || ID: 26
depth_3_Nunatsiavut.txt || ID: 27
depth_3_Nunavik.txt || ID: 28
depth_3_Statistics_Canada.txt || ID: 30
depth_3_Statistics_Canada.txt || ID: 30
depth_3_Statistics_Canada.txt || ID: 30
depth_3_Transfer_payment.txt || ID: 31
depth_3_Transfer_payment.txt || ID: 31
```

