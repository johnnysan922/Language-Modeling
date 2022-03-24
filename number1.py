from collections import Counter


def removeElements(filename):
    lst = open(filename[:-4] + 'padded.txt',
               encoding="utf8").read().lower().split()
    k = 1
    counted = Counter(lst)
    with open(filename[:-4] + 'preprocessed.txt', 'x',
              encoding="utf8") as fileobject:
        # uses list comprehension to remove sparse words
        fileobject.writelines(
            str(el) + " " if counted[el] > k else ' <unk> ' for el in lst)
    return


def padSentence(filename):
    result = ""
    with open(filename, encoding="utf8") as fileobject:
        with open(filename[:-4] + 'padded.txt', 'x', encoding="utf8") as f:
            for line in fileobject:
                print(line.rstrip("\n") + " </s> ", file=f)
    return


def removeUnseenWords(testfile, trainingfile):
    traininglst = open(trainingfile[:-4] + 'preprocessed.txt',
                       'r',
                       encoding='utf8').read().lower().split()
    trainingcounted = Counter(traininglst)
    testlst = open(testfile[:-4] + 'padded.txt', 'r',
                   encoding='utf8').read().lower().split()
    testcounted = Counter(testlst)
    with open(testfile[:-4] + 'preprocessed.txt', 'x',
              encoding="utf8") as fileobject:
        # uses list comprehension to remove sparse words
        fileobject.writelines(
            str(el) + " " if trainingcounted[el] > 0 else ' <unk> '
            for el in testlst)  #
    return

trainingfilepath = 'C:\\Users\\johns\\code\\assignments\\cs381\\NLP\\hw1\\train-Spring2022.txt'
testfilepath = 'C:\\Users\\johns\\code\\assignments\\cs381\\NLP\\hw1\\test.txt'

padSentence(trainingfilepath)
removeElements(trainingfilepath)

padSentence(testfilepath)
removeUnseenWords(testfilepath, trainingfilepath)


