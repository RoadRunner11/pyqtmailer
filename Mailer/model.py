class Model(object):
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
    def isValid(self, fileName):
        try:
            file = open(fileName, 'r')
            file.close()
            return True
        except:
            return False
    def setFilename(self, fileName):
        if self.isValid(fileName):
            self.fileName = fileName
            self.fileContents =""                
    def getFileName(self):
        return self.fileName
    def getFileContents(self):
        return self.fileContents
    def openfile(self, fileName):
        with open(fileName, "r") as f:
            return f.read()
    def readline(self, fileName):
        with open(fileName, "r") as f:
            for line in f.readlines():
                return line    
