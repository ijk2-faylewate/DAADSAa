import csv
import tennisTools
import sortLists

copyForSortOverallRank = []
copyForSortRankForRound = []

#Update's total, season wide, points (also, currently erroneuosly calculates points mid tournement, rather than at the end)
def updateRankPoints(tornementName, roundNumber, gender):
    
    #Save overall points from last round.
    #Run new round
    #Read points from previous round to list
    #If winner, subtract previous rounds points
    #Add new points to list
    #save new points to file.

    currentWinners = tennisTools.currentWinners
    rankPoints = 0
    previousRoundPoints = 0
    difficultyPoints = 0.0

    tempPlayerList = []
    playerList = []
    tempDataList = []
    pointsList = []

    #assign tornement difficulty
    if tornementName == tennisTools.tornementOne:
        difficultyPoints = 2.7
    elif tornementName == tennisTools.tornementTwo:
        difficultyPoints = 2.3
    elif tornementName == tennisTools.tornementThree:
        difficultyPoints = 3.1
    elif tornementName == tennisTools.tornementFour:
        difficultyPoints = 3.25
    
    #select ranking points for current rount and previous round
    with open('RANKING_POINTS.csv', "r") as readPoints:
        pointsReader = list(csv.reader(readPoints, delimiter =',', quotechar='|'))

    if gender == 'f':
        overallPointsFile = 'OVERALL_POINTS_WOMEN.csv'
    elif gender == 'm':
        overallPointsFile = 'OVERALL_POINTS_MEN.csv'

    #Points assigned to different rounds
    if roundNumber == '1':
        rankPoints = pointsReader[8][0]
    elif roundNumber == '2':
        rankPoints = pointsReader[4][0]
        previousRoundPoints = pointsReader[8][0]
    elif roundNumber == '3':
        rankPoints = pointsReader[3][0]
        previousRoundPoints = pointsReader[4][0]
    elif roundNumber == '4':
        rankPoints = pointsReader[1][0]
        previousRoundPoints = pointsReader[3][0]
    elif roundNumber == '5':
        rankPoints = pointsReader[0][0]
        previousRoundPoints = pointsReader[0][0]

    #Total points awarded to player leaving a round    
    rankPoints = float(rankPoints) * difficultyPoints

    #Points deleted from player progressing to next round (new points added at next level)
    winnersDeduction = float(previousRoundPoints) * difficultyPoints 

    #Read saved overall points into list
    with open(overallPointsFile, "r") as pointsFile:
        thesePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            tempDataList.append(players)     

    #Populate temporary full player list
    for i in range(len(tempDataList)):
        playerList.append(tempDataList[i][0])        

    #save temp list of winners
    tempPlayerListWinners = [tempPlayerList for tempPlayerList in playerList if tempPlayerList in currentWinners]

    #Add points from round one. Then, add points if player not advancing, remove points if player advancing. Simply assign points to winner.
    for i in range(len(tempDataList)):
        for j in range(len(currentWinners)):
            if roundNumber == '1':
                if currentWinners[j] == tempDataList[i][0]: 
                    tempScore = float(tempDataList[i][1])
                    tempDataList[i].insert(1, tempScore + rankPoints)
                    tempDataList[i].pop(2)

            elif roundNumber == '5':
                if tempPlayerListWinners[j] == tempDataList[i][0]:
                    tempScore = float(tempDataList[i][1])
                    tempDataList[i].insert(1, rankPoints)
                    tempDataList[i].pop(2)
                
            else:
                if tempPlayerListWinners[j] == tempDataList[i][0]:
                    tempScore = float(tempDataList[i][1])
                    tempDataList[i].insert(1, (tempScore - winnersDeduction) + rankPoints)
                    tempDataList[i].pop(2)               

    #Save points back into file    
    with open(overallPointsFile, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(tempDataList)):
            writePoints.writerow(tempDataList[players])

    #Copy list for eventual display of rank
    global copyForSortOverallRank 
    copyForSortOverallRank = tempDataList

