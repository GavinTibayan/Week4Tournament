#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
#Team Name
print("\t\tList the names of 6 teams")
print("Team 1:")
Team1 = input()
print("Team 2:")
Team2 = input()
print("Team 3:")
Team3 = input()
print("Team 4:")
Team4 = input()
print("Team 5:")
Team5 = input()
print("Team 6:")
Team6 = input()

#Wins
print("\t\tHow many wins?")
print(Team1)
Wins1 = int(input())
Points1 = int(Wins1 * 2)
#Losses
print("\t\tHow many losses?")
Losses1 = int(input())
#Ties
print("\t\tHow many ties?")
Ties1 = int(input())
Points2 = int(Ties1 * 1)
#Calculate
Points3 = int(Points1 + Points2)
print("Team name:",Team1,"wins:",Wins1,"Ties:",Ties1,"Losses:",Losses1,"Points:",Points3)
#Podium Calculation


#Podium
print("In 6th place is...", Number6)
print("\t\tpress enter to continue to the next lines")
input()
print("In 5th place is...", Number5)
input()
print("In 4th place is...", Number4)
input()
print("In 3rd place is...", Number3)
input()
print("In 2nd place is...", Number2)
input()
print("And the winner of this tournament is...", Number1)

