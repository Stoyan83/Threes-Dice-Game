
def bet_is_ligit(number, current_money):
    current_money = current_money
    while True:
        try:

            bet = int(input(number))
            if bet <= 0 or bet > current_money:
                raise ValueError
            break

        except ValueError:
            print("INVALID AMOUNT OR NOT ENOUGH MONEY IN YOUR ACCOUNT PLEASE TRY AGAIN")
    return bet


def is_positive(number):
    while True:
        try:

            deposit = int(input(number))
            if deposit <= 0:
                raise ValueError
            break

        except ValueError:
            print("INVALID AMOUNT PLEASE TRY AGAIN")

    return deposit


def valid_dice(amount, number):
    while True:
        try:

            index = int(input(number))
            if index - 1 < 0 or index - 1 >= amount:
                raise ValueError
            break

        except ValueError:
            print("Invalid dice number please try again")

    return index
