from colorama import Fore
from colorama import Style

def main():
    player = player_turn("")
    board = make_board()
    while not (is_winner(board) or cat_game(board)):
        show_board(board)
        your_move(player,board)
        player = player_turn(player)
    show_board(board)
    print(f'{Fore.RED} Game over! Thanks for playing! {Style.RESET_ALL}')
        
def player_turn(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"
    
def make_board():
    board = []
    for box in range(9):
        board.append(box + 1)
    return board

    
def show_board(board): 
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()
    
def cat_game(board):
        for box in range(9):
            if board[box] != "x" and board[box] != 'o':
                return False
        return True
def is_winner (board):
        return(board[0] == board[1] == board[2] or
               board[3] == board[4] == board[5] or
               board[6] == board[7] == board[8] or
               board[0] == board[3] == board[6] or
               board[1] == board[4] == board[7] or
               board[2] == board[5] == board[8] or
               board[0] == board[4] == board[8] or
               board[2] == board[4] == board[6])

def your_move(player,board):
    box = int(input(f"{player} {Fore.BLUE}'s turn to choose a square:{Style.RESET_ALL} "))
    board[box - 1] = player

def player_turn(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"
    
if __name__ == "__main__":
    main()