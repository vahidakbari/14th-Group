from random import randint
# Variables
valid_answers = {'Rock': 0, 'Paper': 1, 'Scissor': 2}
result_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]  # result_matrix[user_choice][computer_choice]
com_res_dic = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
user_res_dic = {'R': 'Rock', 'S': 'Scissor', 'P': 'Paper', 'Paper': 'Paper', 'Rock': 'Rock', 'Scissor': 'Scissor'}
user_score = 0
computer_score = 0
rounds_played = 0
result_found = 0

# Game
while True:  # Receiving Number of Rounds
    round_input = input('How many rounds would you like to play?')
    if round_input.isdigit():
        print(f'Let\'s have fun for {round_input} rounds!' if int(round_input) > 1
              else f'Let\'s have fun for {round_input} round!')
        print('You can exit the game at any time by pressing [Q/Quit]!')
    else:
        print('Number of rounds must be an integer only. Please try again!')
        continue
    while user_score + computer_score < int(round_input):  # Main Game
        print('*' * 40)
        user_choice = input(f'Round {rounds_played + 1}: What\'s your choice?')
        print('*' * 40)
        computer_response = randint(0, 2)
        if user_choice.lower() in 'q' or user_choice.lower() in 'quit':
            print('We hope to see you soon!')
            break
        else:
            result_found = 0
            for string in user_choice.lower().split(' '):
                if result_found != 0:
                    break
                for resp in valid_answers.keys():
                    if string.capitalize() == resp or string.capitalize() == resp[0]:
                        result_found += 1
                        if result_matrix[valid_answers[resp]][computer_response] == 1:
                            user_score += 1
                            print(" " * 13, 'Damn! You Won!')
                        elif result_matrix[valid_answers[resp]][computer_response] == -1:
                            computer_score += 1
                            print(" " * 8, 'Ha Ha! I beat you!')
                        elif result_matrix[valid_answers[resp]][computer_response] == 0:
                            print(" " * 6, 'It\'s a tie! Let\'s try again!')
                        rounds_played += 1
                        print(f'Round {rounds_played}')
                        print(
                            f'My choice was {com_res_dic[computer_response]}, '
                            f'Your choice was {user_res_dic[string.capitalize()]}')
                        print(f'User Score: {user_score}')
                        print(f'Computer Score: {computer_score}')
                        break
                    else:
                        continue
                else:
                    continue
            else:
                if result_found:
                    continue
                else:
                    print('Please choose a valid option only to proceed!')
                    continue
    else:  # Showing Results and asking for replay
        print('*' * 40)
        print(" " * 13, 'Final Results')
        print(f'User Score: {user_score}')
        print(f'Computer Score: {computer_score}')
        if computer_score > user_score:
            print('Computer Wins. Better luck next time!')
        elif computer_score < user_score:
            print('You Win!')
        else:
            print('Looks like someone\'s as good as me!')
        print('*' * 40)
        repeat_game = input('Would you like to play again? [yes/no]')
        if repeat_game.lower() == 'yes' or repeat_game.lower() == 'y':
            user_score = 0
            computer_score = 0
            rounds_played = 0
            tie_count = 0
            continue
        else:
            print('Playing with you was fun :)')
            break
    if True:  # if a user decides not to play after stating the rounds, hitting q will enable this option
        break
