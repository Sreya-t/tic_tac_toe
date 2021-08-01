import random

class Board:
    def __init__(self):
        self.gameBoard = [' '] * 10
    def drawBoard(self):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.gameBoard[7] + ' | ' + self.gameBoard[8] + ' | ' + self.gameBoard[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.gameBoard[4] + ' | ' + self.gameBoard[5] + ' | ' + self.gameBoard[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.gameBoard[1] + ' | ' + self.gameBoard[2] + ' | ' + self.gameBoard[3])
        print('   |   |')

    def makeMove(self, letter, move):
        self.gameBoard[move] = letter

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.gameBoard[7] == le and self.gameBoard[8] == le and self.gameBoard[9] == le) or  # across the top
                (self.gameBoard[4] == le and self.gameBoard[5] == le and self.gameBoard[6] == le) or  # across the middle
                (self.gameBoard[1] == le and self.gameBoard[2] == le and self.gameBoard[3] == le) or  # across the self.gameBoardttom
                (self.gameBoard[7] == le and self.gameBoard[4] == le and self.gameBoard[1] == le) or  # down the left side
                (self.gameBoard[8] == le and self.gameBoard[5] == le and self.gameBoard[2] == le) or  # down the middle
                (self.gameBoard[9] == le and self.gameBoard[6] == le and self.gameBoard[3] == le) or  # down the right side
                (self.gameBoard[7] == le and self.gameBoard[5] == le and self.gameBoard[3] == le) or  # diagonal
                (self.gameBoard[9] == le and self.gameBoard[5] == le and self.gameBoard[1] == le))  # diagonal

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.gameBoard[move] == ' '


class Game(Board):
    def getPlayer1Move(self,gameBoard):
        # Let player 1 type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not gameBoard.isSpaceFree(int(move)):
            print('What is player 1\'s next move? (1-9)')
            move = input()
        return int(move)

    def getPlayer2Move(self,gameBoard):
        # Let player 2 type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not gameBoard.isSpaceFree(int(move)):
            print('What is player 2\'s next move? (1-9)')
            move = input()
        return int(move)

    def inputPlayer1Letter(self):
        # Lets player 1 type which letter they want to be.
        # Returns a list with the player 1's letter as the first item, and player 2's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does player 1 want to be X or O?')
            letter = input().upper()
        # the first element in the tuple is the player 1's letter, the second is player 2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'player2'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def startGame(self):
        print('Welcome to Tic Tac Toe!')
        while True:
            # Reset the board
            game = Board()
            player1Letter, player2Letter = self.inputPlayer1Letter()
            turn = self.whoGoesFirst()
            print(turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player1':
                    # Player 1's turn.
                    game.drawBoard()
                    move = self.getPlayer1Move(game)
                    game.makeMove(player1Letter, move)

                    if game.isWinner(player1Letter):
                        game.drawBoard()
                        print('Player 1 has won the game!')
                        gameIsPlaying = False
                    else:
                        if game.isBoardFull():
                            game.drawBoard()
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player2'

                else:
                    # Player 2's turn.
                    game.drawBoard()
                    move = self.getPlayer2Move(game)
                    game.makeMove( player2Letter, move)

                    if game.isWinner( player2Letter):
                        game.drawBoard()
                        print('Player 2 has won the game!')
                        gameIsPlaying = False
                    else:
                        if game.isBoardFull():
                            game.drawBoard()
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player1'
            if not self.playAgain():
                break


game = Game()
game.startGame()