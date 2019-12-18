import os
from HTMLParser import HTMLParser
import datetime

# https://stackoverflow.com/questions/11804148/parsing-html-to-get-text-inside-an-element
class soHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.HTMLDATA = []
    def handle_data(self, data):
        self.HTMLDATA.append(data)
    def clean(self):
        self.HTMLDATA = []

# get user downloads directory
dlDirPath = os.path.expanduser("~")
dlDirPath += str(os.path.sep + "Downloads")

# get saved .html file
htmlFilePath = dlDirPath + str(os.path.sep + "ITPRoTV ProPortal.html")
htmlFile = open(htmlFilePath) # TODO: exception handling

# parse .html file
parser = soHTMLParser()

for line in htmlFile:
    parser.feed(line)

data = parser.HTMLDATA

# parse data
# dataFile = open('data-file.txt', 'w')
lineCounter = 0
startFlag = 59
endFlag = "All Courses"
skipVals = ["Activity", "Created with Sketch."]
dataCounter = 0
accountName = ""
lastLogin = ""
nameLoginList = []

for datum in data:
    lineCounter = lineCounter + 1
    if (datum == endFlag):
        break
    elif (lineCounter >= startFlag and not datum in skipVals):
        dataCounter = dataCounter + 1
        if (dataCounter == 1):
            accountName = datum.rstrip()
        if (dataCounter == 3):
            lastLogin = datum.rstrip()
            date = datetime.datetime(2000, 1, 1) # represent no login since invited
            if (not lastLogin[12:-6] == ''):
                date = datetime.datetime(int(lastLogin[12:-6]), int(lastLogin[17:-3]), int(lastLogin[-2:]))
            nameLoginList.append([date.__str__(), accountName])
            dataCounter = 0

nameLoginList.sort(key=lambda x: x[0])
        
for item in nameLoginList:
    # dataFile.write(str(item) + "\n")
    print(item)

# dataFile.close()