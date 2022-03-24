import math
from collections import Counter
from itertools import islice

# change these paths to your respective paths
trainpreprocessedpath = 'C:\\Users\\johns\\code\\assignments\\cs381\\NLP\\hw1\\train-Spring2022preprocessed.txt'
testpreprocessedpath = "C:\\Users\\johns\\code\\assignments\\cs381\\NLP\\hw1\\testpreprocessed.txt"

traincorpus = open(trainpreprocessedpath, encoding="utf8").read().split()
traincount = Counter(traincorpus)
testcorpus = open(testpreprocessedpath, encoding="utf8").read().split()
testcount = Counter(testcorpus)
bigramtraincount = Counter(zip(traincorpus, islice(traincorpus, 1, None)))
bigramtestcount = Counter(zip(testcorpus, islice(testcorpus, 1, None)))

# change this path to your respective paths
testbeforeunkpath = 'C:\\Users\\johns\code\\assignments\\cs381\\NLP\\hw1\\testpadded.txt'

testcorpus2=open(testbeforeunkpath, encoding="utf8").read().split()
testcount2 = Counter(testcorpus2)

# question 1
print("Question 1: ")
print("Number of word types in training corpus: " + str(len(traincount)))
# question 2
print("Question 2:")
print("Number of word tokens in training corpus: " + str(sum(traincount.values())))
# question 3
print("Question 3: ")

percentagetypes = testcount2["</s>"] / sum(testcount2.values()) * 100
percentagetokens =traincount["<unk>"] /sum(traincount.values())  * 100
print(
    "Percentage of word types in the test corpus that did not occur in training: "
    + str(percentagetypes)
    + "%"
)
print(
    "Percentage of word tokens in the test corpus that did not occur in training: "
    + str(percentagetokens)
    + "%"
)
# question 4
print("Question 4: ")
uniquebigramtypecounter = 0
for el in bigramtestcount:
    if bigramtraincount[el] == 0:
        uniquebigramtypecounter += 1
percentageuniquebigramtypecounter = uniquebigramtypecounter / len(bigramtestcount) * 100
print(
    "Percentage of bigram types that did not occur in training: "
    + str(percentageuniquebigramtypecounter)
)
uniquebigramtokencounter = 0
for el in bigramtestcount:
    if bigramtraincount[el] == 0:
        uniquebigramtokencounter += bigramtestcount[el]
percentageuniquebigramtokencounter = (
        uniquebigramtokencounter / sum(bigramtestcount.values()) * 100
)
print(
    "Percentage of bigram tokens that did not occur in training: "
    + str(percentageuniquebigramtokencounter)
)

# question 5
print("Question 5: ")
input = "I look forward to hearing your reply ."

input = input.lower() + " </s>"

inputsplit = input.split()
inputsplit = ["<unk>" if traincount[i] == 0 else i for i in inputsplit]

unilogprob = 0
for el in inputsplit:
    unilogprob += math.log2(traincount[el] / sum(traincount.values()))
    print(
        "Log probability of "
        + el
        + " : "
        + str(math.log2(traincount[el] / sum(traincount.values())))
    )
print(
    "Unigram log probability of input: "
    + str(unilogprob)
    + " (sum of individual log probabilities)"
    + "\n"
)

input2 = " I look forward to hearing your reply ."
input2 = '<s>' + input2.lower() + " </s>"
inputsplit2 = input2.split()
inputsplit2 = ["<s>" if traincount[i] == 0 else i for i in inputsplit2]
bigraminputsplit = list(zip(inputsplit2, inputsplit2[1:]))
bilogprob = 0
for el in bigraminputsplit:
    if (bigramtraincount[el]) == 0:
        bilogprob = "undefined"
        print("Log probability of " + el[0] + " " + el[1] + " : undefined")

    else:
        if (
                bilogprob != "undefined"
        ):
            bilogprob += math.log2(bigramtraincount[el] / traincount[el[0]])
        print(
            "Log probability of "
            + el[0]
            + " "
            + el[1]
            + " : "
            + str(math.log2(bigramtraincount[el] / traincount[el[0]]))
        )
