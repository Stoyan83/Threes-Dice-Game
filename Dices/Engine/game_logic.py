from .constraint import bet_is_ligit
import time
from Faces.Face import ndice, ndice_aside
from .rolling import next_roll, roll, sum_roll_result
from .command_logic import command, remove_smallest
from .constraint import valid_dice



def bet(money_amount):
    current_money = money_amount
    computer_turns = 4
    number_of_rolls = 4
    left_dice = []
    left_computer_dice = []
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
                if current_computer_roll + left_computer_dice == [6, 6, 6, 6, 6]:
                    # play = False
                    left_computer_dice = [6, 6, 6, 6, 6]
                    return sum_roll_result(left_dice), sum_roll_result(
                    left_computer_dice), left_dice, left_computer_dice , current_bet
                elif current_roll + left_dice == [6, 6, 6, 6, 6]:
                    # play = False
                    left_dice = [6, 6, 6, 6, 6]
                    return sum_roll_result(left_dice), sum_roll_result(
                    left_computer_dice), left_dice, left_computer_dice, current_bet
                   
                if number_of_rolls > 1:
                    current_command = command("MAKE YOUR CHOICE: ")
                if current_command == "D" or current_command == "DONE":

                 
                    if sum_roll_result(current_computer_roll + left_computer_dice) >= sum_roll_result(
                            current_roll + left_dice) and \
                            sum_roll_result(left_computer_dice) + sum_roll_result(current_computer_roll) > 5:
                        try:
                            while computer_turns > 0:
                                computer_turns -= 1
                                new_dice, aside_computer = remove_smallest(current_computer_roll)
                                left_computer_dice += aside_computer

                                next_computer = next_roll(len(new_dice))
                                current_computer_roll = next_computer
                                if computer_turns > 1:
                                    print("***********************************************************************")
                                    print("Computer's turn ...")
                                time.sleep(1)
                                dice_faces = ndice(*next_computer)
                                if sum_roll_result(current_computer_roll + left_computer_dice) < sum_roll_result(
                                        current_roll + left_dice):
                                    print("=============         COMPUTER'S DICE     ============")
                                    ndice_aside(*left_computer_dice)
                
                                    print("***********************************************************************")
                                    print(
                                        f"======                  YOU HAVE {sum_roll_result(current_roll)} POINTS AT THE MOMENT !        ======")
                                    print(
                                        f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dice + current_computer_roll)} POINTS !         ======")
                                    break
                                if sum_roll_result(current_computer_roll + left_computer_dice) >= sum_roll_result(
                                        current_roll + left_dice):

                                    print("=============         COMPUTER'S DICE     ============")
                                    ndice_aside(*left_computer_dice)
                
                                    print("***********************************************************************")
                                    print(
                                        f"======                  YOU HAVE {sum_roll_result(left_dice + current_roll)} POINTS !                     ======")
                                    print(
                                        f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dice + current_computer_roll)} POINTS !        ======")
                        except ValueError:
                            pass

                    left_dice += current_roll
                    left_computer_dice += current_computer_roll
                    
                
                 
                    play = False
                    break
                if number_of_rolls == 0:
                    left_dice += current_roll
                    left_computer_dice += current_computer_roll
                    play = False

                    break

                if current_command == "R" or current_command == "ROLL":
                
                    number_of_rolls -= 1

                    aside_dice = valid_dice(len(current_roll),
                                            "TYPE NUMBER OF THE DICE YOU WANT TO SET ASIDE, COUNTING BACKWARDS FROM RIGHT TO LEFT: ")

                    set_aside = current_roll[::-1].pop(aside_dice - 1)
                    left_dice.append(int(set_aside))

                    
                   

                    print("Your turn ...")
                    time.sleep(1)
                    roll_results = [int(x) for x in range(len(current_roll)) if x != 0]
                    next = next_roll(len(roll_results))
                    dice_faces = ndice(*next)
                    current_roll = next
                    if len(left_dice) < 4:
                        ndice_aside(*left_dice)

                        print("*********************************************************")
                        print("*********************************************************")

                    if sum_roll_result(left_computer_dice) + sum_roll_result(current_computer_roll) > 5:
                        new_dice, aside_computer = remove_smallest(current_computer_roll)
                        left_computer_dice += aside_computer

                        next_computer = next_roll(len(new_dice))
                        print("Computer's turn ...")
                        time.sleep(1)
                        dice_faces = ndice(*next_computer)

                        current_computer_roll = next_computer
                        computer_turns -= 1

                        if len(left_computer_dice) != 4 and len(left_computer_dice) > 0:
                            ndice_aside(*left_computer_dice)
                    
                        if number_of_rolls > 0:

                            print(
                                f"======                  YOU HAVE {sum_roll_result(left_dice + current_roll)} POINTS AT THE MOMENT !       ======")
                            print(
                                f"=====          COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dice + current_computer_roll)} POINTS        !  ======")

                            print('''
                    ***********************************************************************
                    ==========      YOU CAN KEEP THAT SCORE. TYPE [DONE/D]       ==========
                    ***********************************************************************
                    ==========         YOU CAN ROLL AGAIN. TYPE [ROLL/R]         ==========
                    ***********************************************************************
                    ''')
                    if number_of_rolls == 0:
                        ndice_aside(*left_dice +    current_roll)
                        print("=============         COMPUTER'S DICE     ============")
                        ndice_aside(*left_computer_dice + current_computer_roll)
                

                        print("***********************************************************************")
                        print(
                                f"======                  YOU HAVE {sum_roll_result(left_dice + current_roll)} POINTS !                     ======")
                        print(
                                f"======            COMPUTER REACHED THE SCORE OF {sum_roll_result(left_computer_dice + current_computer_roll)} POINTS !        ======")



                    if computer_turns != 0:
                       
                        if number_of_rolls >= 1:
                            print("***********************************************************************")
                            print(
                                f"======                  YOU HAVE {sum_roll_result(left_dice + current_roll)} POINTS !                     ======")
                     
    return sum_roll_result(left_dice), sum_roll_result(
            left_computer_dice), left_dice, left_computer_dice, current_bet