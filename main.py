import tennisTools
import ranking
import prizeMoney
import manualInput
import sys
import sortLists
import menuFunctions

#Set saved data files to default(Does not delete results files)
menuFunctions.dataWipe()
#########################
#START MAIN PROGRAM LOOP#
#########################
while True:

    #Populate list of Male Players
    listOfMalePlayers = []
    tennisTools.fillPlayerList('MALE_PLAYER_LIST.CSV', listOfMalePlayers)

    #Populate list of female players
    listOfFemalePlayers = []
    tennisTools.fillPlayerList('FEMALE_PLAYER_LIST.CSV', listOfFemalePlayers)
    
    #Tornement select
    tornement = menuFunctions.tornementSelector()

    #Simple string to complete nameOfFile
    fileType = '.csv'

    #Gender select
    selectGender= menuFunctions.genderSelector()

    #Check if previous tornement of this type ended properly
    checkPrevious = tennisTools.checkIfPreviousComplete(tornement, selectGender)

    #IF PREVIOUS TORNEMENT OF THIS TYPE COMPLETED, RUN AS NORMAL
    if checkPrevious == 'TRUE':
        #Manual imput option
        manualSelect = menuFunctions.manualSelector()

        playRound = 0
        #Play next round
        playRound = menuFunctions.playNextRound(playRound)
        print('Round: ',  playRound)
        
        #Determine list of players to use
        if selectGender == 'f':
            gender = '_WOMEN'
            if manualSelect == 'n':
                listSelect = listOfFemalePlayers
        elif selectGender == 'm':
            gender = '_MEN'
            if manualSelect == 'n':
                listSelect = listOfMalePlayers

        #Recieve manual input if requested, else ignore
        if manualSelect == 'y':
            listSelect = manualInput.userInputStack(selectGender, str(playRound))
        else:
            pass

        #Name of Round File to be generated
        nameOfFile = tornement + str(playRound) + gender + fileType
        
        ######################################
        #START ROUND 1 (INITIALIZE TORNEMENT)#
        ######################################

        #Set fixtures, generate scores, write to file.
        if manualSelect == 'n':
            tennisTools.setFixtures(nameOfFile,listSelect, selectGender)
        else:
            tennisTools.setFixturesFromManual(nameOfFile,listSelect, selectGender)
            
        #Determine winners by reading file created in previous step. Display Results
        tennisTools.runRound(nameOfFile)

        #Update Ranking points, both per round and overall
        ranking.updateRankPoints(tornement, str(playRound), selectGender)
        ranking.updatePointsCurrentTornement(tornement, str(playRound), selectGender)

        #Determine money owed to each player
        prizeMoney.calculatePrizeMoney(tornement, str(playRound), selectGender)

        #Record tornement as complete, or not. 
        tennisTools.writePreviousComplete(tornement, selectGender, playRound)

        #Enable sorted lists
        cantSee = False

    #IF PREVIOUS ROUND OF THIS TORNEMENT TYPE DID NOT FINISH, RE-RUN ROUND PRIOR TO SHUTDOWN
    elif checkPrevious == 'FALSE':
        if selectGender == 'f':
            gender = '_WOMEN'
        elif selectGender == 'm':
            gender = '_MEN'
        #Get number of round to restart from (i.e. round played just before tornement finished prematurely)
        playRound = tennisTools.restartRound

        #Name of previous round
        nameOfFile = tornement + str(playRound) + gender + fileType
        #Re-run round, but don't update anything as those points already added
        tennisTools.runRound(nameOfFile)

        #Don't display option to view sorted list if re-running un-finished tornement
        cantSee = True
        manualSelect = 'n'
        
    #end check#

    ################################
    #LOOP THROUGH SUBSEQUENT ROUNDS#
    ################################

    while int(playRound) != 5:
        if cantSee == False:
            #check players' earnings
            menuFunctions.checkPrizeMoney(selectGender)
            #Check leader board for round
            menuFunctions.checkPointsFromRound()
            #check overall leader bourd
            menuFunctions.checkOverallRankPoints()
        else:
            pass

        #Enable sorted lists
        cantSee = False

        #Confirm play next round and add players to list for next round
        if manualSelect == 'y':
            playRound = menuFunctions.playNextRound(playRound)
            listSelect = manualInput.userInputStack(selectGender, str(playRound))     
        else:
            playRound = menuFunctions.playNextRound(playRound)
            listSelect = tennisTools.currentWinners

        #Display round number
        print('Round: ', playRound)

        #select file depending on round
        nameOfFile = tornement + str(playRound) + gender + fileType

        #Set fixtures, generate scores, write to file.
        if manualSelect == 'y':            
            tennisTools.setFixturesFromManual(nameOfFile,listSelect, selectGender)
        else:
            tennisTools.setFixtures(nameOfFile,listSelect, selectGender)
            
        #Clear curent winners list, so a new list of winners can be made from this round  
        tennisTools.currentWinners.clear()
        
        #Determine winners by reading file created in previous step. Display Results
        tennisTools.runRound(nameOfFile)
        
        #Update Ranking points, both per round and overall
        ranking.updateRankPoints(tornement, str(playRound), selectGender)
        ranking.updatePointsCurrentTornement(tornement, str(playRound), selectGender)

        #Determine money owed to each player
        prizeMoney.calculatePrizeMoney(tornement, str(playRound), selectGender)

        #Record tornement as complete, or not. 
        tennisTools.writePreviousComplete(tornement, selectGender, str(playRound))
    

    #Clear temporary points file, as tornement finished
    ranking.clearTempFileForPastTornement(selectGender)

    #Commit Prize money to file 
    prizeMoney.commitPrizeMoney(selectGender)

    #Clear temporary prize money file, as tornement finished
    prizeMoney.clearTemporaryRoundFile(selectGender)

    #empty current Winners list, so winner doesn't spill into next tornement
    tennisTools.currentWinners.clear()

    #check players' earnings
    menuFunctions.checkPrizeMoney(selectGender)
    #Check leader board for round
    menuFunctions.checkPointsFromRound()
    #check overall leader bourd
    menuFunctions.checkOverallRankPoints()
    
    
    #Exit System?
    #exitSystem = input('Exit Program: Y/N').upper()
    exitSystem = menuFunctions.exitSelector()
    if exitSystem == 'Y':
        sys.exit(0)
    else:
        pass

#######################
#END MAIN PROGRAM LOOP#
#######################


