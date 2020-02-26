import sys

class OpenFile:
    def __init__(self, path):
        self.path = path
        self.open()

    def open(self):
        self.file = open(self.path, 'r')

    def read(self):
        self.content = self.file.read()

    def loadKeyWord(self):
        self.keyWordTab = []
        lines = self.content.split('\n')
        for line in lines:
            self.keyWordTab.append(line.split(','))

    def returnKeyWord(self):
        return self.keyWordTab
