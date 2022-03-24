# Language-Modeling
Pre-processed selected data from a given text to pad all sentences with start and end symbols/tokens, and replacing all words occurring in training data once with an UNK (unknown) token. Trained maximum-likelihood language models (unigram and bigram) and evaluated them on two test corpora to predict probability of the next word. Then calculated log probability and perplexity of sample sentences using the trained language models