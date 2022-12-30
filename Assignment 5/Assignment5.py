import math
import numpy as np
from numpy.linalg import norm


# calculate bag of words
def calc_bow(sentence):
    bow = {}
    words = sentence.split()
    for word in words:
        if word in bow:
            bow[word] += 1
        else:
            bow[word] = 1

    return bow


def calc_tf(bow):
    tf = {}
    for word in bow:
        tf[word] = round(bow[word] / sum(bow.values()), 2)
    return tf


def calc_idf(vocab, strings):
    idf = {}
    for word in vocab:
        count = 0
        for string in strings.values():
            if word in string.split():
                count += 1
        # print(word, count)
        idf[word] = round(math.log((3 / count), 10), 2)

    return idf


def calc_tfidf(tf, idf):
    tfidf = {}
    for word in tf:
        tfidf[word] = round(tf[word] * idf[word], 3)
    return tfidf


def get_vector_representation(bow, vocab):
    vector = []
    for word in vocab:
        if word in bow:
            vector.append(bow[word])
        else:
            vector.append(0)
    return vector


def get_cosine_similarity(vector1, vector2):
    cosine = np.dot(vector1, vector2)/(norm(vector1)*norm(vector2))
    return cosine


def main():
    strings = {'s1': 'sunshine state enjoy sunshine',
               's2': 'brown fox jump high, brown fox run',
               's3': 'sunshine state fox run fast'}
    # strings = {
    #     's1': 'This movie is very scary and long',
    #     's2': 'This movie is not scary and is slow',
    #     's3': 'This movie is spooky and good'
    # }

    vocab = []
    for string in strings.values():
        words = string.split()
        for word in words:
            if word not in vocab:
                vocab.append(word)

    # print(vocab)

    bowS1 = calc_bow(strings['s1'])
    bowS2 = calc_bow(strings['s2'])
    bowS3 = calc_bow(strings['s3'])

    tfS1 = calc_tf(bowS1)
    tfS2 = calc_tf(bowS2)
    tfS3 = calc_tf(bowS3)

    idf = calc_idf(vocab, strings)

    tfidfS1 = calc_tfidf(tfS1, idf)
    tfidfS2 = calc_tfidf(tfS2, idf)
    tfidfS3 = calc_tfidf(tfS3, idf)

    print('BOW of s1: ', bowS1)
    print('BOW of s2: ', bowS2)
    print('BOW of s3: ', bowS3, '\n')

    print('TF of s1: ', tfS1)
    print('TF of s2: ', tfS2)
    print('TF of s3: ', tfS3, '\n')

    print('IDF: ', idf, '\n')

    print('TF-IDF of s1: ', tfidfS1)
    print('TF-IDF of s2: ', tfidfS2)
    print('TF-IDF of s3: ', tfidfS3, '\n')

    vectorS1 = get_vector_representation(bowS1, vocab)
    vectorS3 = get_vector_representation(bowS3, vocab)

    print('Vector representation of s1: ', vectorS1)
    print('Vector representation of s3: ', vectorS3, '\n')

    cosine = get_cosine_similarity(vectorS1, vectorS3)
    print('Cosine similarity: ', cosine)


if __name__ == '__main__':
    main()
