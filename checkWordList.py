count = 0

file_location = "F:\Projects\Python Projects\Zip-Pass-Breaker\word-corpus\words"
i = 0
with open(file_location) as wordList:
    for line in wordList:
        try :
            word = line.strip().encode("ASCII")
            # print(word.encode("ASCII"))
            count = count + 1
            i = i+1
        except (UnicodeEncodeError):
            print(line)
            break

print(count)

