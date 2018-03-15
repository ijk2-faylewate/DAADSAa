import csv
import math

#Function to make quickSort easier to access
def enterSorting(listToSort):
    quickSort(listToSort,0, len(listToSort) - 1)

    #Display
    count = 0
    for i in range(len(listToSort)):
        count = count + 1
        print(count, ':',listToSort[i][0], round(float(listToSort[i][1]), 2) )
        
#Spit lists at pivot and recursivly sort either side of pivot
def quickSort(listToSort,first, last):
    if first < last:
        splitpoint = partition(listToSort, first, last)
        quickSort(listToSort, first, splitpoint - 1)
        quickSort(listToSort, splitpoint + 1, last )

#Define point at which to split list
def partition(listToSort,first, last):

    #Define pivot(intitally at first element of list)
    pivot = float(listToSort[first][1])
    #Left value (at second element of list)
    leftVal = float(listToSort[1][1])
    #Right value (at last element of list)
    rightVal = float(listToSort[len(listToSort) - 1][1])

    #Define left and right mark (list indexs)
    left = first + 1
    right = last

    done = False
    #While leftmark (index) is less than rightmark (index) and value of left mark greater than pivot
    #Increment leftmark(index). Then do the opposite (while right less than pivot and greater than left, decrement)
    while done == False:
        while left <= right and float(listToSort[left][1]) >= pivot:
            left = left + 1
        while float(listToSort[right][1]) <= pivot and right >= left:
            right = right - 1
        #when right and left meet, stop. Splitpoint found
        if right < left:
            done = True
        #Swap left element and right element
        else:
            temp = listToSort[left]
            listToSort[left] = listToSort[right]
            listToSort[right] = temp
    #Swap 'first' element with right(define next splitpoint)
    temp = listToSort[first]
    listToSort[first] = listToSort[right]
    listToSort[right] = temp
    
    #Return splitpoint
    return right