print(
    "Bigram log probability of input: "
    + str(bilogprob)
    + " (sum of individual log probabilities)"
    + "\n"
)
addonebilogprob = 0

addonebiloginputsplit = zip(inputsplit2, inputsplit2[1:])
for el in addonebiloginputsplit:
    addonebilogprob += math.log2(
        (bigramtraincount[el] + 1) / (traincount[el[0]] + len(traincount))
    )
    print(
        "Add-one Log probability of "
        + el[0]
        + " "
        + el[1]
        + " : "
        + str(
            math.log2(
                (bigramtraincount[el] + 1) / (traincount[el[0]] + len(traincount))
            )
        )
    )
print(
    "Add-one Bigram log probability of input: "
    + str(addonebilogprob)
    + " (sum of individual log probabilities)"
    + "\n"
)
# question 6
print("Question 6: ")

avgunilogprob = 0
avgbilogprob = 0
avgaddonebilogprob = 0
if unilogprob != "undefined":
    avgunilogprob = unilogprob / len(inputsplit)
else:
    avgunilogprob = "undefined"
if bilogprob != "undefined":
    avgbilogprob = bilogprob / len(inputsplit2)
else:
    avgbilogprob = "undefined"
avgaddonebilogprob = addonebilogprob / len(inputsplit2)
if avgunilogprob != "undefined":
    print(
        "perplexity of sentence under unigram model: "
        + str(math.pow(2, -1 * avgunilogprob))
    )
else:
    print("perplexity of sentence under unigram model is undefined")
if avgbilogprob != "undefined":
    print(
        "perplexity of sentence under bigram model: "
        + str(math.pow(2, -1 * avgbilogprob))
    )
else:
    print("perplexity of sentence under bigram model is undefined")
print(
    "perplexity of sentence under add-one bigram model: "
    + str(math.pow(2, -1 * avgaddonebilogprob))
)
# question 7
print("Question 7: ")

testunilogprob = 0
for el in testcorpus:
    testunilogprob += math.log2(traincount[el] / sum(traincount.values()))


testbilogprob = 0
testbigraminputsplit = list(zip(testcorpus, islice(testcorpus, 1, None)))
for el in testbigraminputsplit:
    if (bigramtraincount[el]) == 0:
        testbilogprob = "undefined"

    else:
        if testbilogprob != "undefined":
            testbilogprob += math.log2(bigramtraincount[el] / traincount[el[0]])


testaddonebilogprob = 0

testaddonebiloginputsplit = list(zip(testcorpus, islice(testcorpus, 1, None)))
for el in testaddonebiloginputsplit:
    testaddonebilogprob += math.log2(
        (bigramtraincount[el] + 1) / (traincount[el[0]] + len(traincount))
    )




testavgunilogprob = 0
testavgbilogprob = 0
testavgaddonebilogprob = 0
if testunilogprob != "undefined":
    testavgunilogprob = testunilogprob / sum(testcount.values())
else:
    testavgunilogprob = "undefined"
if testbilogprob != "undefined":
    testavgbilogprob = testbilogprob / sum(testcount.values())
else:
    testavgbilogprob = "undefined"
testavgaddonebilogprob = testaddonebilogprob / sum(testcount.values())
if testavgunilogprob != "undefined":
    print(
        "perplexity of test under unigram model: "
        + str(math.pow(2, -1 * testavgunilogprob))
    )
else:
    print("perplexity of test under unigram model is undefined")
if testavgbilogprob != "undefined":
    print(
        "perplexity of test under unigram model: "
        + str(math.pow(2, -1 * testavgbilogprob))
    )
else:
    print("perplexity of test under unigram model is undefined")
print(
    "perplexity of test under add-one bigram model: "
    + str(math.pow(2, -1 * testavgaddonebilogprob))
)