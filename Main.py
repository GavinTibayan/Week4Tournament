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
print("Whats the team name?")
Team1 = input()
#Wins
Wins1 = input()
Points1 = int(Wins1 * 2)
#Losses
Losses1 = input()
#Ties
Ties1 = input()
Points2 = int(Ties1)
#Calculate
Points3 = int(Points1 + Points2)

print("Team name:",Team1,"wins:",Wins1,"Ties:",Ties1,"Losses:",Losses1,"Points:",Points3)
