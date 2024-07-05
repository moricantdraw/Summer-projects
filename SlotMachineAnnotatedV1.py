#This code is going to simulate a 3x3 slots game. There are 3 reels with 3 outputs each. Get 3 outputs in a row for a win.
#the module we're importing here will help us randomize things 
import random

#this is a global constant. It's goingto define how many lines are going to exist in the slot machine 
MAX_LINES = 3
#this defines the maximum money that can be bet on each line
MAX_BET = 100
#this defines the minimum money that can be bet on each line
MIN_BET = 1
#This says there are 3 rows in the slot machine (which is why theres a max of 3 lines to bet on)
ROWS = 3
#this says there are 3 columns (which is why the win condition is 3 in a row)
COLS = 3



# this dictionary is going to define the number of symbols on each reel (three will be randomly selected from it) and the values of each of those symbols 
symbol_count = {
    #This first line is saying that there will be 2 "A" symbols on each reel
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    #This first line is saying that there will be 2 "A" symbols on each reel
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines =[]
    #looping and checking every row
    for line in range(lines):
        #check whichever symbol is in the first column of that row (to see if the others match it)
        symbol = columns[0][line]
        #loop through the columns to check for a matcing symbol
        for column in columns:
            #checks in the other columns at the current row
            symbol_to_check = column[line]
            #check if they are not the same (aka a loss)
            if symbol != symbol_to_check:
                break
        else:
            #a win so we calculate winnings 
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings, winning_lines

#This runction is going to generate the outcome of our slots game. Rows, cols and symbols are the parameters this function is going to take
def get_slot_machine_spin(rows, cols, symbols):
    #we're going to create a list that contains all the differnt values we could select from and the choose a random 3 from that list removing options from the list once they have been chosen 
    #this next line is defining a list 
    all_symbols =[]
    #Now we're going to use a for loop that adds however many symbols we have to the all symbols list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    #This next part of code will record the output of our virtual slot machine 
    #First we define a column list 
    columns = []
    #Now we're going to generate a column for ever column that we have 
    for _ in range(cols):
        #This next part of code is going to randomly fill each column 
        #this is going to define an empty list for us to store our information
        column = []
        #This is going to make sure that were taking values from a copy of the list 
        current_symbols = all_symbols[:]
        #here we're going to generate a value for each of the rows 
        for _ in range(rows):
            #this randomly selescts our value 
            value = random.choice(current_symbols)
            #this removes the value from the selection so that we can't double pick
            current_symbols.remove(value)
            #This adds the value selected to the list where we're keeping our generated vlaues 
            column.append(value)
        #Here we add our completed column to our list our columns 
        columns.append(column)
    return columns

#this function will print out the output of our solt machine 
def print_slot_machine(columns):
    #Each list would normally print out horzontal which is notably not a column 
    #We're therefore going to treat the output like a matrix and transpose it 
    for row in range(len(columns[0])):
        #this will loop through all the columns and only print the first value in in 
        for i, column in enumerate(columns):
            if i != len (columns) - 1:
                print(column[row], end= " | ")
            else: 
                 print(column[row], end="")
        print()

# function that collects user input 
# collects users initial deposit

def deposit():
    #using while loop to keep asking for input until it gets a valid input 
    while True: 
        # next line of code is setting a new variable equal to an input that we collect from the user. This method of collecting inputs collects them as strings 
        # inside the quotes is the text that prompts the user to give the input
        amount = input("What would you like to deposit? $")
        # we need to check if amount is a number before we go on so were going to use "if" to make sure that we are only moving on with a valid input
        if amount.isdigit():
            #now we can turn this number into an integer variable so that we can do math with it later on 
            amount = int(amount)
            # we also need to be sure that the number is greater than zero for the slots to work so we'll set that condition in the same way
            if amount > 0:
                #if both of these conditions are satisfied than we have a collected a working depost value and we can end the funtion
                break
            else: 
                #if it's not bigger than 0 a new number must be entered so we will print what when wrong and then the previous while loo[ will repromt 
                print("Amount must be greater than 0.")
        else:
            # we will also include a message here in case the first condition was failed
            print ("Please enter a number.")
    #the objective of this function is to collect and define a variable amount. It should therefore return a variable that contains the deposit value as an interger that can be used later in the code. 
    return amount 

#function that collects user input 
#collects how many lines they want to bet on
def get_number_of_lines():
    #This is going to collect input in the same way as the deposit function so we're going to use to the same format
    while True: 
        #This still follows the same general format as the deposit function except for inside the string of text which contations a concatenation (" + str(MAX_LINES) + ")this convert the int constant to a string so that it can be typed out as "(1-3)?" or whatever else the max vbl is set to 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines.")
        else:
            print ("Please enter a number.")
    return lines

# function that collects user input
# collects the amount the user is betting on each line 
def get_bet():
    #This is going to collect input in the same way as the deposit function so we're going to use to the same format
    while True: 
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                #This shows another way to convert an integer into a string 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print ("Please enter a number.")

    return amount

def spin(balance):
 #this line of code will prompt the collection of the lines variable through the get_number_of_lines function 
    lines = get_number_of_lines()
    #This while loop will make sure the bet is less than the deposit
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    #this line will calculate the total bet based off of the lines and bet per line
    total_bet = bet * lines
    #now that all of the necessary data had been collected from the user, we will tell them what they've done with a string of text before running slot machine simulator 
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. ")
    #this will generate the slot machine results 
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines  = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:",*winning_lines)
    return winnings - total_bet


#this is going to be the start of our main program 
#this function will call all of the other functions needed for a turn so by running main we can test the whole program 
def main():
    #this line of code will prompt the collection of the balance variable through the deposit function 
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print (f"You left with ${balance}")
main()
