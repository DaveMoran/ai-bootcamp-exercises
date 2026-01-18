class FileTraversal:

    def __init__(self, file):
        self.file = file
        self.file_text = self.load_file()
        self.lines = str.splitlines(self.file_text)

    def __getitem__(self, i):
        return self.lines[i]

    def __len__(self):
        return len(self.lines)

    def __repr__(self):
        return f"FileTraversal(file={self.file}, lines={len(self.lines)})"

    def load_file(self):
        file_text = open(self.file)
        return file_text.read()


ft = FileTraversal("./test.md")

ft_iter = iter(ft)

print(ft_iter)

print(next(ft_iter))
print(next(ft_iter))
print(next(ft_iter))
print(next(ft_iter))
print(next(ft_iter))
print(next(ft_iter))
