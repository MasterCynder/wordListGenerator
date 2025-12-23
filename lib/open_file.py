class OpenFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        """Reads the entire file content."""
        with open(self.path, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def loadKeyWord(self):
        """Parses lines and commas into a keyword matrix, removing duplicates."""
        self.keyWordTab = []
        lines = self.content.split('\n')
        for line in lines:
            if line.strip():
                # Clean whitespace and filter duplicates on the same line
                variants = list(set([v.strip() for v in line.split(',') if v.strip()]))
                if variants:
                    self.keyWordTab.append(variants)

    def returnKeyWord(self):
        return self.keyWordTab
