import os
from HTMLParser import HTMLParser
import re
import datetime

rundate = datetime.datetime.now().strftime("%m-%d-%y")

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

# create/open file
dataFile = open(str(dlDirPath + os.path.sep + 'itprotv-status-' + rundate + '.txt'), 'w')

# write file header
dataFile.write("ITProTV Status(" + rundate + ")\n")

# parse data
endFlag = "All Courses"
parseFlag = False
startFlag = "Last Login"
countRegEx = "\d{2} Available"
skipVals = ["Activity", "Created with Sketch."]
dataCounter = 0
accountName = ""
lastLogin = ""
unusedLoginList = []
usedLoginList = []

for datum in data:
    if (re.search(countRegEx, datum)):
        dataFile.write(re.search(countRegEx, datum).group() + "\n")
    if (datum == endFlag):
        break
    elif (parseFlag and not datum in skipVals):
        dataCounter = dataCounter + 1
        if (dataCounter == 1):
            accountName = datum.rstrip()
        if (dataCounter == 3):
            lastLogin = datum.rstrip()
            if (not lastLogin == ''):
                date = datetime.datetime(int(lastLogin[:4]), int(lastLogin[5:-3]), int(lastLogin[-2:]))
                usedLoginList.append([date, accountName])
            else:
                unusedLoginList.append(accountName)
            dataCounter = 0
    elif (datum == startFlag):
        parseFlag = True

# sort parsed data
usedLoginList.sort(key=lambda x: x[0])
        
# output to file
dataFile.write("\nUnused:\n")
for item in unusedLoginList:
    dataFile.write(item + "\n")

dataFile.write("\nUsed:\n")
for item in usedLoginList:
    dataFile.write(item[0].strftime("%x") + " " + item[1] + "\n")

dataFile.close()