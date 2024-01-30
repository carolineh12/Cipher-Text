##########################################
#Program 6
#Caroline Holland
#October 25, 2022
##########################################
#Subroutine
#Darri Stuber and https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python        
def caesar(plainText, sh): 
    cipherText=""
    #for every character in the text
    for x in plainText:
        #if the character is in the alphabet, change letter to number and shift the alphabet
        if x.isalpha():
            stayInAlphabet = ord(x) + sh
            #if the character is greater than the number assigned to Z, then subtract 26 to get to the right letter
            if stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            #convert the number back into letter
            finalLetter = chr(stayInAlphabet)
            #add the shifted letter to the empty string
            cipherText += finalLetter
        else:
           #if not a letter, just add the character to the empty string
            cipherText += x   
    return cipherText

def filter_out(shifted_cipher, library, sh):
    #split words from shifted cipher 
    split_cipher= shifted_cipher.split(" ")
    n=0
    for word in split_cipher:
        #see if the words in split cipher are in the library
        if word in library:
            n+=1
    #if more than half of the words are in the library, print
    if n > len(split_cipher)/2:
        print("Shift = {}: {}".format(sh, shifted_cipher))
        return split_cipher
        
######MAIN PROGRAM#########
from sys import stdin, stdout
file= open("cipher.txt")
#put into array
datalist= []
for i in file:
    datalist.append(i)
#https://codeparttime.com/python-file-close-method/#:~:text=Python%20File%20close%20%28%29%20Method%20%E2%80%93%20How%20to,terminates%20the%20execution%20of%20an%20open%20file.%20
file.close()
with open("words.txt", "r") as dictionary:
    words = dictionary.read().splitlines()
#normalize words
library= []
for word in words:
    for char in word:
        #get rid of non-letter characters
        if (not char.isalpha()):
            word= word.replace(char, "")
    #make uppercase
    word= word.upper()
    #add to library
    library.append(word)
#https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html#:~:text=Create%20a%20Timer%20in%20Python%3A%20Step-by-Step%20Guide%201,what%20we%E2%80%99ve%20learned%20to%20build%20a%20stopwatch.%20
import time
start= time.time()
for line in datalist:
    print("Ciphertext: " + line)
    #shift each line in datalist 25 times
    for i in range(1, 26):
        #call subroutine
        new= caesar(line, i)
        #call subroutine
        filters= filter_out(new, library, i)
end= time.time()
#Sofia Whelchel; subtract start and end time to get the final time it took to do all shifts
print("Process took " + str(end-start) + " s")













    
