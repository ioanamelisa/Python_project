# TIC-TAC-TOE

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for keys in theBoard:
    board_keys.append(keys)


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')


def game():
    turn = 'x'
    count = 0

    for i in range(28):
        print_board(theBoard)
        print("It's your turn," + turn + " Move to witch place?")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. \nMove to witch place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("\nGame Over\n")
                print(" **** " + turn + " won **** ")
                break
        if count == 9:
            print("\nGame Over\n")
            print("It's a tie!")
        if turn == 'x':
            turn = '0'
        else:
            turn = 'x'
    restart = input("Do you want to play again? (yes/no)")
    if restart == 'yes' or restart == 'YES':
        for key in board_keys:
            theBoard[key]= ' '
        game()

if __name__ == '__main__':
    game()


