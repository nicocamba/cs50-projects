from cs50 import get_float

def main():
    cents = get_cents()
    quarters = calculate_quarters(cents)
    cents = cents - 25 * quarters
    dimes = calculate_dimes(cents)
    cents = cents - 10 * dimes
    nickels = calculate_nickels(cents)
    cents = cents - 5 * nickels
    pennies = calculate_pennies(cents)
    coins = quarters + dimes + nickels + pennies
    print(f"{coins} coins")



def calculate_quarters(cents):
    n = cents // 25
    return n

def calculate_dimes(cents):
    n = cents // 10
    return n

def calculate_nickels(cents):
    n = cents // 5
    return n

def calculate_pennies(cents):
    n = cents // 1
    return n




def get_cents():
    while True:
        n = get_float("Change: ")
        if n >= 0:
            break
    return n * 100

main()
