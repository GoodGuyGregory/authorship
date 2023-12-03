import pandas as pd
import re

def readAusten():
# read in the files from Austen, divide paragraphs into an array of individual values.
    northanger = open('austen-northanger-abbey.txt', encoding="utf8").read().split('\n\n')
    for line in range(len(northanger)):
        northanger[line] = re.sub('\n',' ', northanger[line])
    print(northanger)

def main():
    print('Running')
    readAusten()



main()