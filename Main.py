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
Number6 = min(Final1,Final2,Final3,Final4,Final5,Final6)
#Calculate remainder numbers
if Number1 != Final1 or Number6 != Final1:
    Remainder1 = Final1
else:
    Remainder1 = int()
if Number1 != Final2 or Number6 != Final2:
    Remainder2 = Final2
else:
    Remainder2 = int()
if Number1 != Final3 or Number6 != Final2:
    Remainder3 = Final3
else:
    Remainder3 = int()
if Number1 != Final4 or Number6 != Final4:
    Remainder4 = Final4
else:
    Remainder4 = int()
if Number1 != Final5 or Number6 != Final5:
    Remainder5 = Final5
else:
    Remainder5 = int()
if Number1 != Final6 or Number6 != Final6:
    Remainder6 = Final6
else:
    Remainder6 = int()
Number2 = max(Remainder1,Remainder2,Remainder3,Remainder4,Remainder5,Remainder6)
Number5 = min(Remainder1,Remainder2,Remainder3,Remainder4,Remainder5,Remainder6)
#Last Stuff
if Number2 != Final1 or Number5 != Final1:
    Last1 = Final1
elif Number2 != Final2 or Number5 != Final2:
    Last2 = Final2
elif Number2 != Final3 or Number5 != Final3:
    Last3 = Final3
elif Number2 != Final4 or Number5 != Final4:
    Last4 = Final4
elif Number2 != Final5 or Number5 != Final5:
    Last5 = Final5
elif Number2 != Final6 or Number5 != Final6:
    Last6 = Final6
else:
    exit()
if Last1 != Final1:
    Last1 = int(0)
elif Last2 != Final2:
    Last2 = int(0)
elif Last3 != Final3:
    Last3 = int(0)
elif Last4 != Final4:
    Last4 = int(0)
elif Last5 != Final5:
    Last5 = int(0)
elif Last6 != Final6:
    Last6 = int(0)
else:
    exit()
Number3 = max(Last1,Last2,Last3,Last4,Last5,Last6)
Number4 = min(Last1,Last2,Last3,Last4,Last5,Last6)
#Podium
Final1 = Team1
Final2 = Team2
Final3 = Team3
Final4 = Team4
Final5 = Team5
Final6 = Team6

print("In 6th place is...", Number6)
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

