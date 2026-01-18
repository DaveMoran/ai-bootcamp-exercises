class FileTraversal:

    def __init__(self, directory):
        self.directory = directory
        self.files = []

    def __len__(self):
        return len(self.files)

    def __repr__(self):
        return f"FileTraversal(directory={self.directory}, files={len(self.files)})"


ft = FileTraversal("../")

print(ft)
