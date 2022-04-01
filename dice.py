import random
import time
from turtle import left

money_amount = 0
player_name = ''

players = {}

s = "+ - - - - +"
m1 = "|  o   o  |"
m2 = "|  o      |"
m3 = "|    o    |"
m4 = "|      o  |"
m5 = "|         |"

dice = [
    [m5, m3, m5],
    [m2, m5, m4],
    [m2, m3, m4],
    [m1, m5, m1],
    [m1, m3, m1],
    [m1, m1, m1]
]


def dice_line(i):
    return [s, *dice[i - 1], s]


def join_row(*rows):
    return ['   '.join(r) for r in zip(*rows)]


def ndice(*ns):
    for line in join_row(*map(dice_line, ns)):

        print("░", line, "░")


def ndice_aside(*ns):
    print("======================  SET ASIDE  ======================")
    for line in join_row(*map(dice_line, ns)):

        print("▓", line, "▓")



def roll():
    roll_result = []
    for i in range(5):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


# def computer_roll(): 
#     roll_result = []
#     for i in range(5):
#         roll = random.randint(1,4)
#         roll_result.append(roll)
#     return roll_result

def next_roll(dices):
    roll_result = []
    for _ in range(dices):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


def sum_roll_result(roll):
    roll = [x for x in roll if x != 3]
    result = sum(roll)
    return result


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

def player(line):
    while True:
        try:

            current_line = input(line).upper()
            if not current_line.isalpha() or len(current_line) < 3:
                raise ValueError
            break

        except ValueError:
            print(
'''PLEASE ENTER A VALID NAME:
Username may only contain uppercase and lowercase letters
and may have 3 or more letters.
''')

    return current_line

def command(line):
    while True:
        try:

            current_line = input(line).upper().strip()
            if current_line != "R" and current_line != "D" and current_line != "ROLL" and current_line != "DONE":
                raise ValueError
            break

        except ValueError:
            print("Invalid command please try again")

    return current_line


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


def remove_smallest(numbers):
    new_nums = []
    if len(numbers) == 0:
        return numbers
    if 3 in numbers:
        for number in numbers[:len(numbers)]:
            if number == 3:
                numbers.remove(number)
                new_nums.append(number)
                break
    else:
        for number in numbers[:len(numbers)]:
            if number == min(numbers):
                numbers.remove(number)
                new_nums.append(number)
                break
    return numbers, new_nums


