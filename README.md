# Natural Language Toolkit: Corpus Readers

Copyright (C) 2001-2020 NLTK Project
Author: Edward Loper <edloper@gmail.com>
URL: <http://nltk.org/>
For license information, see LICENSE.TXT

NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus files in a variety of formats.  These
functions can be used to read both the corpus files that are
distributed in the NLTK corpus package, and corpus files that are part
of external corpora.

## 1. How to Download **all** packages of NLTK on a mac:
### 1.1 In the mac terminal:
1. Download and/or update pip "/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip"
2. Installing NLTK Data on a mac (aka Download nltk datasets): "sudo pip install -U nltk"
3. Run "python3"
### 1.2 In the mac terminal while running the python3 interpreter:
#### How to Download **all** corpora of NLTK on a mac:
See http://www.nltk.org/nltk_data/ for a complete list of all corpora.
1. After importing the python3 interpreter, type the command "import nltk"
2. To install all corpora of NLTK, use "nltk.download ('all')" or "nltk.download('movies_reviews')" to download a corpus.
3. And you are done.

## 2. Adding your own corpus while using NLTK
1. Import the required files (after you import a package you may import other files using relative referencing)
>>> import nltk 
>>> print(nltk.corpus.__file__) 
// The path to the __int__.py will be returned. For example, /Library/Python/3.7/site-packages/nltk/corpus/__init__.py
2. After completing 1, open the file (from terminal or finder)

## 3. Corpus Reader Functions
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a filename, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``nltk.corpus.brown.words()``:

    >>> from nltk.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""

## 4. Creating a SentimentClassifier
https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python

