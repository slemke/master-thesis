# Code Classification

This repository contains the code for my master thesis. The basic idea was to 
classify source code with a common deep learning approach for text classification
to determine binary code quality. In `/data` you can find the code snippets. In
`/src/classifier/` you can find three different classifiers.

## Method classification
The first experiment was to classify methods in "good" or "bad" methods to see if 
the idea of automatic code classification with deep learning works. The sample
contains 2000 "good" and "bad" Java methods. The methods were classified by hand 
on criteria such as clean code or code smells. The code for the model was based 
on this [tensorflow tutorial](https://www.tensorflow.org/tutorials/text/text_classification_rnn)
an reached a total accuracy of `85%`.

```
64/500  [...................] - loss : 0.6444 - accuracy : 0.8438
128/500 [===>...............] - loss : 0.6397 - accuracy : 0.8672
192/500 [======>............] - loss : 0.6305 - accuracy : 0.8698
256/500 [=========>.........] - loss : 0.6325 - accuracy : 0.8164
320/500 [===========>.......] - loss : 0.6241 - accuracy : 0.8062
384/500 [==============>....] - loss : 0.6137 - accuracy : 0.8125
448/500 [================>..] - loss : 0.6070 - accuracy : 0.8170
500/500 [===================] - loss : 0.5935 - accuracy : 0.8220

Accuracy : 85.30%
``` 

## Name classification (Characters)
Good method names are important for clean code. The second experiment tried 
to distinguish between "good" and "bad" method names with the same approach 
for the method classification. The sample contains 5000 "good" and "bad" Java
method names. The methods were also classified by hand on clean code guidelines.
The same model was used for this experiment, but the characters of the names were
encoded instead of the tokens. The model reached a total accuracy of `52%`.

```
64/2500   [.................] - loss : 0.6932 - accuracy : 0.4688
128/2500  [>................] - loss : 0.6913 - accuracy : 0.5469
192/2500  [==>..............] - loss : 0.6920 - accuracy : 0.5365
256/2500  [===>.............] - loss : 0.6924 - accuracy : 0.5234
...
704/2500  [=====>...........] - loss : 0.6933 - accuracy : 0.4957
768/2500  [======>..........] - loss : 0.6935 - accuracy : 0.4922
832/2500  [======>..........] - loss : 0.6932 - accuracy : 0.4940
896/2500  [=======>.........] - loss : 0.6936 - accuracy : 0.4900
960/2500  [========>........] - loss : 0.6932 - accuracy : 0.4979
1024/2500 [=========>.......] - loss : 0.6932 - accuracy : 0.5000
1088/2500 [==========>......] - loss : 0.6931 - accuracy : 0.5000
...
2368/2500 [==============>..] - loss : 0.6925 - accuracy : 0.5000
2432/2500 [===============>.] - loss : 0.6925 - accuracy : 0.5021
2496/2500 [===============>.] - loss : 0.6925 - accuracy : 0.5016
2500/2500 [=================] - loss : 0.6925 - accuracy : 0.5012

Accuracy : 52.12%
```

## Name classification (Token)
The last experiment tried to improved the results of the second experiment.
Instead of characters the names where split into tokens. A name was split into
several token when a capital letter would appear in a name. So the name `getValueById`
would be the following list of tokens: `['get', 'value', 'by', 'id']`. Again, the same
model was used. The model reached a total accuracy of `47%`.

```
64/2500   [.................] - loss : 0.6982 - accuracy : 0.4688
320/2500  [===>.............] - loss : 0.6883 - accuracy : 0.5375
512/2500  [======>..........] - loss : 0.6845 - accuracy : 0.5469
...
1088/2500 [=======>.........] - loss : 0.6780 - accuracy : 0.5818
1280/2500 [========>........] - loss : 0.6767 - accuracy : 0.5836
1472/2500 [=========>.......] - loss : 0.6788 - accuracy : 0.5815
1664/2500 [==========>......] - loss : 0.6786 - accuracy : 0.5859
...
2112/2500 [===========>.....] - loss : 0.6777 - accuracy : 0.5819
2304/2500 [=============>...] - loss : 0.6782 - accuracy : 0.5773
2496/2500 [===============>.] - loss : 0.6782 - accuracy : 0.5761
2500/2500 [=================] - loss : 0.6781 - accuracy : 0.5768

Accuracy : 47.20%
```