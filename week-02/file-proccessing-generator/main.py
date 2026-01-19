import re


def read_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line


ft = read_lines("./test.md")


def lines_starting_with_vowel(lines):
    for line in lines:
        if line[0].lower() in "aeiou":
            yield line


def lines_containing_keyword(lines, keyword):
    for line in lines:
        if keyword.lower() in line:
            yield line


def strip_and_uppercase(lines):
    for line in lines:
        yield line.strip().upper()


def lines_with_numbers_extracted(lines):
    for line in lines:
        numbers = re.findall(r"\d+", line)
        yield numbers


result = lines_with_numbers_extracted(ft)

for item in result:
    print(item)
