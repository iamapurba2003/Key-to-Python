listOfDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
SmallestNumberToBeMultiplied = [x for x in range(1, 53)]
YELLOW = '\u001b[33m'
RESET = '\u001b[0m'

# It gets the Smallest Number to be Multiplied by 7 to set the difference between this and the User Given Number. 
def Search(l : list, n : int):
    ln = []
    for val in l:
        if  val*7 > n:
            break
        else:
            ln.append(val*7)
    return ln[-1]


# It gets the difference and sets the day to find initially to the day one less than the First day of the Year and then runs the
# loop according to the differnce it gets and then iterates over the list of Days and find the corect match and returns the 
# required day.
def Assign(DayStarting : int, leastNumber : int, UserGivenNumber : int, dayslist : list):
    difference = UserGivenNumber - leastNumber
    DayFound = ""
    index = DayStarting+1
    if difference > 0:
        while difference != 0:
            if index > 6:
                track = 7
                index = index-track
            DayFound = dayslist[index]
            difference -= 1
            index += 1
        return DayFound
    else:
        return dayslist[index]


# Gets the First Day of the Year and the Number of the Day for which the user watnts the Day Name and sets a index number 
# for the first day of the year accounding to the listofDays
FirstDayOfYear, UserNumber = input("ENTER THE FIRST DAY OF YEAR? "), int(input("ENTER THE DAY NUMBER? "))
for index, val in enumerate(listOfDays):
    if val == FirstDayOfYear:
        IndexNumber = index

# Initialises the Search Function and passes the Smallest Number List and the Day Number of User as Arguments
a = Search(SmallestNumberToBeMultiplied, UserNumber)

# Assings the Day to one day less than the First Day of the Year
DayToBeAssigned = IndexNumber-1

# Initialises the Assign Function and passes the DayToBeAssigned, the Smallest Number to be multiplied by 7, the User Given Day 
# day Number and the listOfDays as Arguments 
b = Assign(DayToBeAssigned, a, UserNumber, listOfDays)

# Prints the Result of the required Day Name of the Given Day Number.
print()
print(f"{YELLOW}The Day of the Day Number {UserNumber} is {b}{RESET}")





def test(a):
    a = a+5
    print(id(a))
    
a = 5    
print(id(a))
test(a)



