#Calculates points within a tornement, round to round. Saves information to a temporary location, in case of mid tornement closure. 
def updatePointsCurrentTornement(tornementName, roundNumber, gender):
    currentWinners = tennisTools.currentWinners
    rankPoints = 0
    previousRoundPoints = 0

    playerList = []
    tempDataList = []

    #select ranking points for current rount and previous round
    with open('RANKING_POINTS.csv', "r") as readPoints:
        pointsReader = list(csv.reader(readPoints, delimiter =',', quotechar='|'))

    #Points assigned to different rounds
    if roundNumber == '1':
        rankPoints = int(pointsReader[8][0])
    elif roundNumber == '2':
        rankPoints = pointsReader[4][0]
        previousRoundPoints = int(pointsReader[8][0])
    elif roundNumber == '3':
        rankPoints = pointsReader[3][0]
        previousRoundPoints = int(pointsReader[4][0])
    elif roundNumber == '4':
        rankPoints = pointsReader[1][0]
        previousRoundPoints = int(pointsReader[3][0])
    elif roundNumber == '5':
        rankPoints = pointsReader[0][0]
        previousRoundPoints = int(pointsReader[0][0])

    #Select gender of files
    if gender == 'f':
        nameOfFillFile = 'FEMALE_PLAYER_LIST.csv'
        tempTornementFile = 'TEMP_TORNEMENT_FEMALE.csv'
    elif gender == 'm':
        nameOfFillFile = 'MALE_PLAYER_LIST.csv'
        tempTornementFile = 'TEMP_TORNEMENT_MALE.csv'

    #Populate player lists
    tennisTools.fillPlayerList(nameOfFillFile, playerList)

    #save temp list of winners
    tempPlayerListWinners = [tempPlayerList for tempPlayerList in playerList if tempPlayerList in currentWinners]

    with open(tempTornementFile, "r") as pointsFile:
        thesePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            tempDataList.append(players)

    #Add points from round one. Then, add points if player not advancing, remove points if player advancing. Simply assign points to winner.
    for i in range(len(tempDataList)):
        for j in range(len(currentWinners)):
            if roundNumber == '1':
                if currentWinners[j] == tempDataList[i][0]: 
                    tempScore = int(tempDataList[i][1])
                    tempDataList[i].insert(1, tempScore + rankPoints)
                    tempDataList[i].pop(2)

            elif roundNumber == '5':
                if tempPlayerListWinners[j] == tempDataList[i][0]:
                    tempScore = int(tempDataList[i][1])
                    tempDataList[i].insert(1, rankPoints)
                    tempDataList[i].pop(2)
                
            else:
                if tempPlayerListWinners[j] == tempDataList[i][0]:
                    tempScore = int(tempDataList[i][1])
                    tempDataList[i].insert(1, (int(tempScore) - int(previousRoundPoints)) + int(rankPoints))
                    tempDataList[i].pop(2)
    
    #Save points back into file    
    with open(tempTornementFile, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(tempDataList)):
            writePoints.writerow(tempDataList[players])

    global copyForSortRankForRound
    copyForSortRankForRound = tempDataList
    

#Clears temporary in tornement save file
def clearTempFileForPastTornement(gender):
    tempData = []
    zero = 0

    #Select gender of files
    if gender == 'f':
        x = 'TEMP_TORNEMENT_FEMALE.csv'
        a = 'FEMALE_PLAYER_LIST.csv'
    elif gender == 'm':
        x = 'TEMP_TORNEMENT_MALE.csv'
        a = 'MALE_PLAYER_LIST.csv'

    #Store player list
    with open(a, "r") as pointsFile:
        femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
        for players in femalePlayers:
            tempData.append(players)


    #Restore file to default. List of players with score of zero
    with open(x, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(tempData)):
            writePoints.writerow(tempData[players] + [zero])

