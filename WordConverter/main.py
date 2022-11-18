import json
import jsonpickle
import beautifulWord
import beautifulWordsCollection


collection = beautifulWordsCollection.BeautifulWordsCollection()
count = 0
with open("words.txt", "r") as filestream:
    for line in filestream:
        currentline = line.split(":")
        #total = str(int(currentline[0]) + int(currentline[1]) + int(currentline [2])) + "\n"
        if(len(currentline) == 2):
            newWord = beautifulWord.BeautifulWord(
                currentline[0], currentline[1], [])
            collection.add(newWord)
            count = count + 1
        else:
            print("Not enough fields to create a word entry for entry " + str(count))
            print(currentline)
collection.save()
print("Processed " + str(count) + " words")
