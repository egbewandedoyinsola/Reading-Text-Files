# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
# put this comment after
# openfile = open("./story.txt", "r") this or the line immediately after
# will open the file.

def read_file_content(filename):
    # [assignment] Add your code here
    # reading the file

    with open("./story.txt", "r") as open_file:
        read_file = open_file.read()
    return read_file

    # return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # individual words/ split_text =text.split()
    individual_words = text.split()
    # print(individual_words)
    count = {}
    for i in individual_words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

    # return {"as": 10, "would": 20}
print(count_words())
