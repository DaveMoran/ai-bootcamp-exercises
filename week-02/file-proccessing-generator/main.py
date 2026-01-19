import re


class FileTraversal:

    def __init__(self, file):
        self.file = file
        self.lines = self.read_lines()

    def __iter__(self):
        return FileTraversalIterator(self.lines)

    def __repr__(self):
        return f"FileTraversal(file={self.file}, lines={len(self.lines)})"

    def read_lines(self):
        with open(self.file) as f:
            for line in f:
                yield line


class FileTraversalIterator:
    def __init__(self, lines):
        self.lines = lines
        self.idx = 0

    def __next__(self):
        try:
            line = next(self.lines)
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return line

    def __iter__(self):
        return self


ft = FileTraversal("./test.md")


def lines_starting_with_vowel(lines):
    for line in lines:
        if line[0].lower() in "aeiou":
            yield line


def lines_containing_keyword(lines, keyword):
    for line in lines:
        if keyword.lower() in line.lower():
            yield line


def strip_and_uppercase(lines):
    for line in lines:
        yield line.strip().upper()


def lines_with_numbers_extracted(lines):
    for line in lines:
        new_line = re.sub(r"\d+", "", line)
        yield new_line


result = lines_containing_keyword(lines_with_numbers_extracted(ft), "TwO")

for item in result:
    print(item)
