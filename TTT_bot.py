import json
import random
from TTT_board import Board

REWARD = {1: 100,
          2: -100,
          0: -3}


class Bot(object):
    def __init__(self, color, board, epsilon=0.1, alpha=0.7, gamma=0.9):
        self.board = board
        self.color = color
        self.load_strategy()
        self.moves = []
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def get_strategy_color(self, board_color):
        if board_color == self.color:
            return 1
        elif board_color == 0:
            return 0
        else:
            return 2

    def get_state_from_board(self):
        state = 0
        for i in range(3):
            for j in range(3):
                strategy_color = (self.board.get_color((i, j)))
                state = state * 10 + strategy_color
        return state

    def get_board_from_state(self, state):

        board1 = Board()
        q = []
        while state > 0:
            digit = int(state % 10)
            q.append(digit)
            state = int(state / 10)
        for i in range(9 - len(q)):
            q.append(0)
        q.reverse()

        for i in range(9):
            if (q[i] != 0):
                if (i <= 2):
                    if (i == 0):
                        where = [0, 0]
                    elif (i == 1):
                        where = [0, 1]
                    else:
                        where = [0, 2]
                elif (i <= 5):
                    if (i == 3):
                        where = [1, 0]
                    elif (i == 4):
                        where = [1, 1]
                    else:
                        where = [1, 2]
                else:
                    if (i == 6):
                        where = [2, 0]
                    elif (i == 7):
                        where = [2, 1]
                    else:
                        where = [2, 2]

                board1.move(q[i], where)

        return board1

    def find_new_state(self, state, move):
        q = []
        while state > 0:
            digit = int(state % 10)
            q.append(digit)
            state = int(state / 10)
        for i in range(9 - len(q)):
            q.append(0)
        q.reverse()
        if move[0] == 0:
            if move[1] == 0:
                q[0] = self.color
            elif move[1] == 1:
                q[1] = self.color
            else:
                q[2] = self.color
        elif move[0] == 1:
            if move[1] == 0:
                q[3] = self.color
            elif move[1] == 1:
                q[4] = self.color
            else:
                q[5] = self.color
        elif move[0] == 2:
            if move[1] == 0:
                q[6] = self.color
            elif move[1] == 1:
                q[7] = self.color
            else:
                q[8] = self.color
        new_state = 0
        for i in range(len(q)):
            new_state = new_state * 10 + q[i]
        return new_state

    def load_strategy(self):

        self.strategy = {}

        try:
            fd = open('strategy.json', 'r')
        except IOError:
            return

        self.strategy = json.load(fd)
        fd.close()

    def act(self):

        state = self.get_state_from_board()

        action = self.choose_action_from_state(state, self.board)

        self.moves.append((state, action))

        self.board.move(self.color, action)

    def learning(self):

        strategy_color = self.get_strategy_color(self.board.get_winner())

        reward = REWARD[strategy_color]

        for i in range(len(self.moves)):

            if i == len(self.moves) - 1:

                state = self.moves[i][0]

                action = []
                action.append(self.moves[i][1][0])
                action.append(self.moves[i][1][1])

                value = self.Q(state, action, reward) + self.alpha * (
                    reward - self.Q(state, action, reward))

                self.sarsa_learn(state, action, value)
            else:
                state = self.moves[i][0]

                action = []
                action.append(self.moves[i][1][0])
                action.append(self.moves[i][1][1])

                new_state = self.moves[i + 1][0]

                new_action = []
                new_action.append(self.moves[i + 1][1][0])
                new_action.append(self.moves[i + 1][1][1])

                value = self.sarsa(state, action, new_state, new_action, reward)

                self.sarsa_learn(state, action, value)

    def choose_action_from_state(self, state, board):

        possible_actions = board.get_possible_actions()

        strategy = self.strategy
        if random.random() < self.epsilon:

            action = random.choice(possible_actions)

        else:
            action = None
            if str(state) in strategy:

                max_score_action = max(strategy[str(state)], key=lambda a: a['score'])

                if max_score_action['score'] > 0:
                    action = tuple(max_score_action['move'])

                else:

                    for act in strategy[str(state)]:
                        if tuple(act['move']) in possible_actions:
                            possible_actions.remove(tuple(act['move']))
                if len(possible_actions) == 0:
                    action = tuple(max_score_action['move'])

            if action == None:
                action = random.choice(possible_actions)

        return action

    def Q(self, state, action, reward):
        self.load_strategy()
        strategy = self.strategy
        if str(state) in strategy:
            for act in strategy[str(state)]:
                if act['move'] == action:
                    return act['score']
            else:
                return reward
        else:
            return reward

    def sarsa(self, state1, action1, state2, action2, r):

        value = self.Q(state1, action1, r) + self.alpha * (
            r + self.gamma * self.Q(state2, action2, r) - self.Q(state1, action1, r))

        return value

    def sarsa_learn(self, state, action, value):

        self.load_strategy()
        strategy = self.strategy
        if str(state) not in strategy:

            strategy[str(state)] = []
        else:

            for act in strategy[str(state)]:
                if act['move'] == action:
                    strategy[str(state)].remove(act)

        strategy[str(state)].append({'move': action,
                                     'score': value})

        fd = open('strategy.json', 'w')
        json.dump(strategy, fd)
        fd.close()
