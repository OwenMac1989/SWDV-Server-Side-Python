#!/usr/bin/env python3

from statistics import median
from tokenize import Double


def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scoreList = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scoreList
        else:
            score = float(score)
            if score >= 0 and score <= 100:
                scoreList.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scoreList: list):
    totalScore: float = 0.0
    averageScore: float = 0.0
    # calculate average score
    for i in scoreList:
        totalScore += i
    averageScore = totalScore / len(scoreList)
    scoreList.sort(reverse = True)
    lowestScore = scoreList[(len(scoreList) - 1)]
    highestScore = scoreList[0]
    medianScore = median(scoreList)

                
    # format and display the result
    print()
    print("Score total:       ", round(totalScore, 2))
    print("Number of Scores:  ", len(scoreList))
    print("Average Score:     ", round(averageScore, 2)"%")
    print("Lowest Score:     ", round(lowestScore, 2)"%")
    print("Highest Score:     ", round(highestScore, 2)"%")
    print("Median Score:     ", round(medianScore, 2)"%")

def main():
    display_welcome()
    scorelist = get_scores()
    process_scores(scorelist)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


