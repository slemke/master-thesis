import random
import re


def read(text_file):
    """Reads a text file from disc.

    This function reads any text file from disc.

    Parameters
    ----------
    text_file : str
        A path to the text file

    Returns
    -------
    text
        The files content
    """
    f = open(text_file, "r")
    text = f.read().split('\n')
    f.close()
    return text


def get_code_snippets(paths):
    """Reads the java code snippets for the experiment.

    This function reads the code snippets for the experiment and shuffles them.

    Parameters
    ----------
    paths : list
        A list of paths to read the code snippets from

    Returns
    -------
    code_snippets
        A tuple containing the code snippets and labels
    """
    docs = []
    labels = []
    label_counter = 0

    for path in paths:
        text = read(path)
        for n in range(0, len(text)):
            docs.append(text[n])
            labels.append(label_counter)
        label_counter += 1

    return shuffle(docs, labels)


def get_code_names(paths):
    """Reads the java code names for the experiment.

    This function reads the code names for the experiment and shuffles them.

    Parameters
    ----------
    paths : list
        A list of paths to read the code names from

    Returns
    -------
    names
        A tuple containing the code names and labels
    """
    docs = []
    labels = []
    label_counter = 0

    for path in paths:
        text = read(path)
        for n in range(0, len(text)):
            token = [char for char in text[n]]
            docs.append(token)
            labels.append(label_counter)
        label_counter += 1
    return shuffle(docs, labels)


def get_code_name_tokens(paths):
    """Reads the java name tokens for the experiment.

    This function reads the name tokens for the experiment and shuffles them.

    Parameters
    ----------
    paths : list
        A list of paths to read the name tokens from

    Returns
    -------
    tokens
        A tuple containing the name tokens and labels
    """
    docs = []
    labels = []
    label_counter = 0

    for path in paths:
        text = read(path)
        for n in range(0, len(text)):
            token = re.sub(r'([A-Z])', r' \1', text[n]).split(' ')
            docs.append(token)
            labels.append(label_counter)
        label_counter += 1

    return shuffle(docs, labels)


def shuffle(docs, labels):
    """Shuffles two lists in parallel.

    This function shuffles to lists in parallel to shuffle
    the documents and labels for the experiment.

    Parameters
    ----------
    docs : list
        A list of documents
    labels : list
        A list of labels

    Returns
    -------
    docs
        A tuple containing the shuffled documents and labels
    """
    combined_list = list(zip(docs, labels))
    random.shuffle(combined_list)
    return zip(*combined_list)
