import sys

class WriteFile:
    def __init__(self, path):
        self.path = path
        self.open()
        
    def write(self, string):
        self.file.write(string)
    
    def open(self):
        self.file = open(self.path, 'w')
    
    def close(self):
        self.file.close()