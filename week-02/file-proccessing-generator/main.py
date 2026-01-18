class FileTraversal:

    def __init__(self, file):
        self.file = file
        self.file_text = self.load_file()
        self.lines = str.splitlines(self.file_text)

    def __iter__(self):
        return FileTraversalIterator(self.lines)

    def __repr__(self):
        return f"FileTraversal(file={self.file}, lines={len(self.lines)})"

    def load_file(self):
        file_text = open(self.file)
        return file_text.read()


class FileTraversalIterator:
    def __init__(self, lines):
        self.lines = lines
        self.idx = 0


ft = FileTraversal("./test.md")

list(ft)
