import zipfile
import zlib


wordFile = "F:\Projects\Python Projects\Zip-Pass-Breaker\word-corpus\words"

with zipfile.ZipFile("demo.zip", "r") as archive:
    # archive.printdir()
    first = archive.infolist()[0]

    print("Reading :", first.filename)
    with open(wordFile) as corpus:
        for line in corpus:

            try:
                word = line.strip().encode("ASCII")
                with archive.open(first, 'r', pwd=word) as member:
                    text = member.read()
                print("Password", word)
                # print(text)
                break
            except(UnicodeEncodeError,RuntimeError, zlib.error, zipfile.BadZipFile):
                pass
