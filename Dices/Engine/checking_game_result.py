import time
from Faces.Face import ndice
from .rolling import  roll, sum_roll_result


def check_result(sum_left_dice, sum_left_computer_dice, left_dice, left_computer_dice, current_bet):
    money = 0

    if left_dice == [6, 6, 6, 6, 6]:

        print("=====     YOU SHOOT THE MOON WITH [6][6][6][6][6]              =====")
        print(f"======                  YOU WIN ${current_bet * 2}                            ======")
        money += current_bet
        

    elif left_computer_dice == [6, 6, 6, 6, 6]:
        print("=====     COMPUTER SHOOT THE MOON WITH [6][6][6][6][6]           =====")
        print(f"======                  YOU LOSE ${current_bet}                             ======")
        money -= current_bet
    

    else:
        if sum_left_computer_dice > sum_left_dice:
            print(f"======                          YOU WIN ${current_bet * 2}                       ======")
            money += current_bet
    
        elif sum_left_computer_dice < sum_left_dice:
            print(f"======                  YOU LOSE ${current_bet}                              ======")
            money -= current_bet
        
        elif sum_left_computer_dice == sum_left_dice:
            print("THE SCORE IS TIED, THERE WILL BE ONE MORE ROLL OF THE FIVE DICE")
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

            print("Computer's turn ...")
            time.sleep(1)
            dice_faces = ndice(*computer_roll_results)
            current_computer_roll = computer_roll_results



            print(f"======                  YOU HAVE {sum_roll_result(roll_results)} POINTS !                      ======")
            print(f"=====           COMPUTER REACHED THE SCORE OF {sum_roll_result(computer_roll_results)} POINTS !         ======")

        
            if left_computer_dice == [6, 6, 6, 6, 6]:
                print("=====     COMPUTER SHOOT THE MOON WITH [6][6][6][6][6]          =====")
                print(f"======                  YOU LOSE ${current_bet}                             ======")
                money -= current_bet

            elif left_dice == [6, 6, 6, 6, 6]:
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
        
                print(f"===== THE SCORE IS TIED AGAIN. THERE IS NO WINNER U TAKE BACK ${current_bet} ======")

    return money