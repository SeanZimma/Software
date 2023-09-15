#!/usr/bin/env python
# coding: utf-8

# In[10]:


from IPython.display import clear_output
board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
    
def display_board(board):
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   '),
        print(board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   ')
        print('---------------')
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   ')
        print(board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6])
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   ')
        print('---------------')
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   ')
        print(board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3])
        print('   ' + ' ' + '|' + ' ' + '   ' + ' ' + '|' + ' ' + '   ')


# In[11]:


display_board(board)


# In[12]:


option_list = []
def user_input():
        print('Welcome to Tic Tac Toe!\n')
    
        acceptable_values_wanna_play = ['YES', 'NO']
        ask_play = False
        
        while ask_play == False:
            play = input('Would you like to play? Enter YES or NO:\n')
            wanna_play = play.upper()
            if wanna_play not in acceptable_values_wanna_play:
                print("I don't understand,please try again\n")
            elif wanna_play == 'YES':
                ask_play = True
            else:
                print('Okay. See you whenever you want!')
                return 'NO'
        
        acceptable_options = ['X','O']
        ask_option = False
        player_two_option = ''
        
        while ask_option == False:
            if ask_play == True:
                player_one_option_lower = input('Player 1 - Choose your option. Enter X or O:\n')
            else:
                break
                
            player_one_option = player_one_option_lower.upper()
            
            if player_one_option not in acceptable_options:
                print('Please enter a valid value! Enter X or O')
            else:
                ask_option = True
        
        if player_one_option == 'X':
            player_two_option = 'O'
        else:
            player_two_option = 'X'
        
        print(f'Player one : {player_one_option}')
        print(f'Player two : {player_two_option}')
        
        option_list.append(' ' + player_one_option + ' ')
        option_list.append(' ' + player_two_option + ' ')
        return option_list


# In[13]:


user_input()


# In[14]:


def replacement_function(board, option):
        choice = 'WRONG'
        boolean_choice = False
        acceptable_values_choice = [1,2,3,4,5,6,7,8,9]
        boolean = False
        while choice.isdigit() == False or boolean_choice == False:
            
            choice = input("Choose a position (1-9):\n")
            if choice.isdigit() == True:
                choice_int = int(choice)
            else:
                print("Please enter a numerical value\n")
                continue
                
            if choice_int not in acceptable_values_choice:
                print("Please enter a number between 1 and 9\n")
                continue
            else:
                boolean_choice = True
                break
                
        while boolean == False:
            if board[choice_int] == '   ':
                board[choice_int] = option
                boolean = True
            else:
                print("This position is already taken. Enter another value!")
                choice = input("Choose a position (1-9):\n")
                choice_int = int(choice)
            
        return board


# In[9]:


replacement_function(board,option_list[0])


# In[33]:


def game_on():
    
    #Firstly, ask the player if he would like to play
    
        player_one_turn = True
        player_two_turn = False
        win_boolean = False
        continue_to_play = True
        result =user_input()
        if result == 'NO':
            win_boolean = True
        board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
        
        while win_boolean == False or continue_to_play == True:
            
            display_board(board)
            
        #Secondly, players have to select a specific box
        
            if player_one_turn == True:
                    replacement_function(board, option_list[0])
                    player_one_turn = False
                    player_two_turn = True
                    
            else:
                    replacement_function(board, option_list[1])
                    player_one_turn = True
                    player_two_turn = False
             
            #Combination:
            
            if board[1] == option_list[0] and board[2] == option_list[0] and board[3] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        
                        #Ask players if they would like to play again
                        
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[1] == option_list[1] and board[2] == option_list[1] and board[3] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[4] == option_list[0] and board[5] == option_list[0] and board[6] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[4] == option_list[1] and board[5] == option_list[1] and board[6] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[7] == option_list[0] and board[8] == option_list[0] and board[9] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[7] == option_list[1] and board[8] == option_list[1] and board[9] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[1] == option_list[0] and board[4] == option_list[0] and board[7] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[1] == option_list[1] and board[4] == option_list[1] and board[7] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[2] == option_list[0] and board[5] == option_list[0] and board[8] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[2] == option_list[1] and board[5] == option_list[1] and board[8] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[3] == option_list[0] and board[6] == option_list[0] and board[9] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[3] == option_list[1] and board[6] == option_list[1] and board[9] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[1] == option_list[0] and board[5] == option_list[0] and board[9] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[1] == option_list[1] and board[5] == option_list[1] and board[9] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[3] == option_list[0] and board[5] == option_list[0] and board[7] == option_list[0]:
                display_board(board)
                print("Player one won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            elif board[3] == option_list[1] and board[5] == option_list[1] and board[7] == option_list[1]:
                display_board(board)
                print("Player two won!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            
            string_empty = '   '
            if string_empty not in board:
                display_board(board)
                print("That's a tie!")
                win_boolean = True
                if win_boolean == True:
                    intention = ''
                    intention_possible_values =['YES','NO']
                    ask_play= False
                    while ask_play == False:
                        intention = input("Would you like to play again? Enter YES or NO\n")
                        intention_upper = intention.upper()
                        if intention_upper not in intention_possible_values:
                            print("I don't understand, please enter YES or NO\n")
                        else:
                            ask_play = True
                
                if intention_upper == 'YES':
                    board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
                    continue_to_play = True
                    player_one_turn = True
                    player_two_turn = False
                else:
                    continue_to_play = False
                    print("Okay. Thank you for playing!")
            else:
                continue
            


# In[34]:


game_on()


# In[26]:


user_input()


# In[4]:


win_boolean = True
def continue_to_play():
    if win_boolean == True:
        intention = ''
        intention_possible_values =['YES','NO']
        ask_play= False
        while ask_play == False:
            intention = input("Would you like to play again? Enter YES or NO")
            intention_upper = intention.upper()
            if intention_upper not in intention_possible_values:
                print("I don't understand, please enter YES or NO")
            else:
                ask_play = True
                
        if intention_upper == 'YES':
            board=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
        else:
            continue_to_play = False


# In[5]:


continue_to_play()


# In[ ]:




