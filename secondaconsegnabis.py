import linecache
import logging

from gensim import corpora

from primaconsegna import getfromgoogle, NUMERORISULTATI


__author__ = 'Fundor333'

LEXICONNAME = "./out/out.txt"
DICTIONARYNAME = './out/deerwester.dict'


def readlexicon():
    return linecache.getline(LEXICONNAME, 0)


def makedictionary(listfilename):
    documents = []
    try:
        fistline = linecache.getline(LEXICONNAME, 0)
    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)

    for i in range(0, int(fistline)):
        filein = open(".out/" + i + ".txt")
    for line in filein:
        documents.append(line)

    spamword = open("spamword.teo")
    stoplist = None
    for line in spamword:
        stoplist = set(line.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    all_tokens = sum(texts, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once] for text in texts]
    dictionary = corpora.Dictionary(texts)
    dictionary.save(DICTIONARYNAME)  # store the dictionary, for future reference
    return dictionary


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
