from .constraint import  is_positive
from .checking_game_result import check_result
from .game_logic import bet
from .login_player import player



money_amount = 0
player_name = ''

players = {}

still_play = True

while True:

    choice = input('''
    ***********************************************************************
    ========== THIS IS SIMPLE GAMBLING GAME, PLAYED WITH FIVE DICE ========
    ***********************************************************************
    ===========           Do YOU WANT TO PLAY? [YES/NO]            ========
    ***********************************************************************
    ''').upper().strip()
    if choice == "NO" or choice == "N":
        print("BYE, YOU WILL COME BACK AGAIN !")
        still_play = False
        break

    elif choice == "YES" or choice == "Y":
        player_name = player("ENTER YOUR NAME: ")
        players[player_name] = 0
        deposit = is_positive('PLEASE DEPOSIT AMOUNT OF MONEY TO PLAY WITH. ONLY INTEGER NUMBERS, NO COINS ')
        if deposit:
            money_amount += int(deposit)
            players[player_name] += int(deposit)
            break


    else:
        print("PLEASE ENTER A VALID COMMAND")

if money_amount > 0:
    print('''
*************************************************************************************************
*************************************************************************************************
*************************************************************************************************
EACH PLAYER ANTES ONE BETTING UNIT INTO THE POT AND THEY THEN TAKE IT IN TURN THROWING THE DICE. 
THE OBJECT OF THE GAME IS TO SCORE THE LOWEST TOTAL AMOUNT BY ADDING UP THE SPOT VALUES OF ALL 
FIVE SET ASIDE DICE BUT COUNTING 3S AS ZEROES.
EACH PLAYER HAS UP TO FIVE ROLLS OF THE DICE, BUT MUST SET AT LEAST ONE ASIDE AFTER EACH THROW. 
ONCE A DICE IS SET ASIDE, IT MAY NOT BE ROLLED AGAIN.
THE BEST POSSIBLE SCORE AFTER ALL THE DICE HAVE BEEN SET ASIDE IS 0 (3-3-3-3-3), BUT SHOULD ANY 
PLAYER ROLL 6-6-6-6-6 ("SHOOTING THE MOON"), THEY WIN INSTANTLY WITH NO FURTHER PLAY.
*************************************************************************************************
*************************************************************************************************
*************************************************************************************************
''')

    print(f"YOUR DEPOSIT IS: {deposit} \nTotal money: ${money_amount}")
if still_play:
    sum_left_dice, sum_left_computer_dice, left_dice, left_computer_dice, current_bet = bet(money_amount)

if still_play:
    money = check_result(sum_left_dice, sum_left_computer_dice, left_dice, left_computer_dice, current_bet)
    money_amount += money
    players[player_name] = money_amount
    

while True:
    menu = input('''
    ***********************************************************************
    ***********************************************************************
    ==============           TO BET PRESS [B]               ===============
    ==============       TO MAKE DEPOSIT PRESS  [D]         ===============
    ==============   TO WITHDRAW YOUR MONEY PRESS [W]       ===============
    ==============  TO SEE YOUR CURRENT BANK PRESS [C]      ===============
    ==============          TO QUIT PRESS  [Q]              ===============
    ***********************************************************************
    ***********************************************************************
    ''').upper().strip()
    if menu == "B":
        if money_amount > 0:
            sum_left_dice, sum_left_computer_dice, left_dice, left_computer_dice, current_bet = bet(money_amount)
            money = check_result(sum_left_dice, sum_left_computer_dice, left_dice, left_computer_dice, current_bet)
            money_amount += money
            players[player_name] += money_amount
        else:
            print("NO MONEY IN YOUR ACCOUNT !")
    elif menu == "C":
        print(f"======       {''.join([key for key in players.keys()])} YOU HAVE ${money_amount} IN YOUR ACCOUNT      =====")

    elif menu == "Q":
        print("BYE, YOU WILL COME BACK AGAIN !")
        break
    elif menu == "W":
        if money_amount > 0:
            withdraw = is_positive("MAKE YOUR WITHDRAW. ONLY INTEGER NUMBERS, NO COINS: ")
            if withdraw:
                money_amount -= withdraw
              
                print(F" {''.join([key for key in players.keys()])} YOU SUCCESSFULLY WITHDRAW ${withdraw}\n=====       {''.join([key for key in players.keys()])} YOU HAVE TOTAL MONEY: ${money_amount}       =====")
        else:
            print("NO MONEY IN YOUR ACCOUNT !")
    elif menu == "D":
        if player_name == '':
           player_name = player("ENTER YOUR NAME: ") 
           players[player_name] = 0
        else:
            new_deposit = is_positive('PLEASE DEPOSIT AMOUNT OF MONEY TO PLAY WITH. ONLY INTEGER NUMBERS, NO COINS ')
            money_amount += new_deposit
            print(F"YOU SUCCESSFULLY DEPOSIT ${new_deposit}\n=====     TOTAL MONEY: ${money_amount}     =====")
            print('''
    *************************************************************************************************
    *************************************************************************************************
    *************************************************************************************************
    EACH PLAYER ANTES ONE BETTING UNIT INTO THE POT AND THEY THEN TAKE IT IN TURN THROWING THE DICE. 
    THE OBJECT OF THE GAME IS TO SCORE THE LOWEST TOTAL AMOUNT BY ADDING UP THE SPOT VALUES OF ALL 
    FIVE SET ASIDE DICE BUT COUNTING 3S AS ZEROES.
    EACH PLAYER HAS UP TO FIVE ROLLS OF THE DICE, BUT MUST SET AT LEAST ONE ASIDE AFTER EACH THROW. 
    ONCE A DICE IS SET ASIDE, IT MAY NOT BE ROLLED AGAIN.
    THE BEST POSSIBLE SCORE AFTER ALL THE DICE HAVE BEEN SET ASIDE IS 0 (3-3-3-3-3), BUT SHOULD ANY 
    PLAYER ROLL 6-6-6-6-6 ("SHOOTING THE MOON"), THEY WIN INSTANTLY WITH NO FURTHER PLAY.
    *************************************************************************************************
    *************************************************************************************************
    *************************************************************************************************
    ''')

