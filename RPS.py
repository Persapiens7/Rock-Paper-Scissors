import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def play(self):
        return moves[0]

    def learn(self, last_opponent_move):
        pass


class RandomPlayer(Player):
    def play(self):
        index = random.randint(0, 2)
        return moves[index]


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_opponent_move = None

    def play(self):
        if self.last_opponent_move is None:
            return Player.play(self)
        return self.last_opponent_move

    def learn(self, last_opponent_move):
        self.last_opponent_move = last_opponent_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def play(self):
        move = None
        if self.last_move is None:
            move = Player.play(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move


class HumanPlayer(Player):
    def play(self):
        player_move = input('What is your move:\n' +
                            'rock, paper or scissors?\n')
        while player_move not in moves:
            player_move = input('\nThat is an invalid move.\n' +
                                'Is it: rock, paper or scissors?')
        return player_move


class Game():
    def __init__(self):
        self.first_player = HumanPlayer()
        self.second_player = CyclePlayer()

    def match(self):
        input('\nWelcome to Rock, Paper or Scissors!\n\n' +
              'The rules of the game are the following:\n' +
              'rock beats scissors\n' +
              'paper beats rock\n' +
              'and scissors beats paper\n\n' +
              'Press enter to start\n')
        try:
            while True:
                self.play_round()
                print('The score: ' + str(self.first_player.score) + ' to ' +
                      str(self.second_player.score) + '\n')
                input('Press enter to play again\n' +
                      'or ctrl + C and then enter to quit\n')
        except KeyboardInterrupt:
            print('\n\nThanks for playing rock, paper, scissors!')
            if self.first_player.score > self.second_player.score:
                print('You won!')
            elif self.first_player.score > self.second_player.score:
                print('Computer won!')
            else:
                print('The game was a draw!')
            print('Final score: ' + str(self.first_player.score) + ' to ' +
                  str(self.second_player.score))

    def play_round(self):
        first_player_move = self.first_player.play()
        second_player_move = self.second_player.play()
        result = Game.winning_round(first_player_move, second_player_move)

        self.first_player.learn(second_player_move)
        self.second_player.learn(first_player_move)

        print('You picked "' + first_player_move + '" and computer picked "' +
              second_player_move + '"')
        if result == 1:
            self.first_player.score += 1
            print('=> You won!\n')
        elif result == 2:
            self.second_player.score += 1
            print('=> Computer won!\n')
        else:
            print('=> That is a draw!\n')

    @classmethod
    def winning_round(cls, first_move, second_move):
        if Game.winning_move(first_move, second_move):
            return 1
        elif Game.winning_move(second_move, first_move):
            return 2
        else:
            return 0

    @classmethod
    def winning_move(cls, first_move, second_move):
        if (first_move == 'rock' and second_move == 'scissors'):
            return True
        elif (first_move == 'paper' and second_move == 'rock'):
            return True
        elif (first_move == 'scissors' and second_move == 'paper'):
            return True
        return False


RPS = Game()
RPS.match()
