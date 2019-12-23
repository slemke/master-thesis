import os

from keras.models import Sequential
from keras.layers import Dense, Bidirectional
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from preprocessing.file import get_code_name_tokens
from preprocessing.sequences import get_sequences
from preprocessing.sequences import get_number_of_token

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

FILES = [
    '../../data/names/clean.txt',
    '../../data/names/not_clean.txt'
]

# get tokens and labels
docs, labels = get_code_name_tokens(FILES)

# obtain training and test sequences
(x_train, x_test), (y_train, y_test) = get_sequences(docs, labels)

# truncate and pad input sequences
x_train = sequence.pad_sequences(x_train)
x_test = sequence.pad_sequences(x_test, maxlen=len(x_train[1]))

# create the model
model = Sequential()
model.add(Embedding(get_number_of_token(docs), 64, input_length=len(x_train[1])))
model.add(Bidirectional(LSTM(64)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model
model.fit(x_train, y_train, epochs=3, batch_size=64)

# Final evaluation of the model
scores = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))
