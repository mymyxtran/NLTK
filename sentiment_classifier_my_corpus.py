import nltk

# Adding my own corpus
mycorpus = nltk.corpus.reader.CategorizedPlaintextCorpusReader(
    r"/Users/mymytran/git/NLTK/my_corpus",
    r'(?!\.).*\.txt', 
    cat_pattern=r'(neg|pos)/.*',
    encoding="ascii") 

documents = [(list(mycorpus.words(fileid)), category)
              for category in mycorpus.categories()
              for fileid in mycorpus.fileids(category)]
              
# print(documents)

## print the categories which exists

# print ("Categorize : ", mycorpus.categories()) 
  
print ("\nNegative field : ", mycorpus.fileids(categories =['neg'])) # for all fileids print the negative ids
  
print ("\nPosiitve field : ", mycorpus.fileids(categories =['pos'] )) # for all fileids print the positive ids

# print(list(mycorpus.words()))

# random.shuffle(documents)

# # Define the feature extractor

# all_words = nltk.FreqDist(w.lower() for w in mycorpus.words())
# word_features = list(all_words)[:2000]

# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features

# # Train Naive Bayes classifier
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# # Test the classifier
# print(nltk.classify.accuracy(classifier, test_set))
