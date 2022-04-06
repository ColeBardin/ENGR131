import sys
import os
import re

def countComments(sourceFileName):
    # open sourceFileName, read contents into strCode
    f = open(sourceFileName)
    strCode = f.read()
    # strCode contains the .py file (sourceFileName) contents as a string
    hashComments = re.findall("^\s*#(.*?)$", strCode, re.DOTALL | re.MULTILINE)
    mlComments = re.findall("^\s*'''(.*?)'''", strCode, re.DOTALL | re.MULTILINE)

    nChars = 0
    nWords = 0
    nLines = 0
    comments = []

    for c in hashComments:
        # check hash comments one line at a time, add to comments list if non-empty
        if c != '' or c != ' ' or c != '  ' or c != '   ' or c != '    ':
            comments.append(c)

    for c in mlComments:
        # split c at '/n', add to comments if not empty
        for l in c.split('\n'):
            if l != '' or l != ' ' or l != '  ' or l != '   ' or l != '    ':
                comments.append(l)

        # count words, chars, non-empty lines in comments
    for c in comments:
        words = re.findall('\s*(\w*)\W', c)
        nWords += len(words)
        chars = ''.join(words)
        nChars += len(chars)
        # if chars is not empty, increment nLines
        if chars != '':
            nLines += 1
    return(nChars, nWords, nLines)


if __name__ == '__main__':
    sourceFileName = sys.argv[1]
    num_chars, num_words, num_lines = countComments(sourceFileName)
    print('{},{},{}'.format(num_chars, num_words, num_lines))
