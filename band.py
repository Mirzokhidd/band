#bands

import filecmp 
import re
import numpy as np

def askForBands():
    numberOfBands = int(input("How many bands are there: "))
    bands = []
    scores = []
    bands2 = []
    total = 0
    number = 0
    for i in range(numberOfBands):
        ask = input("What is the band name for band " + str(i + 1) + ": ")
        votes = int(input("What is the number of votes for " + ask + ": "))
        two = ask + " " + str(votes)
        bands.append(ask)
        scores.append(votes)
        bands2.append(two)
        total += votes

    for i in range(numberOfBands):
        with open(str(bands[i]) + ".txt", "a") as x:
            x.write(str(bands[i]))
            i += 1

    def nestedFunction():
        choice = int(input("What do you want to do: \n 1. Full results \n 2. Total Number of votes \n 3. Top 3 \n 4. Bottom 3 \n 5. Average number of votes \n 6. Threshold\n")) 
        if choice == 1:
            for i in range(numberOfBands):
                with open(str(bands[i]) + ".txt", "r") as y:
                    print(bands2[i] + "\n")
            nestedFunction()
        elif choice == 2:
            print("\nTotal votes: " + str(total) + "\n")
            nestedFunction()
        elif choice == 3:
            top = sorted(zip(scores, bands), reverse=True)[0:3]
            print(top)
            nestedFunction()
        elif choice == 4:
            bottom = sorted(zip(scores, bands))[0:3]
            print(bottom)
            nestedFunction()
        elif choice == 5:
            print("\n Average votes: " + str(total / numberOfBands) + "\n")
            for i in range(numberOfBands):
                if scores[i] > (total / numberOfBands):
                    print("The band " + bands[i] + " scored more than average. They had " + str(scores[i]) + ", which is " + str(scores[i] - (total / numberOfBands)) + " more than the average.\n")
            nestedFunction()
        elif choice == 6:
            question = int(input("What threshold do you want: "))

            print("These bands are above that threshold: \n")
            for i in range(numberOfBands):
                if scores[i] > question:
                    print(bands[i] + " with the score of " + str(scores[i]) + "\n")

            print("These bands are below or the same value as the threshold: \n")
            for i in range(numberOfBands):
                if scores[i] <= question:
                    print(bands[i] + " with the score of " + str(scores[i]) + "\n")
            nestedFunction()
            
    
    nestedFunction()

askForBands()
    