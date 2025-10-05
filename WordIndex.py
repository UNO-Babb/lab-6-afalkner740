#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNum = 0

  for line in textFile:
    lineNum += 1
    wordlist = line.split()
    for w in wordlist:
      w = w.lower()
      w = w.replace(",", "")
      w = w.replace(".","")
      w = w.replace("!","")

      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]
     
  for word in words:
    print(word, words[word])


if __name__ == '__main__':
  main()
