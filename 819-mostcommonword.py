#time complexity O(n), n is len(paragraph)
#space complexity O(n), n is len(paragraph)
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        newParagraph = paragraph.lower()
        mostFrequentWord = "" 
        currWord = ""
        wordMap = {}
        maxWord = 0
        
        for letter in newParagraph:
            if letter == " " or letter in string.punctuation:
                if currWord != "":
                    if currWord in banned:
                        currWord = ""
                        continue
                    if currWord in wordMap:
                        wordMap[currWord] += 1
                    else:
                        wordMap[currWord] = 1
                currWord = ""
            else:
                currWord += letter
                
        if currWord in wordMap:
            wordMap[currWord] += 1
        else:
            wordMap[currWord] = 1
            
        for word in wordMap:
            if word not in banned and wordMap[word] > maxWord:
                maxWord = wordMap[word]
                mostFrequentWord = word
        return mostFrequentWord
        