# SentimentClassifer

https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python
## How to Download **all** packages of NLTK on a mac:
### In the mac terminal:
1. Download and/or update pip "/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip"
2. Installing NLTK Data on a mac (aka Download nltk datasets): "sudo pip install -U nltk"
3. Run "python3"
### In the mac terminal while running the python3 interpreter:
#### How to Download **all** packages of NLTK on a mac:
4. "import nltk"
5. "nltk.download ('all')"


## Adding your own corpus while using NLTK
1. Import the required files (after you import a package you may import other files using relative referencing)
>>> import nltk 
>>> print(nltk.corpus.__file__) 
// The path to the __int__.py will be returned. For example, /Library/Python/3.7/site-packages/nltk/corpus/__init__.py
2. After completing 1, open the file (from terminal or finder)
>>> 
