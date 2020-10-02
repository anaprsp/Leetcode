#time complexity O(n), n is len(paragraph)
#space complexity O(n), n is len(paragraph)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        newParagraph = paragraph.lower()+" "
        numBanned = set(banned)
        mostFrequentWord = "" 
        currWord = ""
        wordMap = {}
        maxWord = 0
        
        for letter in newParagraph:
            if letter == " " or letter.isalpha() == False:
                if currWord != "":
                    if currWord in numBanned:
                        currWord = ""
                        continue
                    if currWord in wordMap:
                        wordMap[currWord] += 1
                    else:
                        wordMap[currWord] = 1
                currWord = ""
            else:
                currWord += letter
        
        for word in wordMap:
            if wordMap[word] > maxWord:
                maxWord = wordMap[word]
                mostFrequentWord = word
        return mostFrequentWord
        