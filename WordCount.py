#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  text = input("Would you like to use gettysberg or fish txt? (1 or 2): ")
  if text == "1":
    filename = "gettysberg.txt"
    with open (filename, 'r') as textFile:
      linecount = 0
      wordcount = 0
      lettercount = 0

      for line in textFile:
        linecount += 1
        words = line.split()

        for w in words:
          wordcount += 1
          w = w.lower()
          w = w.replace("," ,"")
          w = w.replace(".","")
          for char in w:
            if char.isalpha():
              lettercount += 1

  elif text == "2":
    filename = "fish.txt"
    with open (filename, 'r') as textFile:
      linecount = 0
      wordcount = 0
      lettercount = 0

      for line in textFile:
        linecount += 1
        words = line.split()

        for w in words:
          wordcount += 1
          w = w.lower()
          w = w.replace(",", "")
          w = w.replace(".","")
          for char in w:
            if char.isalpha():
              lettercount += 1
  else:
    print("Invalid choice!")
    return
      
    #print(line)
  print("Lines:", linecount)
  print("Words:", wordcount)
  print("Letters:", lettercount)

if __name__ == '__main__':
  main()