def bet(money_amount):
    current_money = money_amount
    computer_turns = 4
    number_of_rolls = 4
    left_dices = []
    left_computer_dices = []
    play = True
    while True:
        if not play:
            break
        bet = bet_is_ligit("MAKE YOUR BET. ONLY INTEGER NUMBERS, NO COINS: ", current_money)
        if bet:

            current_bet = bet


            roll_results = roll()
            computer_roll_results = roll()

            print("***********************************************************************")

            print("Your turn ...")
            time.sleep(1)
            dice_faces = ndice(*roll_results)
            current_roll = roll_results
       

            print('''
***********************************************************************
***********************************************************************

            ''')

            print("Computer's turn ...")
            time.sleep(1)
            dice_faces = ndice(*computer_roll_results)
            current_computer_roll = computer_roll_results

            print("***********************************************************************")
            print(
                f"======                  YOU HAVE {sum_roll_result(current_roll)} POINTS AT THE MOMENT !                ======")
            print(
                f"===== COMPUTER REACHED THE SCORE OF {sum_roll_result(current_computer_roll)} POINTS AND WAITING FOR YOUR TURNS ! ======")

            print('''
            ***********************************************************************
            ==========      YOU CAN KEEP THAT SCORE. TYPE [DONE/D]       ==========
            ***********************************************************************
            ==========         YOU CAN ROLL AGAIN. TYPE [ROLL/R]         ==========
            ***********************************************************************
            ''')

            while True:
                if current_computer_roll + left_computer_dices == [6, 6, 6, 6, 6]:
                    # play = False
                    left_computer_dices = [6, 6, 6, 6, 6]
                    return sum_roll_result(left_dices), sum_roll_result(
                    left_computer_dices), left_dices, left_computer_dices , current_bet
                elif current_roll + left_dices == [6, 6, 6, 6, 6]:
                    # play = False
                    left_dices = [6, 6, 6, 6, 6]
                    return sum_roll_result(left_dices), sum_roll_result(
                    left_computer_dices), left_dices, left_computer_dices, current_bet
                   
                if number_of_rolls > 1:
                    current_command = command("MAKE YOUR CHOICE: ")
                if current_command == "D" or current_command == "DONE":

                 
                    if sum_roll_result(current_computer_roll + left_computer_dices) >= sum_roll_result(
                            current_roll + left_dices) and \
                            sum_roll_result(left_computer_dices) + sum_roll_result(current_computer_roll) > 5:
                        try:
                            while computer_turns > 0:
                                computer_turns -= 1
                                new_dices, aside_computer = remove_smallest(current_computer_roll)
                                left_computer_dices += aside_computer

                                next_computer = next_roll(len(new_dices))
                                current_computer_roll = next_computer
                                if computer_turns > 1:
                                    print("***********************************************************************")
                                    print("Computer's turn ...")
                                time.sleep(1)
                                dice_faces = ndice(*next_computer)
                                if sum_roll_result(current_computer_roll + left_computer_dices) < sum_roll_result(
                                        current_roll + left_dices):
                                    print("=============         COMPUTER'S DICES     ============")
                                    ndice_aside(*left_computer_dices)
                
                                    print("***********************************************************************")
                                    print(
                                        f"======                  YOU HAVE {sum_roll_result(current_roll)} POINTS AT THE MOMENT !        ======")
                                    print(
                                        f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dices + current_computer_roll)} POINTS !         ======")
                                    break
                                if sum_roll_result(current_computer_roll + left_computer_dices) >= sum_roll_result(
                                        current_roll + left_dices):

                                    print("=============         COMPUTER'S DICES     ============")
                                    ndice_aside(*left_computer_dices)
                
                                    print("***********************************************************************")
                                    print(
                                        f"======                  YOU HAVE {sum_roll_result(left_dices + current_roll)} POINTS !                     ======")
                                    print(
                                        f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dices + current_computer_roll)} POINTS !        ======")
                        except ValueError:
                            pass

                    left_dices += current_roll
                    left_computer_dices += current_computer_roll
                    
                
                 
                    play = False
                    break
                if number_of_rolls == 0:
                    left_dices += current_roll
                    left_computer_dices += current_computer_roll
                    play = False

                    break

                if current_command == "R" or current_command == "ROLL":
                
                    number_of_rolls -= 1

                    aside_dice = valid_dice(len(current_roll),
                                            "TYPE NUMBER OF THE DICE YOU WANT TO SET ASIDE, COUNTING BACKWARDS FROM RIGHT TO LEFT: ")

                    set_aside = current_roll[::-1].pop(aside_dice - 1)
                    left_dices.append(int(set_aside))

                    
                   

                    print("Your turn ...")
                    time.sleep(1)
                    roll_results = [int(x) for x in range(len(current_roll)) if x != 0]
                    next = next_roll(len(roll_results))
                    dice_faces = ndice(*next)
                    current_roll = next

                    ndice_aside(*left_dices)

                    print("*********************************************************")
                    print("*********************************************************")

                    if sum_roll_result(left_computer_dices) + sum_roll_result(current_computer_roll) > 5:
                        new_dices, aside_computer = remove_smallest(current_computer_roll)
                        left_computer_dices += aside_computer

                        next_computer = next_roll(len(new_dices))
                        print("Computer's turn ...")
                        time.sleep(1)
                        dice_faces = ndice(*next_computer)
                        current_computer_roll = next_computer
                        computer_turns -= 1

                        if len(left_computer_dices) != 5 and len(left_computer_dices) >= 1:
                            ndice_aside(*left_computer_dices)
                    
                    
                        print(
                            f"======                  YOU HAVE {sum_roll_result(left_dices + current_roll)} POINTS AT THE MOMENT !                  ======")
                        print(
                            f"===== COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dices + current_computer_roll)} POINTS AND WAITING FOR YOUR TURNS !  ======")
                        if number_of_rolls > 0:
                            print('''
                    ***********************************************************************
                    ==========      YOU CAN KEEP THAT SCORE. TYPE [DONE/D]       ==========
                    ***********************************************************************
                    ==========         YOU CAN ROLL AGAIN. TYPE [ROLL/R]         ==========
                    ***********************************************************************
                    ''')
                    if number_of_rolls == 0:
                        if computer_turns != 0:
                            print("=============         COMPUTER'S DICES     ============")
                            ndice_aside(*left_computer_dices + current_computer_roll)
                  
                     
                        print("***********************************************************************")
                        print(
                            f"======                  YOU HAVE {sum_roll_result(left_dices + current_roll)} POINTS !                     ======")
                        print(
                            f"======           COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dices + current_computer_roll)} POINTS !        ======")

                    # if sum_roll_result(left_computer_dices) + sum_roll_result(current_computer_roll) <= 5:
                        
                    #         ndice_aside(*left_computer_dices)
                    #         # if computer_turns == 0:
                    #         ndice(*computer_roll_results)
    return sum_roll_result(left_dices), sum_roll_result(
        left_computer_dices), left_dices, left_computer_dices, current_bet


