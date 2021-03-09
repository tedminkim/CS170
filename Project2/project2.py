import csv 
import math 
from os import path
import os.path 
from array import *

#def featureSearch(data):
    #currentSetOfFeatures = []
    #for i in range(len(data, 2) - 1):
        

def main():
    userInput = ""
    print("Welcome to Ted Kim's Feature Selection Algorithm!")
    fileInput = input("Type in the name of the file to test: ")
    while not path.exists(fileInput):
        print("CRINGE!! THAT FILE ISN'T REAL.")
        fileInput = input("Type in the name of the file to test:")


    print("Wow! Thanks for inputting the file name: " + fileInput + "! We'll doing something about it.")
    while userInput != '1' and userInput != '2':
        print("Type the number of the algorithm you want to run.")
        print("1) Foward Selection")
        print("2) Backward Elimination")
        userInput = input()
        if userInput == '1':
            print("This is going to do forward selection")
        elif userInput == '2':
            print("This is going to do backward elimination")
        else:
            print("Yo you didn't even TRY to do a correct input.")


main()