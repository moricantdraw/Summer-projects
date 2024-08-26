#This code is going to simulate a 3x3 slots game. There are 3 reels with 3 outputs each. Get 3 outputs in a row for a win.
#the module we're importing here will help us randomize things

import random

#Global Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Dictionaries
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    """
    Calulates and returns how much money the player wins and how many lines they won on.

    Args:
        columns: a list of lists representing the outcome of the slots game.
        lines: an integer represing how many lines the player bet on.
        bet: an integer representing the amount of money the player bet on each line.
        values: integers from a dictionary representing the value of each symbol 

    Returns:
        An integer containing how much money the player won and an integer contatining how many lines they won on.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Returns outcome of the slots game

    Args:
        rows: integer representing the amount of rows in the slots game
        cols: integer representing the amount of columns in the slots game 
        symbols: variables from the symbols dictionary 

    Returns:
       A list of lists representing the outcome of the slots game.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    """
    Print out the output of our slot machine

    Args:
       columns: a list of lists representing the outcome of the slots game generates by the get_slot_machine_spin function.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    """
    Collects user input representing the amount of money they want to deposit.

    Returns:
        An integer representing the amount of money the player wants to deposit.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    """
    Collects user input representing how many lines they want to bet on

    Returns:
        An integer representing how many lines the player wants to bet on.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" +
                      str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    """
    Collects user input representing the amount the user is betting on each line.
    
    Returns:
        An integer representing the amount the user is betting on each line.
    """

    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Checks if a bet is less than the players's deposit and returns winnings of viable bets  

    Args:
       Balance: An integer representing the amount of money the player has deposited and not yet used

    Returns:
        Integer containing player's account balance after playing    
    """

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount. Your current balance is: ${balance}"
            )
        else:
            break
    total_bet = bet * lines
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. "
    )
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:, {winning_lines}")
    return winnings - total_bet

def main():
    
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    
main()