def check_result(sum_left_dices, sum_left_computer_dices, left_dices, left_computer_dices, current_bet):
    money = 0

    if left_dices == [6, 6, 6, 6, 6]:

        print("=====     YOU SHOOT THE MOON WITH [6][6][6][6][6]              =====")
        print(f"======                  YOU WIN ${current_bet * 2}                            ======")
        money += current_bet
        

    elif left_computer_dices == [6, 6, 6, 6, 6]:
        print("=====     COMPUTER SHOOT THE MOON WITH [6][6][6][6][6]           =====")
        print(f"======                  YOU LOSE ${current_bet}                             ======")
        money -= current_bet
    

    else:
        if sum_left_computer_dices > sum_left_dices:
            print(f"======                          YOU WIN ${current_bet * 2}                       ======")
            money += current_bet
    
        elif sum_left_computer_dices < sum_left_dices:
            print(f"======                  YOU LOSE ${current_bet}                              ======")
            money -= current_bet
        
        elif sum_left_computer_dices == sum_left_dices:
            print("THE SCORE IS TIED, THERE WILL BE ONE MORE ROLL OF THE FIVE DICES")
            time.sleep(2)
            print("***********************************************************************")
            roll_results = roll()
            computer_roll_results = roll()
            print("Your turn ...")
            time.sleep(1)
            dice_faces = ndice(*roll_results)
            current_roll = roll_results

            print('''
    ***********************************************************************
    ***********************************************************************

            ''')

            print("***********************************************************************")
            print(f"======                  YOU HAVE {sum_roll_result(roll_results)} POINTS !                     ======")
            print(f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(computer_roll_results)} POINTS !         ======")

            print("Computer's turn ...")
            time.sleep(1)
            dice_faces = ndice(*computer_roll_results)
            current_computer_roll = computer_roll_results


        
            if left_computer_dices == [6, 6, 6, 6, 6]:
                print("=====     COMPUTER SHOOT THE MOON WITH [6][6][6][6][6]          =====")
                print(f"======                  YOU LOSE ${current_bet}                             ======")
                money -= current_bet

            elif left_dices == [6, 6, 6, 6, 6]:
                print("=====     YOU SHOOT THE MOON WITH [6][6][6][6][6]           =====")
                print(f"======                  YOU WIN ${current_bet * 2}                            ======")
                money += current_bet
            elif sum_roll_result(current_roll) < sum_roll_result(current_computer_roll):
                print(f"======                  YOU WIN ${current_bet * 2}                            ======")
                money += current_bet

            elif sum_roll_result(current_computer_roll) < sum_roll_result(current_roll):
                print(f"======                  YOU LOSE ${current_bet}                             ======")
                money -= current_bet
            
            else:
        
                print(f"THE SCORE IS TIED AGAIN. THERE IS NO WINNER U TAKE BACK ${current_bet}")

    return money



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
    sum_left_dices, sum_left_computer_dices, left_dices, left_computer_dices, current_bet = bet(money_amount)

if still_play:
    money = check_result(sum_left_dices, sum_left_computer_dices, left_dices, left_computer_dices, current_bet)
    money_amount += money
    players[player_name] = money_amount
    

while True:
    menu = input('''
    ***********************************************************************
    ***********************************************************************
    ==============           TO BET PRESS [B]               ===============
    ==============       TO MAKE DEPOSTI PRESS  [D]         ===============
    ==============   TO WITHDRAW YOUR MONEY PRESS [W]       ===============
    ==============  TO SEE YOUR CURRENT BANK PRESS [C]      ===============
    ==============          TO QUIT PRESS  [Q]              ===============
    ***********************************************************************
    ***********************************************************************
    ''').upper().strip()
    if menu == "B":
        if money_amount > 0:
            sum_left_dices, sum_left_computer_dices, left_dices, left_computer_dices, current_bet = bet(money_amount)
            money = check_result(sum_left_dices, sum_left_computer_dices, left_dices, left_computer_dices, current_bet)
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
              
                print(F" {''.join([key for key in players.keys()])} YOU SUCCESSFULLY WITHDRAW ${withdraw}\n=====       {''.join([key for key in players.keys()])} YOU HAVE TOAL MONEY: ${money_amount}       =====")
        else:
            print("NO MONEY IN YOUR ACCOUNT !")
    elif menu == "D":
        if player_name == '':
           player_name = player("ENTER YOUR NAME: ") 
           players[player_name] = 0
        else:
            new_deposit = is_positive('PLEASE DEPOSIT AMOUNT OF MONEY TO PLAY WITH. ONLY INTEGER NUMBERS, NO COINS ')
            money_amount += new_deposit
            print(F"YOU SUCCESSFULLY DEPOSIT ${new_deposit}\n=====     TOAL MONEY: ${money_amount}     =====")
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
