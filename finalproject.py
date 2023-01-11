# No required libraries needed (run on 3.8.3)
# Executed on Terminal for Mac (Command Line)
import time
import hashlib
import multiprocessing
from itertools import product

# String of characters (alphabet, number, special symbols)
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Add the MD5 hashed passwords from text file to hashList
file = open("hashes.txt", "r")
hashList = []
for line in file:
    hashList.append(line.strip())
file.close()

# Create all possible combination of passwords with a character
# concatenated in the front of it
def brute_force_attack(char):
    # Start with 0 to allow the designated character to be checked alone at first
    for length in range(0,9):
        # Create all possible combinations with string of characters and the length
        combinations = product(chars, repeat=length)
        for combination in combinations:
            word = char + ''.join(combination)
            # Generate the MD5 hash from the combination
            md5 = hashlib.md5(word.encode())
            # Check if the MD5 is in the hashList
            if md5.hexdigest() in hashList:
                # Output the time that it took in the terminal
                print(word, '\t', time.time() - starttime)
                # Remove from hash from the hashList
                hashList.remove(md5.hexdigest())

# Measure start time
starttime = time.time()

# Use multi-threading for multiple processor cores 
processes = []
for char in chars: # Each character is its own process
    task = multiprocessing.Process(target=brute_force_attack, args=(char))
    processes.append(task)
    task.start()
for process in processes:
    process.join()
