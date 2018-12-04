Search Engine
Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.

github
https://github.com/IceTwilight/CS600/tree/master/final

directory structure
├── InvertFile.py -- a dictionary implemented by (compressed)Trie ├── SearchEngine.py -- main class ├── Tries.py -- (compressed)tries structure ├── file_link_map.json -- a map of html files and its' link ├── input -- the websites used to be the input of search engine ├── output -- the websites recommend by SearchEngine  

dependencies
python3.7
beatifulsoup (pip install bs4)
nltk (pip install nltk)

deploying
download or check out the project
cd ./final(in the 1st level of the directory)
python SearchEngine.py
