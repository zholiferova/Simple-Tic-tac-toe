import numpy as np

class board:
    def new():
        return np.full((3,3), "-", dtype = str)
    def draw_board(b):
        print('{}  {}  {} \n'.format(b[0,0],b[0,1],b[0,2]))
        print('{}  {}  {} \n'.format(b[1,0],b[1,1],b[1,2]))
        print('{}  {}  {} \n'.format(b[2,0],b[2,1],b[2,2]))
def move (b, player):
    while True:
        print("Player {}, ".format(player), end = " "),
        n = input('please, select the column (1, 2 or 3) of your next move: ')
        print("Player {}, ".format(player), end = " "),
        m = input('please, select the row (1, 2 or 3) of your next move: ')
        if (n in ["1", "2", "3"]) and (m in ["1", "2", "3"]):
            n = int(n)-1
            m = int(m)-1
            if (b[n,m]=="-"):
                b[n,m] = player
                board.draw_board(b)
                return (b, n, m)
        else:
            print('You made a wrong choice, please try again')


def play_game():
    g = board.new()
    board.draw_board(g)
    while True:
        player_1 = input('The first player, do you want to play X (enter X) or 0 (enter 0):')
        if player_1 == 'X':
            player_2 = '0'
            print(player_1, player_2)
            break
        elif player_1 == '0':
            player_2 = 'X'
            print(player_1, player_2)
            break
        else:
            print('You entered a wrong symbol, please try again')
    player = player_2
    while np.any(g == '-'):
        if player == player_1:
            player = player_2
        else:
            player = player_1
        (g, n, m) = move(g, player)
        comp = np.equal(g, player)
        if (comp[:,m].all() or comp[n,:].all() or comp.diagonal().all()
        or (np.rot90(comp)).diagonal().all()):
            print('Congratulations, {}, you win!'.format(player))
            return
    print('It is a tie game!')
# driver code
print("This is a simple tic-tac-toe game. Before playing, select ", end = "")
print("whether you want to play X or 0, then make your move by choosing column and row.")
print("Good luck!")
play_game()
