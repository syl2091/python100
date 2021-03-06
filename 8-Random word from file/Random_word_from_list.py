import sys
import random

if sys.argv[1:]:
    filename = sys.argv[1]
else:
    filename = input("What is the name of the file? (extension included): ")

try:
    file = open(filename)
except(FileExistsError, IOError):
    print("文件不存在!")
    pass

# get number of lines
num_lines = sum(1 for line in file if line.rstrip())

# generate a random number between possible interval
random_line = random.randint(0, num_lines)

# re-iterate from first line
file.seek(0)

for i, line in enumerate(file):
    if i == random_line:
        print(line.rstrip())  # rstrip removes any trailing newlines :)
        break
