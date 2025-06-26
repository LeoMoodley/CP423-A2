# FIX THIS LATER
# CP423-A2
Due Date: May 31st, 2025 11:59 PM

# Creator
Leonardo Moodley

Student ID: 210337850

# Summary
The main theme of the project was to use the programs to see queries being ran on Canadian Provinces on Wikipedia. This was done
by creating the Index data structure, accepting input from the user, then using the operations 'AND', 'OR', and "NOT' Operations
for the queries and doing error handling to make sure the input was correct, then finally running the queries and returning the data.
# Summarization of each file
### a1_part1.py

This part contains code that web scrape then indexing the content from Canadian Provinces Historical Data Wikpedia page and stores them in the output folder.

### a1_part2.py

This script builds an inverted index from all .txt files in the output directory by preprocessing the text (lowercasing, removing stopwords/punctuation, and tokenizing). Each word is mapped to the files it appears in, using a set of (incorrectly) assigned "doc counters" based on token order rather than actual document IDs. It prints the resulting index, showing which words appear in which documents.

### a1_part3.py

This script processes boolean queries (AND, OR, NOT) over an inverted index to return matching document IDs and count comparisons used in the evaluation.

Functions:
1. is_valid_query_format(raw_query: str) -> bool
  Purpose: Checks if a user query is in a valid format.
  Returns: True if the query is valid. False with an error message otherwise.

2. process_query(query: str, inverted_index: InvertedIndex, totaldoc_counter: int)
   Purpose: Parses and evaluates the query using the inverted index and total number of documents.
   Returns: A list of document IDs that match the query. The number of comparisons made during evaluation.

### a1_main.py

This is the main script that does the following:
  - Builds an inverted index from text files in the output/ folder.

  - Accepts user queries using words and boolean operators (AND, OR, NOT).
  
  - Processes those queries and returns:
  
    - The number of matching documents.
  
    - How many comparisons were needed.
  
    - The names of the documents that matched.


Main Program (__main__):

- Asks the user how many queries they want to run.

- For each query:

    - Gets a sentence and a list of operators.

    - Constructs a full query using the cleaned words and operators.

    - Checks if the query is valid.

    - Builds the inverted index (if not already done).

    - Runs the query and prints the matching documents and some stats.



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

