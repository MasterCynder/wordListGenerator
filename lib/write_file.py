class WriteFile:
    def __init__(self, path):
        # Open in write mode ('w')
        self.file = open(path, 'w', encoding='utf-8')

    def write(self, string):
        self.file.write(string)

    def close(self):
        self.file.close()
