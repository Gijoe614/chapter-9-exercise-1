wordList = open('words.txt')

def words(word):
    wordCount = 0
    lineCount = 0
    for word in wordList:
        if len(word) > 20:
            print word.rstrip('\r\n')
            wordCount += 1
        lineCount += 1
    percent  = (float(wordCount) / float(lineCount)) * 100.0

words(wordList)
