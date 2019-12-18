import os

# get user downloads directory
dlDirPath = os.path.expanduser("~")
dlDirPath += str(os.path.sep + "Downloads")

print("dlDirPath: " + dlDirPath) # DEBUG

# get saved .html file
htmlFilePath = dlDirPath + str(os.path.sep + "ITPRoTV ProPortal.html")
htmlFile = open(htmlFilePath) # TODO: exception handling

for line in htmlFile:
    if "class=\"member-name\"" in line:
        print(line)