# Language-Modeling
Pre-processed selected data from a given text to pad all sentences with start and end symbols/tokens, and replacing all words occurring in training data once with an UNK (unknown) token. Trained maximum-likelihood language models (unigram and bigram) and evaluated them on two test corpora to predict probability of the next word. Then calculated log probability and perplexity of sample sentences using the trained language models

first paste and run "number1.py" to process the files. then run "number2.py"

Paths:
In file "number1.py", change the paths for 'trainingfilepath' and 'testfilepath' to your respective path for any text file.
In file "number2.py", change the paths for 'trainpreprocessed', 'testpreprocessedpath' 'testbeforeunkpath' to your respective path for any text file.

Run number1.py in order to obtain the padded and preprocessed test and train files.

Run number2.py in order to obtain the solutions for part 2.

to see the pdf files, right click and select open with notepad.
