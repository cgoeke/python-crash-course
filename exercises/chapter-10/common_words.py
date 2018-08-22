# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.
filename = 'beyond_good_and_evil.txt'

try:
    with open(filename) as file_object:
        content = file_object.read()
        content = content.lower()
        content = str(content.count('the'))
        print("The word 'the' appears in " + filename + " " + content + " times.")
except FileNotFoundError:
    print("Sorry, cannot find " + filename + " :(")