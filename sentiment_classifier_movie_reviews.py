## read more about *Imports*: Multi-Line and Absolute/Relative https://www.python.org/dev/peps/pep-0328/

# Load and prepare the dataset
import nltk
from nltk.corpus import movie_reviews
import random

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Define the feature extractor
# define a feature for each word, indicating whether the document contains that word

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# Limit the number of most frequent words to 2000
# --> Constructing a list of the 2000 most frequent words
word_features = list(all_words)[:2000]

def document_features(document):
    # Create a set of all words, since checking a set for the frequency of a word
    # is much faster than checking a list for the frequency of a word
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# Train Naive Bayes classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Test the classifier, the line prints the accuracy
print("\nThe classifier was able to achieve", nltk.classify.accuracy(classifier, test_set), "in accuracy.")

# Show the most important features as interpreted by Naive Bayes
classifier.show_most_informative_features(5)

#Most Informative Features
    #   contains(winslet) = True              pos : neg    =      8.4 : 1.0
    #  contains(illogical) = True              neg : pos    =      7.6 : 1.0
    #   contains(captures) = True              pos : neg    =      7.0 : 1.0
    #     contains(turkey) = True              neg : pos    =      6.5 : 1.0
    #     contains(doubts) = True              pos : neg    =      5.8 : 1.0