from keras.preprocessing.text import Tokenizer


def get_sequences(docs, labels):
    """Returns a list of sequences for the provided documents and labels.

    This function tokenizes the documents and returns a tuple containing
    training and testing sequences with their labels that can be used
    for machine learning.

    Parameters
    ----------
    docs : list
        A list of documents to transform into sequences
    labels : list
        A list of labels describing the documents

    Returns
    -------
    sequences
        A tuple containing the training and testing sequences for the documents and labels
    """
    tokenizer = Tokenizer(oov_token=True, filters='')
    tokenizer.fit_on_texts(docs)
    encoded_docs = tokenizer.texts_to_sequences(docs)
    doc_sequences = split(encoded_docs)
    label_sequences = split(labels)
    return doc_sequences, label_sequences


def get_number_of_token(docs):
    """Returns the number of unique tokens in the documents.

    This function tokenizes the documents to build a word index.
    The length of the word index is then returned.

    Parameters
    ----------
    docs : list
        A list of documents

    Returns
    -------
    number_of_tokens
        The number of unique tokens over all documents
    """
    tokenizer = Tokenizer(oov_token=True, filters='')
    tokenizer.fit_on_texts(docs)
    return len(tokenizer.word_index)


def split(list_to_split):
    """Splits a list into two parts

    This function splits a list into two separate parts with the same length.

    Parameters
    ----------
    list_to_split : list
        The list to split in half

    Returns
    -------
    split_list
        A tuple containing the two parts of the input list
    """
    middle = int(len(list_to_split) / 2)
    return list_to_split[0:middle], list_to_split[middle:]
