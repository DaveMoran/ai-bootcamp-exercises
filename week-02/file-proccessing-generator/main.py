class FileTraversal:

    def __init__(self, file):
        self.file = file
        self.lines = []

    def __len__(self):
        return len(self.lines)

    def __repr__(self):
        return f"FileTraversal(file={self.file}, lines={len(self.lines)})"


ft = FileTraversal("../")

print(ft)
