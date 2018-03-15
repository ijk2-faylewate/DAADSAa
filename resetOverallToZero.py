import csv


#Nasty messy file/function that resets all storage files to player lists with zero coloumn, and check list to default
def wipeAllData():
    tempDataList = []
    tempDataList2 = []
    tempDataList3 = []
    tempDataList4 = []
    tempDataList5 = []
    tempDataList6 = []
    tempDataList7 = []
    tempDataList8 = []
    tornementPrevious = []

    zero = 0

    with open('FEMALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList.append(players)
    #Overall Points women
    with open('OVERALL_POINTS_WOMEN.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList)):
                writePoints.writerow(tempDataList[players] + [zero])


    with open('MALE_PLAYER_LIST.csv', "r") as pointsFile:
            malePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in malePlayers:
                tempDataList2.append(players)
    #Overall points men
    with open('OVERALL_POINTS_MEN.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList2)):
                writePoints.writerow(tempDataList2[players] + [zero])


    with open('MALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList3.append(players)
    #Temporary tornement men
    with open('TEMP_TORNEMENT_MALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList3)):
                writePoints.writerow(tempDataList3[players] + [zero])


    with open('FEMALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList4.append(players)
    #Temporary tornement women
    with open('TEMP_TORNEMENT_FEMALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList4)):
                writePoints.writerow(tempDataList4[players] + [zero])



    with open('MALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList5.append(players)
    #Prize money total men
    with open('PRIZE_TOTAL_MALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList5)):
                writePoints.writerow(tempDataList5[players] + [zero])


    with open('FEMALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList6.append(players)
    #Prize money total women
    with open('PRIZE_TOTAL_FEMALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList6)):
                writePoints.writerow(tempDataList6[players] + [zero])



    with open('MALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList7.append(players)
    #Temp Prize money men
    with open('TEMP_PRIZE_TOTAL_MALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList7)):
                writePoints.writerow(tempDataList7[players] + [zero])


    with open('FEMALE_PLAYER_LIST.csv', "r") as pointsFile:
            femalePlayers = csv.reader(pointsFile, delimiter=',', quotechar='|')
            for players in femalePlayers:
                tempDataList8.append(players)
    #Temp Prize money women
    with open('TEMP_PRIZE_TOTAL_FEMALE.csv', "w", newline='') as pointsFile:
            writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
            for players in range(len(tempDataList8)):
                writePoints.writerow(tempDataList8[players] + [zero])


    true = 'TRUE'
    one = '1'

    #Restore previous round check to default
    with open('PREVIOUS_ROUND_COMPLETE_CHECK.csv', "r") as ReadFile:
            tornementPrevious = list(csv.reader(ReadFile, delimiter =',', quotechar='|'))
        
    with open('PREVIOUS_ROUND_COMPLETE_CHECK.csv', "w", newline='') as checkFile:
        writeCheck = csv.writer(checkFile, delimiter =',', quotechar='|' )
        for tornements in range(len(tornementPrevious)):
            writeCheck.writerow([tornementPrevious[tornements][0]] + [tornementPrevious[tornements][1]] + [true] + [one]  )



