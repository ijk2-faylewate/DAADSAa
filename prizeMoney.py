import csv
import tennisTools
import ranking
import sortLists


#Calculate winnings after every tornement
def calculatePrizeMoney(tornement, roundNumber, gender):
    currentWinnings = []
    tempDataList = []
    listOfWinners = tennisTools.currentWinners

    #Determine gender of players
    if gender == 'f':
        tempPrizeFile = 'TEMP_PRIZE_TOTAL_FEMALE.csv'
    elif gender == 'm':
        tempPrizeFile = 'TEMP_PRIZE_TOTAL_MALE.csv'

    #Read file containing amounts of money ro be won to array
    with open('PRIZE_MONEY.csv', "r") as prizeFile:
        prizeReader = csv.reader(prizeFile, delimiter =',', quotechar='|')
        for prize in prizeReader:
            currentWinnings.append(''.join(prize).strip('"'))    

    #Read in temporary prize file
    with open(tempPrizeFile, "r") as playerList:
        playerReader = csv.reader(playerList, delimiter =',', quotechar='|')
        for players in playerReader:
            tempDataList.append(players)

    #Assign winnings based on list/array position and tornement type

    #TAC1. Array index 0 - 3
    if tornement == tennisTools.tornementOne:
        low = currentWinnings[3]
        mid = currentWinnings[2]
        runUp = currentWinnings[1]
        win = currentWinnings[0]

    #TAE21. Array index 4 - 7    
    elif tornement == tennisTools.tornementTwo:
        low = currentWinnings[7]
        mid = currentWinnings[6]
        runUp = currentWinnings[5]
        win = currentWinnings[4]

    #TAW11. Array index 8 - 11    
    elif tornement == tennisTools.tornementThree:
        low = currentWinnings[11]
        mid = currentWinnings[10]
        runUp = currentWinnings[9]
        win = currentWinnings[8]

    #TBS2. Array index 12 - 15   
    elif tornement == tennisTools.tornementFour:
        low = currentWinnings[15]
        mid = currentWinnings[14]
        runUp = currentWinnings[13]
        win = currentWinnings[12]
        
    #If round == 2
        #all winning players insert() lowest win bracket
    #If round == 3
        #four loosing players leave with current
        #four highest pop() current winnings
        #insert mid pay bracket
    #if round == 4
        #looser pop() mid pay bracket,
        #looser insert runUp pay bracket
    #if round == 5
        #winner pop() runUp pay bracket
        #winner insert win pay bracket

    for i in range(len(tempDataList)):
        for j in range(len(listOfWinners)):
            if roundNumber == '2':
                if listOfWinners[j] == tempDataList[i][0]:
                    tempDataList[i].insert(1, low)
                    tempDataList[i].pop(2)

            elif roundNumber == '3':
                if listOfWinners[j] == tempDataList[i][0]:
                    tempDataList[i].insert(1, mid)
                    tempDataList[i].pop(2)      
    
            elif roundNumber == '4':
                if listOfWinners[j] == tempDataList[i][0]:
                    tempDataList[i].insert(1, runUp)
                    tempDataList[i].pop(2)

            elif roundNumber == '5':
                if listOfWinners[j] == tempDataList[i][0]:
                    tempDataList[i].insert(1, win)
                    tempDataList[i].pop(2)
                    
    #Write new value to tempory prize file
    with open(tempPrizeFile, "w", newline='') as tempPointsFile:
        writePoints = csv.writer(tempPointsFile, delimiter =',', quotechar='|' )
        for players in range(len(tempDataList)):
            writePoints.writerow(tempDataList[players])
        
    

#Add valuse from round to file. 
def commitPrizeMoney(gender):
    fromRound = []
    toFile = []

    #choose gender of file
    if gender == 'f':
        tempPrizeFile = 'TEMP_PRIZE_TOTAL_FEMALE.csv'
        prizeFile = 'PRIZE_TOTAL_FEMALE.csv'
    elif gender == 'm':
        tempPrizeFile = 'TEMP_PRIZE_TOTAL_MALE.csv'
        prizeFile = 'PRIZE_TOTAL_MALE.csv'
        
    #Read information from temporary per round file
    with open(tempPrizeFile, "r") as openTemp:
        tempPrizeReader = csv.reader(openTemp, delimiter =',', quotechar='|' )
        for players in tempPrizeReader:
            fromRound.append(players)

    #Read information from overall prize file
    with open(prizeFile, "r") as openFinal:
        prizeReader = csv.reader(openFinal, delimiter =',', quotechar='|' )
        for players in prizeReader:
            toFile.append(players)

    #Compare temporary round file with overall round file. Add prize values together and add to overall        
    for i in range(len(toFile)):
        for j in range(len(fromRound)):
            if fromRound[j][0] == toFile[i][0]:
                tempFromRound = int(fromRound[j][1])
                newScore = int(toFile[i][1]) + tempFromRound
                toFile[i].insert(1, newScore)
                toFile[i].pop(2)

    #commit to file
    with open(prizeFile, "w", newline='') as writeToFinal:
        prizeWriter = csv.writer(writeToFinal, delimiter =',', quotechar='|')
        for players in range(len(toFile)):
            prizeWriter.writerow(toFile[players])

#Clear temp file for next tornement
def clearTemporaryRoundFile(gender):
    tempDataList = []
    zero = 0

    #Choose file gender
    if gender == 'f':
        playerFile = 'FEMALE_PLAYER_LIST.csv'
        pointsFromFile = 'TEMP_PRIZE_TOTAL_FEMALE.csv'
    elif gender == 'm':
        playerFile = 'MALE_PLAYER_LIST.csv'
        pointsFromFile = 'TEMP_PRIZE_TOTAL_MALE.csv'
    
     #Read in player list   
    with open(playerFile, "r") as pointsFile:
        femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
        for players in femalePlayers:
            tempDataList.append(players)
    #Write to file, players and a '0' column
    with open(pointsFromFile, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(tempDataList)):
            writePoints.writerow(tempDataList[players] + [zero])

#Display winnings by sending list to sort function       
def displayWinnings(gender):

    displayWinnings = []

     #choose gender of file
    if gender == 'f':
        prizeFile = 'PRIZE_TOTAL_FEMALE.csv'
    elif gender == 'm':
        prizeFile = 'PRIZE_TOTAL_MALE.csv'

    #Read information from overall prize file
    with open(prizeFile, "r") as openFinal:
        prizeReader = csv.reader(openFinal, delimiter =',', quotechar='|' )
        for players in prizeReader:
            displayWinnings.append(players)

    #Display
    print(sortLists.enterSorting(displayWinnings))
    
    


