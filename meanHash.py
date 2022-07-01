import random as r
from statistics import mean
from time import perf_counter
import string
import sys
import math
import hashlib


def meanHash(password):

    hash = ""
    #Calculation of a unique seed for the password
    seed = sum((ord(char))**(password.find(char)+1) for char in password)
    r.seed(seed)
    #Alphabet builder 
    numbers = [str(i) for i in range(10)]
    numbers.extend(string.ascii_letters + string.punctuation)
    
    #Adding 120 random letters to the hash
    while len(hash) < 120:
        hash += r.choice(alphabet)
    return hash

def flagProcesser(argv):
    flag = argv[1]
    
    if(flag == "-f"):
        try:
            file = argv[2]
        except (NameError, IndexError):
            print("Missing parameter after flag.")
            exit()
        try:    
            with open(file, 'r', encoding='utf-8') as data:
                data2 = data.readlines()
                hashed_lines = list(map(meanHash, data2))
                joined_lines = ''.join(data2)
                hashed_joined_lines = meanHash(joined_lines)
                print("Hash of each line:")
                print(*hashed_lines, sep='\n')
                print('\n')
                print(f'Hash of all content wrapped: \n{hashed_joined_lines}')
                
        except FileNotFoundError:
            print("Missing file.")
            exit()
    if(flag == "-i"):
        try:
            text = argv[2]
        except (NameError, IndexError):
            print("Missing parameter after flag.")
            exit()
        print(meanHash(text))
    if(flag == '-e'):
        try:
            text = argv[2]
        except (NameError, IndexError):
            print("Missing parameter after flag.")
            exit()
        hashed_text = meanHash(text)
        entropy = len(hashed_text)*math.log2(len(string.ascii_letters + string.punctuation)) # 
        print(f'Input text: {text} \nhashed text: {hashed_text} \nentropy: {entropy}' )

if __name__ == '__main__':
    start = perf_counter()
    flagProcesser(sys.argv)
    end = perf_counter()
    print(end, start, end-start)
    
