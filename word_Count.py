import re
fileContent = open(r"Data\test.txt","r")
data = fileContent.readlines()
fileContent.close()
#print(data)
data = data[0]
regWord = r"[\s.?!]+"
wordList = re.split(regWord, data)
wordList.remove('')
#print (wordList)
wordCountDict = {}
for w in wordList:
	if w not in wordCountDict:
		wordCountDict[w] = 1
	else:
		wordCountDict[w] = wordCountDict[w] + 1
#print (wordCountDict)
fileContent = open(r"Data\result.txt","w+")
for i,v in wordCountDict.items():
	toBeWritten = str(i) + ":" + str(v) + "\n"
	fileContent.write(toBeWritten)
print (r"get the result @Data\result.txt")
fileContent.close()