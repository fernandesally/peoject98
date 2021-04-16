def swapFileData():
 filedata=open("sample1.txt")
 filedata=open("sample2.txt")
    #print(filedata.read())
    lines=filedata.readlines()
    for i in lines:
        print(i)
    name="this is code.py"
    print(name.split())    

swapFileData()

def countwords():
    file=open("sample1.txt")
    numberofwords=0
    lines=file.readlines()
    for i in lines:
        word=i.split()
        numberofwords=numberofwords+len(word)
    print(numberofwords)

countwords()