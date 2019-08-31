from readXML import getFileDetailsXml
import re
import os
fileDetailsXML = getFileDetailsXml(os.path.basename(__file__))
fileContent = open(".." + fileDetailsXML['InputPath'],"r")
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
fileContent = open(".." + fileDetailsXML['OutputPath'],"w+")
for i,v in wordCountDict.items():
	toBeWritten = str(i) + ":" + str(v) + "\n"
	fileContent.write(toBeWritten)
print (r"get the result @Data\result.txt")
fileContent.close()