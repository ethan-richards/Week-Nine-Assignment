import string

def sortletters(word):
    word = word.lower()
    listWord = list(word)
    listWord.sort()
    sortedWord = "".join(listWord)
    return sortedWord

def createDict(fileName,dictionary):
    #openfile
    fileHandle = open(fileName, "r")
    #read a  line 
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        word = line.lower()
        if word[0] == 'v':
            sortedWord = sortletters(word)
            dictionary[sortedWord] = word
    fileHandle.close()   


def findAnagram(fileName, dictionary):
    fileHandle = open(fileName,"r")
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        quizword = line.lower()
        print (quizword, dictionary[sortletters(quizword)])
    fileHandle.close()
    
    
def main():
    aDict = {}
    fileName = "wordList.txt"
    quizListName = "quizwords.txt"
    createDict(fileName, aDict)
    findAnagram(quizListName,aDict)

main()