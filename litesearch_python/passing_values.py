# create two funcs.

# First func pass value 5 to second function

# second function adds 5 to the passed value

def giveFive():
    myval = 5

    takeFiveVal = takeFive(myval)
    
    print(myval)

    print(takeFiveVal)



def takeFive(myval : int) -> int:
    myval = myval + 5
    return myval

def giveList():
    mylist = ["giveList"]
    takeList(mylist)
    print(mylist)

def takeList(someList: list):
    someList.append("takeList")

giveList()