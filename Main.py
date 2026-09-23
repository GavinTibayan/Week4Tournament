#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################
from idlelib.query import HelpSource

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
print(Team2)
Wins2 = int(input())
print(Team3)
Wins3 = int(input())
print(Team4)
Wins4 = int(input())
print(Team5)
Wins5 = int(input())
print(Team6)
Wins6 = int(input())
Points1 = int(Wins1 * 2)
Points2 = int(Wins2 * 2)
Points3 = int(Wins3 * 2)
Points4 = int(Wins4 * 2)
Points5 = int(Wins5 * 2)
Points6 = int(Wins6 * 2)
#Losses
print("\t\tHow many losses?")
print(Team1)
Losses1 = int(input())
print(Team2)
Losses2 = int(input())
print(Team3)
Losses3 = int(input())
print(Team4)
Losses4 = int(input())
print(Team5)
Losses5 = int(input())
print(Team6)
Losses6 = int(input())
#Ties
print("\t\tHow many ties?")
print(Team1)
Ties1 = int(input())
print(Team2)
Ties2 = int(input())
print(Team3)
Ties3 = int(input())
print(Team4)
Ties4 = int(input())
print(Team5)
Ties5 = int(input())
print(Team6)
Ties6 = int(input())
Points7 = int(Ties1 * 1)
Points8 = int(Ties2 * 1)
Points9 = int(Ties3 * 1)
Points10 = int(Ties4 * 1)
Points11 = int(Ties5 * 1)
Points12 = int(Ties6 * 1)
#Calculate
Final1 = int(Points1 + Points7)
Final2 = int(Points2 + Points8)
Final3 = int(Points3 + Points9)
Final4 = int(Points4 + Points10)
Final5 = int(Points5 + Points11)
Final6 = int(Points6 + Points12)
print("Team name:",Team1,"wins:",Wins1,"Ties:",Ties1,"Losses:",Losses1,"Points:",Final1)
print("Team name:",Team2,"wins:",Wins2,"Ties:",Ties2,"Losses:",Losses2,"Points:",Final2)
print("Team name:",Team3,"wins:",Wins3,"Ties:",Ties3,"Losses:",Losses3,"Points:",Final3)
print("Team name:",Team4,"wins:",Wins4,"Ties:",Ties4,"Losses:",Losses4,"Points:",Final4)
print("Team name:",Team5,"wins:",Wins5,"Ties:",Ties5,"Losses:",Losses5,"Points:",Final5)
print("Team name:",Team6,"wins:",Wins6,"Ties:",Ties6,"Losses:",Losses6,"Points:",Final6)
print("\t\tpress enter to continue to the next lines")
input()
#Podium Calculation
Number1 = max(Final1,Final2,Final3,Final4,Final5,Final6)
if Number1 == Final1:
    Winner = Team1
elif Number1 == Final2:
    Winner = Team2
elif Number1 == Final3:
    Winner = Team3
elif Number1 == Final4:
    Winner = Team4
elif Number1 == Final5:
    Winner = Team5
else:
    Winner = Team6
print("And the winner of this tournament is...", Winner)

