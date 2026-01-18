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

    def __next__(self):
        try:
            line = self.lines[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return line


ft = FileTraversal("./test.md")

print(ft)

for line in ft:
    print(line)

print(list(ft))
